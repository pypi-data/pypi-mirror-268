from __future__ import annotations

import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, call, patch

import nio
import nio.crypto
from diskcache import Cache

import matrix_alertbot.alertmanager
import matrix_alertbot.callback
import matrix_alertbot.command
import matrix_alertbot.matrix


class CallbacksTestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        # Create a Callbacks object and give it some Mock'd objects to use
        self.fake_matrix_client = Mock(spec=nio.AsyncClient)
        self.fake_matrix_client.user_id = "@fake_user:example.com"
        # self.fake_matrix_client.user = "@fake_user"

        self.fake_cache = MagicMock(spec=Cache)
        self.fake_alertmanager_client = Mock(
            spec=matrix_alertbot.alertmanager.AlertmanagerClient
        )

        # Create a fake room to play with
        self.fake_room = Mock(spec=nio.MatrixRoom)
        self.fake_room.room_id = "!abcdefg:example.com"
        self.fake_room.display_name = "Fake Room"

        # We don't spec config, as it doesn't currently have well defined attributes
        self.fake_config = Mock()
        self.fake_config.allowed_rooms = [self.fake_room.room_id]
        self.fake_config.allowed_reactions = ["🤫", "🤗"]
        self.fake_config.insult_reactions = ["🤗"]
        self.fake_config.user_ids = [self.fake_matrix_client.user_id]

        self.fake_matrix_client_pool = Mock(
            spec=matrix_alertbot.matrix.MatrixClientPool
        )
        self.fake_matrix_client_pool.matrix_client = self.fake_matrix_client

        self.callbacks = matrix_alertbot.callback.Callbacks(
            self.fake_matrix_client,
            self.fake_alertmanager_client,
            self.fake_cache,
            self.fake_config,
            self.fake_matrix_client_pool,
        )

    async def test_invite(self) -> None:
        """Tests the callback for InviteMemberEvents"""
        # Tests that the bot attempts to join a room after being invited to it
        fake_invite_event = Mock(spec=nio.InviteMemberEvent)
        fake_invite_event.sender = "@some_other_fake_user:example.com"

        # Pretend that we received an invite event
        await self.callbacks.invite(self.fake_room, fake_invite_event)

        # Check that we attempted to join the room
        self.fake_matrix_client.join.assert_called_once_with(self.fake_room.room_id)

    async def test_invite_in_unauthorized_room(self) -> None:
        """Tests the callback for InviteMemberEvents"""
        # Tests that the bot attempts to join a room after being invited to it
        fake_invite_event = Mock(spec=nio.InviteMemberEvent)
        fake_invite_event.sender = "@some_other_fake_user:example.com"

        self.fake_room.room_id = "!unauthorizedroom@example.com"

        # Pretend that we received an invite event
        await self.callbacks.invite(self.fake_room, fake_invite_event)

        # Check that we attempted to join the room
        self.fake_matrix_client.join.assert_not_called()

    async def test_invite_raise_join_error(self) -> None:
        """Tests the callback for InviteMemberEvents"""
        # Tests that the bot attempts to join a room after being invited to it
        fake_invite_event = Mock(spec=nio.InviteMemberEvent)
        fake_invite_event.sender = "@some_other_fake_user:example.com"

        fake_join_error = Mock(spec=nio.JoinError)
        fake_join_error.message = "error message"
        self.fake_matrix_client.join.return_value = fake_join_error

        # Pretend that we received an invite event
        await self.callbacks.invite(self.fake_room, fake_invite_event)

        # Check that we attempted to join the room
        self.fake_matrix_client.join.assert_has_calls(
            [
                call("!abcdefg:example.com"),
                call("!abcdefg:example.com"),
                call("!abcdefg:example.com"),
            ]
        )

    @patch.object(matrix_alertbot.callback.CommandFactory, "create", autospec=True)
    async def test_message_without_mention(self, fake_command_create: Mock) -> None:
        """Tests the callback for RoomMessageText without any mention of the bot"""
        # Tests that the bot process messages in the room
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "Hello world!"
        fake_message_event.event_id = "some event id"

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command_create.assert_not_called()

    @patch.object(matrix_alertbot.command, "HelpCommand", autospec=True)
    async def test_message_help_client_not_in_pool(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText without any mention of the bot"""
        # Tests that the bot process messages in the room
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user help"
        fake_message_event.source = {"content": {}}

        self.fake_matrix_client_pool.matrix_client = None

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_not_called()

    @patch.object(matrix_alertbot.command, "HelpCommand", autospec=True)
    async def test_message_help_not_in_reply_with_mention(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user help"
        fake_message_event.source = {"content": {}}

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_called_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_message_event.sender,
            fake_message_event.event_id,
            (),
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.command, "HelpCommand", autospec=True)
    async def test_message_help_in_reply_with_mention(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command

        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user help"
        fake_message_event.source = {
            "content": {
                "m.relates_to": {"m.in_reply_to": {"event_id": "some alert event id"}}
            }
        }

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that we attempted to execute the command
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_message_event.sender,
            fake_message_event.event_id,
            (),
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.command.CommandFactory, "create", autospec=True)
    async def test_ignore_message_sent_by_bot(self, fake_create_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command

        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.sender = self.fake_matrix_client.user_id

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that we attempted to execute the command
        fake_create_command.assert_not_called()

    @patch.object(matrix_alertbot.command.CommandFactory, "create", autospec=True)
    async def test_ignore_message_sent_on_unauthorized_room(
        self, fake_create_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command

        self.fake_room.room_id = "!unauthorizedroom@example.com"

        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.sender = "@some_other_fake_user:example.com"

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that we attempted to execute the command
        fake_create_command.assert_not_called()

    @patch.object(matrix_alertbot.command, "AckAlertCommand", autospec=True)
    async def test_message_ack_not_in_reply_with_mention(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user ack"
        fake_message_event.source = {"content": {}}

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_not_called()

    @patch.object(matrix_alertbot.command, "AckAlertCommand", autospec=True)
    async def test_message_ack_in_reply_with_full_mention(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user:example.com ack"
        fake_message_event.source = {
            "content": {
                "m.relates_to": {"m.in_reply_to": {"event_id": "some alert event id"}}
            }
        }

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_message_event.sender,
            fake_message_event.event_id,
            "some alert event id",
            (),
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.command, "AckAlertCommand", autospec=True)
    async def test_message_ack_in_reply_with_short_mention(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "fake_user ack"
        fake_message_event.source = {
            "content": {
                "m.relates_to": {"m.in_reply_to": {"event_id": "some alert event id"}}
            }
        }

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_message_event.sender,
            fake_message_event.event_id,
            "some alert event id",
            (),
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.callback, "UnackAlertCommand", autospec=True)
    async def test_message_unack_not_in_reply_with_mention(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user unack"
        fake_message_event.source = {"content": {}}

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_not_called()

    @patch.object(matrix_alertbot.command, "UnackAlertCommand", autospec=True)
    async def test_message_unack_in_reply_with_mention(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user unack"
        fake_message_event.source = {
            "content": {
                "m.relates_to": {"m.in_reply_to": {"event_id": "some alert event id"}}
            }
        }

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_message_event.sender,
            fake_message_event.event_id,
            "some alert event id",
            (),
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.callback, "logger", autospec=True)
    @patch.object(matrix_alertbot.command, "AckAlertCommand", autospec=True)
    async def test_message_raise_exception(
        self, fake_command: Mock, fake_logger
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_message_event = Mock(spec=nio.RoomMessageText)
        fake_message_event.event_id = "some event id"
        fake_message_event.sender = "@some_other_fake_user:example.com"
        fake_message_event.body = "@fake_user ack"
        fake_message_event.source = {
            "content": {
                "m.relates_to": {"m.in_reply_to": {"event_id": "some alert event id"}}
            }
        }

        fake_command.return_value.process.side_effect = (
            nio.exceptions.LocalProtocolError
        )

        # Pretend that we received a text message event
        await self.callbacks.message(self.fake_room, fake_message_event)

        # Check that the command was not executed
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_message_event.sender,
            fake_message_event.event_id,
            "some alert event id",
            (),
        )
        fake_command.return_value.process.assert_called_once()

        fake_logger.exception.assert_called_once()

    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_reaction_client_not_in_pool(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event = Mock(spec=nio.RoomMessageText)
        fake_alert_event.event_id = "some alert event id"
        fake_alert_event.sender = self.fake_matrix_client.user_id

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event.event_id
        fake_reaction_event.key = "🤫"

        fake_event_response = Mock(spec=nio.RoomGetEventResponse)
        fake_event_response.event = fake_alert_event
        self.fake_matrix_client.room_get_event.return_value = fake_event_response

        self.fake_matrix_client_pool.matrix_client = None

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()

    @patch.object(matrix_alertbot.callback, "AngryUserCommand", autospec=True)
    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_reaction_to_existing_alert(
        self, fake_command: Mock, fake_angry_user_command
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event = Mock(spec=nio.RoomMessageText)
        fake_alert_event.event_id = "some alert event id"
        fake_alert_event.sender = self.fake_matrix_client.user_id

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event.event_id
        fake_reaction_event.key = "🤫"

        fake_event_response = Mock(spec=nio.RoomGetEventResponse)
        fake_event_response.event = fake_alert_event
        self.fake_matrix_client.room_get_event.return_value = fake_event_response

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_reaction_event.sender,
            fake_reaction_event.event_id,
            "some alert event id",
        )
        fake_command.return_value.process.assert_called_once()
        self.fake_matrix_client.room_get_event.assert_called_once_with(
            self.fake_room.room_id, fake_alert_event.event_id
        )

        fake_angry_user_command.assert_not_called()

    @patch.object(matrix_alertbot.callback, "AngryUserCommand", autospec=True)
    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_insult_reaction(
        self, fake_command: Mock, fake_angry_user_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event = Mock(spec=nio.RoomMessageText)
        fake_alert_event.event_id = "some alert event id"
        fake_alert_event.sender = self.fake_matrix_client.user_id

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event.event_id
        fake_reaction_event.key = "🤗"

        fake_event_response = Mock(spec=nio.RoomGetEventResponse)
        fake_event_response.event = fake_alert_event
        self.fake_matrix_client.room_get_event.return_value = fake_event_response

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_reaction_event.sender,
            fake_reaction_event.event_id,
            "some alert event id",
        )
        fake_command.return_value.process.assert_called_once()
        self.fake_matrix_client.room_get_event.assert_called_once_with(
            self.fake_room.room_id, fake_alert_event.event_id
        )

        fake_angry_user_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_reaction_event.sender,
            fake_reaction_event.event_id,
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_reaction_to_inexistent_event(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event_id = "some alert event id"

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.type = "m.reaction"
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event_id
        fake_reaction_event.key = "🤫"

        fake_event_response = Mock(spec=nio.RoomGetEventError)
        self.fake_matrix_client.room_get_event.return_value = fake_event_response

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_cache.set.assert_not_called()
        self.fake_matrix_client.room_get_event.assert_called_once_with(
            self.fake_room.room_id, fake_alert_event_id
        )

    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_reaction_to_event_not_from_bot_user(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event = Mock(spec=nio.RoomMessageText)
        fake_alert_event.event_id = "some alert event id"
        fake_alert_event.sender = "@some_other_fake_user.example.com"

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.type = "m.reaction"
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event.event_id
        fake_reaction_event.key = "🤫"

        fake_event_response = Mock(spec=nio.RoomGetEventResponse)
        fake_event_response.event = fake_alert_event
        self.fake_matrix_client.room_get_event.return_value = fake_event_response

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_cache.set.assert_not_called()
        self.fake_matrix_client.room_get_event.assert_called_once_with(
            self.fake_room.room_id, fake_alert_event.event_id
        )

    @patch.object(matrix_alertbot.callback, "logger", autospec=True)
    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_reaction_raise_exception(
        self, fake_command: Mock, fake_logger: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event = Mock(spec=nio.RoomMessageText)
        fake_alert_event.event_id = "some alert event id"
        fake_alert_event.sender = self.fake_matrix_client.user_id

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event.event_id
        fake_reaction_event.key = "🤫"

        fake_event_response = Mock(spec=nio.RoomGetEventResponse)
        fake_event_response.event = fake_alert_event
        self.fake_matrix_client.room_get_event.return_value = fake_event_response

        fake_command.return_value.process.side_effect = (
            nio.exceptions.LocalProtocolError
        )

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_reaction_event.sender,
            fake_reaction_event.event_id,
            "some alert event id",
        )
        fake_command.return_value.process.assert_called_once()
        self.fake_matrix_client.room_get_event.assert_called_once_with(
            self.fake_room.room_id, fake_alert_event.event_id
        )

        fake_logger.exception.assert_called_once()

    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_reaction_unknown(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event_id = "some alert event id"

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.type = "m.reaction"
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event_id
        fake_reaction_event.key = "unknown"

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_matrix_client.room_get_event.assert_not_called()

    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_ignore_reaction_sent_by_bot_user(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event_id = "some alert event id"

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.type = "m.reaction"
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = self.fake_matrix_client.user_id
        fake_reaction_event.reacts_to = fake_alert_event_id
        fake_reaction_event.key = "unknown"

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_matrix_client.room_get_event.assert_not_called()

    @patch.object(matrix_alertbot.callback, "AckAlertCommand", autospec=True)
    async def test_ignore_reaction_in_unauthorized_room(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        self.fake_room.room_id = "!unauthorizedroom@example.com"

        fake_alert_event_id = "some alert event id"

        fake_reaction_event = Mock(spec=nio.ReactionEvent)
        fake_reaction_event.type = "m.reaction"
        fake_reaction_event.event_id = "some event id"
        fake_reaction_event.sender = "@some_other_fake_user:example.com"
        fake_reaction_event.reacts_to = fake_alert_event_id
        fake_reaction_event.key = "unknown"

        # Pretend that we received a text message event
        await self.callbacks.reaction(self.fake_room, fake_reaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_matrix_client.room_get_event.assert_not_called()

    @patch.object(matrix_alertbot.callback, "UnackAlertCommand", autospec=True)
    async def test_redaction_client_not_in_pool(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event_id = "some alert event id"

        fake_redaction_event = Mock(spec=nio.RedactionEvent)
        fake_redaction_event.redacts = "some other event id"
        fake_redaction_event.event_id = "some event id"
        fake_redaction_event.sender = "@some_other_fake_user:example.com"

        fake_cache_dict = {fake_redaction_event.redacts: fake_alert_event_id}
        self.fake_cache.__getitem__.side_effect = fake_cache_dict.__getitem__

        self.fake_matrix_client_pool.matrix_client = None

        # Pretend that we received a text message event
        await self.callbacks.redaction(self.fake_room, fake_redaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()

    @patch.object(matrix_alertbot.callback, "UnackAlertCommand", autospec=True)
    async def test_redaction(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event_id = "some alert event id"

        fake_redaction_event = Mock(spec=nio.RedactionEvent)
        fake_redaction_event.redacts = "some other event id"
        fake_redaction_event.event_id = "some event id"
        fake_redaction_event.sender = "@some_other_fake_user:example.com"

        fake_cache_dict = {fake_redaction_event.redacts: fake_alert_event_id}
        self.fake_cache.__getitem__.side_effect = fake_cache_dict.__getitem__

        # Pretend that we received a text message event
        await self.callbacks.redaction(self.fake_room, fake_redaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_redaction_event.sender,
            fake_redaction_event.event_id,
            fake_redaction_event.redacts,
        )
        fake_command.return_value.process.assert_called_once()

    @patch.object(matrix_alertbot.callback, "logger", autospec=True)
    @patch.object(matrix_alertbot.callback, "UnackAlertCommand", autospec=True)
    async def test_redaction_raise_exception(
        self, fake_command: Mock, fake_logger
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_alert_event_id = "some alert event id"

        fake_redaction_event = Mock(spec=nio.RedactionEvent)
        fake_redaction_event.redacts = "some other event id"
        fake_redaction_event.event_id = "some event id"
        fake_redaction_event.sender = "@some_other_fake_user:example.com"

        fake_cache_dict = {fake_redaction_event.redacts: fake_alert_event_id}
        self.fake_cache.__getitem__.side_effect = fake_cache_dict.__getitem__

        fake_command.return_value.process.side_effect = (
            nio.exceptions.LocalProtocolError
        )

        # Pretend that we received a text message event
        await self.callbacks.redaction(self.fake_room, fake_redaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_called_once_with(
            self.fake_matrix_client,
            self.fake_cache,
            self.fake_alertmanager_client,
            self.fake_config,
            self.fake_room,
            fake_redaction_event.sender,
            fake_redaction_event.event_id,
            fake_redaction_event.redacts,
        )
        fake_command.return_value.process.assert_called_once()

        fake_logger.exception.assert_called_once()

    @patch.object(matrix_alertbot.callback, "UnackAlertCommand", autospec=True)
    async def test_ignore_redaction_sent_by_bot_user(self, fake_command: Mock) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_redaction_event = Mock(spec=nio.RedactionEvent)
        fake_redaction_event.sender = self.fake_matrix_client.user_id

        fake_cache_dict: Dict = {}
        self.fake_cache.__getitem__.side_effect = fake_cache_dict.__getitem__

        # Pretend that we received a text message event
        await self.callbacks.redaction(self.fake_room, fake_redaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_cache.__getitem__.assert_not_called()

    @patch.object(matrix_alertbot.callback, "UnackAlertCommand", autospec=True)
    async def test_ignore_redaction_in_unauthorized_room(
        self, fake_command: Mock
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        self.fake_room.room_id = "!unauthorizedroom@example.com"

        fake_redaction_event = Mock(spec=nio.RedactionEvent)
        fake_redaction_event.sender = "@some_other_fake_user:example.com"

        fake_cache_dict: Dict = {}
        self.fake_cache.__getitem__.side_effect = fake_cache_dict.__getitem__

        # Pretend that we received a text message event
        await self.callbacks.redaction(self.fake_room, fake_redaction_event)

        # Check that we attempted to execute the command
        fake_command.assert_not_called()
        self.fake_cache.__getitem__.assert_not_called()

    async def test_key_verification_start(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.from_device = "ABCDEFGH"
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.short_authentication_string = ["emoji"]
        fake_key_verification_event.transaction_id = fake_transaction_id

        fake_sas = Mock()
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_start(fake_key_verification_event)

        # Check that we attempted to execute the command
        self.fake_matrix_client.accept_key_verification.assert_called_once_with(
            fake_transaction_id
        )
        self.fake_matrix_client.to_device.assert_called_once_with(fake_sas.share_key())

    async def test_key_verification_start_with_emoji_not_supported(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.from_device = "ABCDEFGH"
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.short_authentication_string = []
        fake_key_verification_event.transaction_id = fake_transaction_id

        fake_sas = Mock()
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_start(fake_key_verification_event)

        # Check that we attempted to execute the command
        self.fake_matrix_client.accept_key_verification.assert_not_called()
        self.fake_matrix_client.to_device.assert_not_called()

    async def test_key_verification_start_with_accept_key_verification_error(
        self,
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.from_device = "ABCDEFGH"
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.short_authentication_string = ["emoji"]
        fake_key_verification_event.transaction_id = fake_transaction_id

        self.fake_matrix_client.accept_key_verification.return_value = Mock(
            spec=nio.ToDeviceError
        )

        fake_sas = Mock()
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_start(fake_key_verification_event)

        # Check that we attempted to execute the command
        self.fake_matrix_client.accept_key_verification.assert_called_once_with(
            fake_transaction_id
        )
        self.fake_matrix_client.to_device.assert_not_called()

    async def test_key_verification_start_with_to_device_error(
        self,
    ) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.from_device = "ABCDEFGH"
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.short_authentication_string = ["emoji"]
        fake_key_verification_event.transaction_id = fake_transaction_id

        self.fake_matrix_client.to_device.return_value = Mock(spec=nio.ToDeviceError)

        fake_sas = Mock()
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_start(fake_key_verification_event)

        # Check that we attempted to execute the command
        self.fake_matrix_client.accept_key_verification.assert_called_once_with(
            fake_transaction_id
        )
        self.fake_matrix_client.to_device.assert_called_once_with(fake_sas.share_key())

    async def test_key_verification_cancel(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_key_verification_event = Mock(spec=nio.KeyVerificationCancel)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.reason = "fake reason"

        # Pretend that we received a text message event
        await self.callbacks.key_verification_cancel(fake_key_verification_event)

        # Check that we attempted to execute the command

    async def test_key_verification_confirm(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.transaction_id = fake_transaction_id

        fake_sas = Mock()
        fake_sas.get_emoji.return_value = [
            ("emoji1", "alt text1"),
            ("emoji2", "alt text2"),
        ]
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_confirm(fake_key_verification_event)

        # Check that we attempted to execute the command
        self.fake_matrix_client.confirm_short_auth_string.assert_called_once_with(
            fake_transaction_id
        )

    async def test_key_verification_confirm_with_error(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.transaction_id = fake_transaction_id

        self.fake_matrix_client.confirm_short_auth_string.return_value = Mock(
            spec=nio.ToDeviceError
        )

        fake_sas = Mock()
        fake_sas.get_emoji.return_value = [
            ("emoji1", "alt text1"),
            ("emoji2", "alt text2"),
        ]
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_confirm(fake_key_verification_event)

        # Check that we attempted to execute the command
        self.fake_matrix_client.confirm_short_auth_string.assert_called_once_with(
            fake_transaction_id
        )

    async def test_key_verification_end(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.transaction_id = fake_transaction_id

        fake_sas = Mock()
        fake_sas.verified_devices = ["HGFEDCBA"]
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_end(fake_key_verification_event)

        # Check that we attempted to execute the command
        fake_sas.get_mac.assert_called_once_with()
        self.fake_matrix_client.to_device.assert_called_once_with(fake_sas.get_mac())

    async def test_key_verification_end_with_missing_transaction_id(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.transaction_id = fake_transaction_id

        fake_sas = Mock()
        fake_transactions_dict = {}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_end(fake_key_verification_event)

        # Check that we attempted to execute the command
        fake_sas.get_mac.assert_not_called()
        self.fake_matrix_client.to_device.assert_not_called()

    async def test_key_verification_end_with_mac_error(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.transaction_id = fake_transaction_id

        fake_sas = Mock()
        fake_sas.get_mac.side_effect = nio.exceptions.LocalProtocolError
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_end(fake_key_verification_event)

        # Check that we attempted to execute the command
        fake_sas.get_mac.assert_called_once_with()
        self.fake_matrix_client.to_device.assert_not_called()

    async def test_key_verification_end_with_to_device_error(self) -> None:
        """Tests the callback for RoomMessageText with a mention of the bot"""
        # Tests that the bot process messages in the room that contain a command
        fake_transaction_id = "fake transaction id"

        fake_key_verification_event = Mock(spec=nio.KeyVerificationStart)
        fake_key_verification_event.sender = "@some_other_fake_user:example.com"
        fake_key_verification_event.transaction_id = fake_transaction_id

        self.fake_matrix_client.to_device.return_value = Mock(spec=nio.ToDeviceError)

        fake_sas = Mock()
        fake_transactions_dict = {fake_transaction_id: fake_sas}
        self.fake_matrix_client.key_verifications = fake_transactions_dict

        # Pretend that we received a text message event
        await self.callbacks.key_verification_end(fake_key_verification_event)

        # Check that we attempted to execute the command
        fake_sas.get_mac.assert_called_once_with()
        self.fake_matrix_client.to_device.assert_called_once_with(fake_sas.get_mac())

    @patch.object(matrix_alertbot.callback, "logger", autospec=True)
    async def test_decryption_failure(self, fake_logger) -> None:
        fake_megolm_event = Mock(spec=nio.MegolmEvent)
        fake_megolm_event.sender = "@some_other_fake_user:example.com"
        fake_megolm_event.event_id = "some event id"

        await self.callbacks.decryption_failure(self.fake_room, fake_megolm_event)

        fake_logger.error.assert_called_once()

    @patch.object(matrix_alertbot.callback, "logger", autospec=True)
    async def test_decryption_failure_in_unauthorized_room(self, fake_logger) -> None:
        fake_megolm_event = Mock(spec=nio.MegolmEvent)
        fake_megolm_event.sender = "@some_other_fake_user:example.com"
        fake_megolm_event.event_id = "some event id"

        self.fake_room.room_id = "!unauthorizedroom@example.com"

        await self.callbacks.decryption_failure(self.fake_room, fake_megolm_event)

        fake_logger.error.assert_not_called()

    async def test_unknown_message(self) -> None:
        fake_room_unknown_event = Mock(spec=nio.RoomMessageUnknown)
        fake_room_unknown_event.source = {
            "content": {
                "msgtype": "m.key.verification.request",
                "methods": ["m.sas.v1"],
            }
        }
        fake_room_unknown_event.event_id = "some event id"

        await self.callbacks.unknown_message(self.fake_room, fake_room_unknown_event)

        self.fake_matrix_client.room_send.assert_called_once_with(
            self.fake_room.room_id,
            "m.room.message",
            {
                "msgtype": "m.key.verification.ready",
                "methods": ["m.sas.v1"],
                "m.relates_to": {
                    "rel_type": "m.reference",
                    "event_id": fake_room_unknown_event.event_id,
                },
            },
        )

    async def test_unknown_message_with_msgtype_not_verification_request(self) -> None:
        fake_room_unknown_event = Mock(spec=nio.RoomMessageUnknown)
        fake_room_unknown_event.source = {
            "content": {
                "msgtype": "unknown",
                "methods": ["m.sas.v1"],
            }
        }
        fake_room_unknown_event.event_id = "some event id"

        await self.callbacks.unknown_message(self.fake_room, fake_room_unknown_event)

        self.fake_matrix_client.room_send.assert_not_called()

    async def test_unknown_message_with_method_not_sas_v1(self) -> None:
        fake_room_unknown_event = Mock(spec=nio.RoomMessageUnknown)
        fake_room_unknown_event.source = {
            "content": {
                "msgtype": "m.key.verification.request",
                "methods": [],
            }
        }
        fake_room_unknown_event.event_id = "some event id"

        await self.callbacks.unknown_message(self.fake_room, fake_room_unknown_event)

        self.fake_matrix_client.room_send.assert_not_called()


if __name__ == "__main__":
    unittest.main()
