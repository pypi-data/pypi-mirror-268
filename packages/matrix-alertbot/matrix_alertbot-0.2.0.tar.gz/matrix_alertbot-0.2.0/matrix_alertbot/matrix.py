from __future__ import annotations

import asyncio
import json
import logging
import os
import random
from typing import Dict, List, Optional, Tuple

from aiohttp import ClientConnectionError, ServerDisconnectedError
from diskcache import Cache
from nio.client import AsyncClient, AsyncClientConfig
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
from nio.exceptions import LocalProtocolError
from nio.responses import LoginError, WhoamiError

import matrix_alertbot.callback
from matrix_alertbot.alertmanager import AlertmanagerClient
from matrix_alertbot.config import AccountConfig, Config

logger = logging.getLogger(__name__)


class MatrixClientPool:
    def __init__(
        self, alertmanager_client: AlertmanagerClient, cache: Cache, config: Config
    ) -> None:
        self._lock = asyncio.Lock()
        self._matrix_clients: Dict[AccountConfig, AsyncClient] = {}
        self._accounts: List[AccountConfig] = []

        self._accounts = config.accounts
        for account in self._accounts:
            matrix_client = self._create_matrix_client(
                account, alertmanager_client, cache, config
            )
            self._matrix_clients[account] = matrix_client

        self.account = next(iter(self._accounts))
        self.matrix_client = self._matrix_clients[self.account]

    async def switch_active_client(
        self,
    ) -> Optional[Tuple[AsyncClient, AccountConfig]]:
        async with self._lock:
            for account in random.sample(self._accounts, len(self._accounts)):
                if account is self.account:
                    continue

                matrix_client = self._matrix_clients[account]
                try:
                    whoami = await matrix_client.whoami()
                    logged_in = not isinstance(whoami, WhoamiError)
                except Exception:
                    logged_in = False

                if logged_in:
                    self.account = account
                    self.matrix_client = matrix_client

                    logger.warning(
                        f"Bot {self.account.id} | Matrix client for homeserver {self.account.homeserver_url} selected as new leader."
                    )

                    return matrix_client, account

            if self.matrix_client.logged_in:
                logger.warning(
                    f"Bot {self.account.id} | No active Matrix client available, keeping Matrix client for {self.account.homeserver_url} as the leader."
                )
            else:
                logger.error(
                    f"Bot {self.account.id} | No active Matrix client connected."
                )
        return None

    async def close(self) -> None:
        for matrix_client in self._matrix_clients.values():
            await matrix_client.close()

    def _create_matrix_client(
        self,
        account: AccountConfig,
        alertmanager_client: AlertmanagerClient,
        cache: Cache,
        config: Config,
    ) -> AsyncClient:
        # Configuration options for the AsyncClient
        try:
            matrix_client_config = AsyncClientConfig(
                max_limit_exceeded=5,
                max_timeouts=3,
                store_sync_tokens=True,
                encryption_enabled=True,
            )
        except ImportWarning as e:
            logger.warning(e)
            matrix_client_config = AsyncClientConfig(
                max_limit_exceeded=5,
                max_timeouts=3,
                store_sync_tokens=True,
                encryption_enabled=False,
            )

        # Load credentials from a previous session
        if os.path.exists(account.token_file):
            with open(account.token_file, "r") as ifd:
                credentials = json.load(ifd)
                account.token = credentials["access_token"]
                account.device_id = credentials["device_id"]

        # Initialize the matrix client based on stored credentials
        matrix_client = AsyncClient(
            account.homeserver_url,
            account.id,
            device_id=account.device_id,
            store_path=config.store_dir,
            config=matrix_client_config,
        )

        # Set up event callbacks
        callbacks = matrix_alertbot.callback.Callbacks(
            matrix_client, alertmanager_client, cache, config, self
        )

        matrix_client.add_event_callback(callbacks.message, (RoomMessageText,))
        matrix_client.add_event_callback(
            callbacks.invite_event_filtered_callback, (InviteMemberEvent,)
        )
        # matrix_client.add_event_callback(callbacks.debug, (Event,))
        matrix_client.add_event_callback(callbacks.decryption_failure, (MegolmEvent,))
        matrix_client.add_event_callback(callbacks.reaction, (ReactionEvent,))
        matrix_client.add_event_callback(callbacks.redaction, (RedactionEvent,))
        matrix_client.add_event_callback(
            callbacks.unknown_message, (RoomMessageUnknown,)
        )
        matrix_client.add_to_device_callback(
            callbacks.key_verification_start, (KeyVerificationStart,)
        )
        matrix_client.add_to_device_callback(
            callbacks.key_verification_cancel, (KeyVerificationCancel,)
        )
        matrix_client.add_to_device_callback(
            callbacks.key_verification_confirm, (KeyVerificationKey,)
        )
        matrix_client.add_to_device_callback(
            callbacks.key_verification_end, (KeyVerificationMac,)
        )

        return matrix_client

    async def start(
        self,
        account: AccountConfig,
        config: Config,
    ):
        matrix_client = self._matrix_clients[account]

        # Keep trying to reconnect on failure (with some time in-between)
        # We switch homeserver after some retries
        while True:
            try:
                if account.device_id and account.token:
                    matrix_client.restore_login(
                        user_id=account.id,
                        device_id=account.device_id,
                        access_token=account.token,
                    )

                    # Sync encryption keys with the server
                    if matrix_client.should_upload_keys:
                        await matrix_client.keys_upload()
                else:
                    # Try to login with the configured username/password
                    try:
                        login_response = await matrix_client.login(
                            password=account.password,
                            device_name=config.device_name,
                        )

                        # Check if login failed
                        if isinstance(login_response, LoginError):
                            logger.error(
                                f"Bot {account.id} | Failed to login: {login_response.message}"
                            )
                            return False
                    except LocalProtocolError as e:
                        # There's an edge case here where the user hasn't installed the correct C
                        # dependencies. In that case, a LocalProtocolError is raised on login.
                        logger.fatal(
                            f"Bot {account.id} | Failed to login. Have you installed the correct dependencies? "
                            "https://github.com/poljar/matrix-nio#installation "
                            "Error: %s",
                            e,
                        )
                        return False

                    if isinstance(login_response, LoginError):
                        logger.fatal(
                            f"Bot {account.id} | Failed to login: {login_response.message}"
                        )
                        return False

                    # Save user's access token and device ID
                    # See https://stackoverflow.com/a/45368120
                    account_token_fd = os.open(
                        account.token_file,
                        flags=os.O_CREAT | os.O_WRONLY | os.O_TRUNC,
                        mode=0o640,
                    )
                    with os.fdopen(account_token_fd, "w") as ofd:
                        json.dump(
                            {
                                "device_id": login_response.device_id,
                                "access_token": login_response.access_token,
                            },
                            ofd,
                        )

                    # Login succeeded!

                logger.info(f"Bot {account.id} | Logged in.")

                await matrix_client.sync_forever(timeout=30000, full_state=True)
            except (ClientConnectionError, ServerDisconnectedError, TimeoutError):
                await matrix_client.close()

                logger.warning(
                    f"Bot {account.id} | Matrix client disconnected, retrying in 15s..."
                )

                if len(self._accounts) > 1 and self.matrix_client is matrix_client:
                    logger.warning(
                        f"Bot {account.id} | Selecting another Matrix client as leader..."
                    )
                    await self.switch_active_client()

                # Sleep so we don't bombard the server with login requests
                await asyncio.sleep(15)
            finally:
                await matrix_client.close()
