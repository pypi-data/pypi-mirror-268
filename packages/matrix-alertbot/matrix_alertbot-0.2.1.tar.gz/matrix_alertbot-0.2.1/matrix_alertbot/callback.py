from __future__ import annotations

import logging
import re

from diskcache import Cache
from nio.client import AsyncClient
from nio.events import (
    InviteMemberEvent,
    KeyVerificationCancel,
    KeyVerificationKey,
    KeyVerificationMac,
    KeyVerificationStart,
    MegolmEvent,
    ReactionEvent,
    RedactionEvent,
    RoomMessageText,
    RoomMessageUnknown,
)
from nio.exceptions import LocalProtocolError, SendRetryError
from nio.responses import JoinError, RoomGetEventError, RoomSendError, ToDeviceError
from nio.rooms import MatrixRoom

import matrix_alertbot.matrix
from matrix_alertbot.alertmanager import AlertmanagerClient
from matrix_alertbot.chat_functions import strip_fallback
from matrix_alertbot.command import (
    AckAlertCommand,
    AngryUserCommand,
    CommandFactory,
    UnackAlertCommand,
)
from matrix_alertbot.config import Config

logger = logging.getLogger(__name__)


class Callbacks:
    def __init__(
        self,
        matrix_client: AsyncClient,
        alertmanager_client: AlertmanagerClient,
        cache: Cache,
        config: Config,
        matrix_client_pool: matrix_alertbot.matrix.MatrixClientPool,
    ):
        """
        Args:
            client: nio client used to interact with matrix.

            cache: Bot cache.

            alertmanager: Client used to interact with alertmanager.

            config: Bot configuration parameters.
        """
        self.matrix_client = matrix_client
        self.matrix_client_pool = matrix_client_pool
        self.cache = cache
        self.alertmanager_client = alertmanager_client
        self.config = config

    async def message(self, room: MatrixRoom, event: RoomMessageText) -> None:
        """Callback for when a message event is received

        Args:
            room: The room the event came from.

            event: The event defining the message.
        """
        # Ignore message when we aren't the leader in the client pool
        if self.matrix_client is not self.matrix_client_pool.matrix_client:
            return

        # Ignore messages from ourselves
        if event.sender in self.config.user_ids:
            return

        # Ignore messages from unauthorized room
        if room.room_id not in self.config.allowed_rooms:
            return

        # Extract the message text
        msg = strip_fallback(event.body)

        logger.debug(
            f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
            f"Event ID {event.event_id} | Sender {event.sender} | "
            f"Message received: {msg}"
        )

        user_id_patterns = []
        for user_id in self.config.user_ids:
            user, homeserver = user_id.split(":")
            username = user[1:]
            user_id_patterns.append(rf"@?{username}(:{homeserver})?")

        pattern = re.compile(
            rf"(^|\s+)({'|'.join(user_id_patterns)})(\s+|$)",
            re.IGNORECASE | re.MULTILINE,
        )
        if pattern.search(msg) is None:
            logger.debug(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Cannot process message: Bot was not mentionned."
            )
            return

        source_content = event.source["content"]
        reacted_to_event_id = (
            source_content.get("m.relates_to", {})
            .get("m.in_reply_to", {})
            .get("event_id")
        )

        if reacted_to_event_id is not None:
            logger.debug(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Command received is in reply to event ID {reacted_to_event_id}"
            )

        # Remove the mention of the bot
        cmd = pattern.sub(" ", msg).strip()
        try:
            command = CommandFactory.create(
                cmd,
                self.matrix_client,
                self.cache,
                self.alertmanager_client,
                self.config,
                room,
                event.sender,
                event.event_id,
                reacted_to_event_id,
            )
        except TypeError as e:
            logger.error(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Cannot process command '{cmd}': {e}"
            )
            return

        try:
            await command.process()
        except (SendRetryError, LocalProtocolError) as e:
            logger.exception(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Cannot send message to room.",
                exc_info=e,
            )

    async def invite(self, room: MatrixRoom, event: InviteMemberEvent) -> None:
        """Callback for when an invite is received. Join the room specified in the invite.

        Args:
            room: The room that we are invited to.

            event: The invite event.
        """
        # Ignore invites from unauthorized room
        if room.room_id not in self.config.allowed_rooms:
            return

        logger.debug(
            f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
            f"Sender {event.sender} | "
            f"Invitation received."
        )

        # Attempt to join 3 times before giving up
        for attempt in range(3):
            result = await self.matrix_client.join(room.room_id)
            if isinstance(result, JoinError):
                logger.error(
                    f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                    f"Sender {event.sender} | "
                    f"Error joining room (attempt {attempt}): {result.message}"
                )
            else:
                break
        else:
            logger.error(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Sender {event.sender} | "
                f"Unable to join room"
            )

        # Successfully joined room
        logger.info(
            f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
            f"Sender {event.sender} | "
            f"Room joined."
        )

    async def invite_event_filtered_callback(
        self, room: MatrixRoom, event: InviteMemberEvent
    ) -> None:
        """
        Since the InviteMemberEvent is fired for every m.room.member state received
        in a sync response's `rooms.invite` section, we will receive some that are
        not actually our own invite event (such as the inviter's membership).
        This makes sure we only call `callbacks.invite` with our own invite events.
        """
        if event.state_key == self.matrix_client.user_id:
            # This is our own membership (invite) event
            await self.invite(room, event)

    async def reaction(self, room: MatrixRoom, event: ReactionEvent) -> None:
        """A reaction was sent to one of our messages. Let's send a reply acknowledging it.

        Args:
            room: The room the reaction was sent in.

            event: The reaction event.

            reacted_to_id: The event ID that the reaction points to.
        """
        # Ignore message when we aren't the leader in the client pool
        if self.matrix_client is not self.matrix_client_pool.matrix_client:
            return

        # Ignore reactions from unauthorized room
        if room.room_id not in self.config.allowed_rooms:
            return

        # Ignore reactions from ourselves
        if event.sender in self.config.user_ids:
            return

        logger.debug(
            f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
            f"Event ID {event.event_id} | Sender {event.sender} | "
            f"Reaction received: {event.key}"
        )

        if event.key not in self.config.allowed_reactions:
            logger.warning(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Reaction not handled: {event.key}"
            )
            return

        alert_event_id = event.reacts_to
        # Get the original event that was reacted to
        event_response = await self.matrix_client.room_get_event(
            room.room_id, alert_event_id
        )
        if isinstance(event_response, RoomGetEventError):
            logger.warning(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Cannot get event related to the reaction and with event ID {alert_event_id}"
            )
            return
        reacted_to_event = event_response.event

        # Only acknowledge reactions to events that we sent
        if reacted_to_event.sender not in self.config.user_ids:
            return

        # Send a message acknowledging the reaction
        command = AckAlertCommand(
            self.matrix_client,
            self.cache,
            self.alertmanager_client,
            self.config,
            room,
            event.sender,
            event.event_id,
            alert_event_id,
        )

        try:
            await command.process()
        except (SendRetryError, LocalProtocolError) as e:
            logger.exception(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Cannot send message to room.",
                exc_info=e,
            )

        if event.key in self.config.insult_reactions:
            command = AngryUserCommand(
                self.matrix_client,
                self.cache,
                self.alertmanager_client,
                self.config,
                room,
                event.sender,
                event.event_id,
            )

            try:
                await command.process()
            except (SendRetryError, LocalProtocolError) as e:
                logger.exception(
                    f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                    f"Event ID {event.event_id} | Sender {event.sender} | "
                    f"Cannot send message to room.",
                    exc_info=e,
                )

    async def redaction(self, room: MatrixRoom, event: RedactionEvent) -> None:
        # Ignore message when we aren't the leader in the client pool
        if self.matrix_client is not self.matrix_client_pool.matrix_client:
            return

        # Ignore events from unauthorized room
        if room.room_id not in self.config.allowed_rooms:
            return

        # Ignore redactions from ourselves
        if event.sender in self.config.user_ids:
            return

        logger.debug(
            f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
            f"Event ID {event.event_id} | Sender {event.sender} | "
            f"Received event to remove event ID {event.redacts}"
        )

        command = UnackAlertCommand(
            self.matrix_client,
            self.cache,
            self.alertmanager_client,
            self.config,
            room,
            event.sender,
            event.event_id,
            event.redacts,
        )
        try:
            await command.process()
        except (SendRetryError, LocalProtocolError) as e:
            logger.exception(
                f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
                f"Event ID {event.event_id} | Sender {event.sender} | "
                f"Cannot send message to room.",
                exc_info=e,
            )

    async def decryption_failure(self, room: MatrixRoom, event: MegolmEvent) -> None:
        """Callback for when an event fails to decrypt. Inform the user.

        Args:
            room: The room that the event that we were unable to decrypt is in.

            event: The encrypted event that we were unable to decrypt.
        """
        # Ignore events from unauthorized room
        if room.room_id not in self.config.allowed_rooms:
            return

        logger.error(
            f"Bot {self.matrix_client.user_id} | Room ID {room.room_id} | "
            f"Event ID {event.event_id} | Sender {event.sender} | "
            f"Failed to decrypt event!"
            f"\n\n"
            f"Tip: try using a different device ID in your config file and restart."
            f"\n\n"
            f"If all else fails, delete your store directory and let the bot recreate "
            f"it (your reminders will NOT be deleted, but the bot may respond to existing "
            f"commands a second time)."
        )

    async def key_verification_start(self, event: KeyVerificationStart):
        """Callback for when somebody wants to verify our devices."""
        if "emoji" not in event.short_authentication_string:
            logger.error(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot use emoji verification with device {event.from_device}."
            )
            return

        event_response = await self.matrix_client.accept_key_verification(
            event.transaction_id
        )
        if isinstance(event_response, ToDeviceError):
            logger.error(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot start key verification with device {event.from_device}, got error: {event_response}."
            )
            return

        sas = self.matrix_client.key_verifications[event.transaction_id]

        todevice_msg = sas.share_key()
        event_response = await self.matrix_client.to_device(todevice_msg)
        if isinstance(event_response, ToDeviceError):
            logger.error(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot share key with device {event.from_device}, got error: {event_response}."
            )
            return

    async def key_verification_cancel(self, event: KeyVerificationCancel):
        # There is no need to issue a
        # client.cancel_key_verification(tx_id, reject=False)
        # here. The SAS flow is already cancelled.
        # We only need to inform the user.
        logger.info(
            f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
            f"Key verification has been cancelled for reason: {event.reason}."
        )

    async def key_verification_confirm(self, event: KeyVerificationKey):
        sas = self.matrix_client.key_verifications[event.transaction_id]
        emoji_list, alt_text_list = zip(*sas.get_emoji())
        emoji_str = " ".join(emoji_list)
        alt_text_str = " ".join(alt_text_list)

        logger.info(
            f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
            f"Received request to verify emojis: {emoji_str} ({alt_text_str})"
        )

        event_response = await self.matrix_client.confirm_short_auth_string(
            event.transaction_id
        )
        if isinstance(event_response, ToDeviceError):
            logger.error(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot confirm emoji verification, got error: {event_response}."
            )

        # FIXME: We should allow manual cancel or reject
        # event_response = await self.matrix_client.cancel_key_verification(
        #     event.transaction_id, reject=True
        # )
        # if isinstance(event_response, ToDeviceError):
        #     logger.error(
        #         f"Unable to reject emoji verification with {event.sender}, got error: {event_response}."
        #     )
        #
        # event_response = await self.matrix_client.cancel_key_verification(
        #     event.transaction_id, reject=False
        # )
        # if isinstance(event_response, ToDeviceError):
        #     logger.error(
        #         f"Unable to cancel emoji verification with {event.sender}, got error: {event_response}."
        #     )

    async def key_verification_end(self, event: KeyVerificationMac) -> None:
        try:
            sas = self.matrix_client.key_verifications[event.transaction_id]
        except KeyError:
            logger.error(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot find transaction ID {event.transaction_id}"
            )
            return

        try:
            todevice_msg = sas.get_mac()
        except LocalProtocolError as e:
            # e.g. it might have been cancelled by ourselves
            logger.warning(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot conclude key verification: {e}."
            )
            return

        event_response = await self.matrix_client.to_device(todevice_msg)
        if isinstance(event_response, ToDeviceError):
            logger.error(
                f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
                f"Cannot conclude key verification, got error: {event_response}."
            )
            return

        verified_devices = " ".join(sas.verified_devices)
        logger.info(
            f"Bot {self.matrix_client.user_id} | Sender {event.sender} | "
            f"Successfully verified devices: {verified_devices}"
        )

    async def unknown_message(
        self, room: MatrixRoom, event: RoomMessageUnknown
    ) -> None:
        event_content = event.source["content"]
        if event_content["msgtype"] != "m.key.verification.request":
            return

        if "m.sas.v1" not in event_content["methods"]:
            return

        response_event = await self.matrix_client.room_send(
            room.room_id,
            "m.room.message",
            {
                "msgtype": "m.key.verification.ready",
                "methods": ["m.sas.v1"],
                "m.relates_to": {"rel_type": "m.reference", "event_id": event.event_id},
            },
        )

        if isinstance(response_event, RoomSendError):
            raise SendRetryError(
                f"{response_event.status_code} - {response_event.message}"
            )
