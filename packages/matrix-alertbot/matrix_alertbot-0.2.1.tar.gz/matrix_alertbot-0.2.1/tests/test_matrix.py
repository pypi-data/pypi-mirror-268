from __future__ import annotations

import random
import unittest
from unittest.mock import Mock, call, patch

import nio
from diskcache import Cache

import matrix_alertbot
import matrix_alertbot.matrix
from matrix_alertbot.alertmanager import AlertmanagerClient
from matrix_alertbot.config import AccountConfig, Config
from matrix_alertbot.matrix import MatrixClientPool


def mock_create_matrix_client(
    matrix_client_pool: MatrixClientPool,
    account: AccountConfig,
    alertmanager_client: AlertmanagerClient,
    cache: Cache,
    config: Config,
) -> nio.AsyncClient:
    fake_matrix_client = Mock(spec=nio.AsyncClient)
    fake_matrix_client.logged_in = True
    return fake_matrix_client


class FakeAsyncClientConfig:
    def __init__(
        self,
        max_limit_exceeded: int,
        max_timeouts: int,
        store_sync_tokens: bool,
        encryption_enabled: bool,
    ) -> None:
        if encryption_enabled:
            raise ImportWarning()

        self.max_limit_exceeded = max_limit_exceeded
        self.max_timeouts = max_timeouts
        self.store_sync_tokens = store_sync_tokens
        self.encryption_enabled = encryption_enabled


class MatrixClientPoolTestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        random.seed(42)

        self.fake_alertmanager_client = Mock(spec=AlertmanagerClient)
        self.fake_cache = Mock(spec=Cache)

        self.fake_account_config_1 = Mock(spec=AccountConfig)
        self.fake_account_config_1.id = "@fake_user:matrix.example.com"
        self.fake_account_config_1.homeserver_url = "https://matrix.example.com"
        self.fake_account_config_1.device_id = "ABCDEFGH"
        self.fake_account_config_1.token_file = "account1.token.secret"
        self.fake_account_config_2 = Mock(spec=AccountConfig)
        self.fake_account_config_2.id = "@other_user:chat.example.com"
        self.fake_account_config_2.homeserver_url = "https://chat.example.com"
        self.fake_account_config_2.device_id = "IJKLMNOP"
        self.fake_account_config_2.token_file = "account2.token.secret"
        self.fake_config = Mock(spec=Config)
        self.fake_config.store_dir = "/dev/null"
        self.fake_config.accounts = [
            self.fake_account_config_1,
            self.fake_account_config_2,
        ]

    @patch.object(
        matrix_alertbot.matrix.MatrixClientPool, "_create_matrix_client", autospec=True
    )
    async def test_init_matrix_client_pool(self, fake_create_matrix_client) -> None:
        fake_matrix_client = Mock(spec=nio.AsyncClient)
        fake_create_matrix_client.return_value = fake_matrix_client

        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        fake_create_matrix_client.assert_has_calls(
            [
                call(
                    matrix_client_pool,
                    self.fake_account_config_1,
                    self.fake_alertmanager_client,
                    self.fake_cache,
                    self.fake_config,
                ),
                call(
                    matrix_client_pool,
                    self.fake_account_config_2,
                    self.fake_alertmanager_client,
                    self.fake_cache,
                    self.fake_config,
                ),
            ]
        )

        self.assertEqual(self.fake_account_config_1, matrix_client_pool.account)
        self.assertEqual(fake_matrix_client, matrix_client_pool.matrix_client)
        self.assertEqual(2, len(matrix_client_pool._accounts))
        self.assertEqual(2, len(matrix_client_pool._matrix_clients))

    @patch.object(
        matrix_alertbot.matrix.MatrixClientPool, "_create_matrix_client", autospec=True
    )
    async def test_close_matrix_client_pool(self, fake_create_matrix_client) -> None:
        fake_matrix_client = Mock(spec=nio.AsyncClient)
        fake_create_matrix_client.return_value = fake_matrix_client

        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )
        await matrix_client_pool.close()

        fake_matrix_client.close.assert_has_calls([(call(), call())])

    @patch.object(
        matrix_alertbot.matrix.MatrixClientPool,
        "_create_matrix_client",
        autospec=True,
        side_effect=mock_create_matrix_client,
    )
    async def test_switch_active_client(self, fake_create_matrix_client) -> None:
        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        fake_matrix_client_1 = matrix_client_pool.matrix_client
        await matrix_client_pool.switch_active_client()
        fake_matrix_client_2 = matrix_client_pool.matrix_client

        self.assertEqual(self.fake_account_config_2, matrix_client_pool.account)
        self.assertNotEqual(fake_matrix_client_2, fake_matrix_client_1)

        await matrix_client_pool.switch_active_client()
        fake_matrix_client_3 = matrix_client_pool.matrix_client

        self.assertEqual(self.fake_account_config_1, matrix_client_pool.account)
        self.assertEqual(fake_matrix_client_3, fake_matrix_client_1)

    @patch.object(
        matrix_alertbot.matrix.MatrixClientPool,
        "_create_matrix_client",
        autospec=True,
        side_effect=mock_create_matrix_client,
    )
    async def test_switch_active_client_with_whoami_raise_exception(
        self, fake_create_matrix_client
    ) -> None:
        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        for fake_matrix_client in matrix_client_pool._matrix_clients.values():
            fake_matrix_client.whoami.side_effect = Exception

        fake_matrix_client_1 = matrix_client_pool.matrix_client
        await matrix_client_pool.switch_active_client()
        fake_matrix_client_2 = matrix_client_pool.matrix_client

        self.assertEqual(self.fake_account_config_1, matrix_client_pool.account)
        self.assertEqual(fake_matrix_client_2, fake_matrix_client_1)

    @patch.object(
        matrix_alertbot.matrix.MatrixClientPool,
        "_create_matrix_client",
        autospec=True,
        side_effect=mock_create_matrix_client,
    )
    async def test_switch_active_client_with_whoami_error(
        self, fake_create_matrix_client
    ) -> None:
        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        for fake_matrix_client in matrix_client_pool._matrix_clients.values():
            fake_matrix_client.whoami.return_value = Mock(
                spec=nio.responses.WhoamiError
            )

        fake_matrix_client_1 = matrix_client_pool.matrix_client
        await matrix_client_pool.switch_active_client()
        fake_matrix_client_2 = matrix_client_pool.matrix_client

        self.assertEqual(self.fake_account_config_1, matrix_client_pool.account)
        self.assertEqual(fake_matrix_client_2, fake_matrix_client_1)

    @patch.object(
        matrix_alertbot.matrix.MatrixClientPool,
        "_create_matrix_client",
        autospec=True,
        side_effect=mock_create_matrix_client,
    )
    async def test_switch_active_client_with_whoami_error_and_not_logged_in(
        self, fake_create_matrix_client
    ) -> None:
        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        for fake_matrix_client in matrix_client_pool._matrix_clients.values():
            fake_matrix_client.whoami.return_value = Mock(
                spec=nio.responses.WhoamiError
            )
            fake_matrix_client.logged_in = False

        fake_matrix_client_1 = matrix_client_pool.matrix_client
        await matrix_client_pool.switch_active_client()
        fake_matrix_client_2 = matrix_client_pool.matrix_client

        self.assertEqual(self.fake_account_config_1, matrix_client_pool.account)
        self.assertEqual(fake_matrix_client_2, fake_matrix_client_1)

    @patch.object(
        matrix_alertbot.matrix, "AsyncClientConfig", spec=nio.AsyncClientConfig
    )
    async def test_create_matrix_client(self, fake_async_client_config: Mock) -> None:
        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        matrix_client_1 = matrix_client_pool._matrix_clients[self.fake_account_config_1]
        self.assertEqual(self.fake_account_config_1.id, matrix_client_1.user)
        self.assertEqual(
            self.fake_account_config_1.device_id, matrix_client_1.device_id
        )
        self.assertEqual(
            self.fake_account_config_1.homeserver_url, matrix_client_1.homeserver
        )
        self.assertEqual(self.fake_config.store_dir, matrix_client_1.store_path)
        self.assertEqual(6, len(matrix_client_1.event_callbacks))
        self.assertEqual(4, len(matrix_client_1.to_device_callbacks))

        fake_async_client_config.assert_has_calls(
            [
                call(
                    max_limit_exceeded=5,
                    max_timeouts=3,
                    store_sync_tokens=True,
                    encryption_enabled=True,
                ),
                call(
                    max_limit_exceeded=5,
                    max_timeouts=3,
                    store_sync_tokens=True,
                    encryption_enabled=True,
                ),
            ]
        )

    @patch.object(
        matrix_alertbot.matrix,
        "AsyncClientConfig",
        spec=nio.AsyncClientConfig,
        side_effect=FakeAsyncClientConfig,
    )
    async def test_create_matrix_client_with_encryption_disabled(
        self, fake_async_client_config: Mock
    ) -> None:
        matrix_client_pool = MatrixClientPool(
            alertmanager_client=self.fake_alertmanager_client,
            cache=self.fake_cache,
            config=self.fake_config,
        )

        matrix_client_1 = matrix_client_pool._matrix_clients[self.fake_account_config_1]
        self.assertEqual(self.fake_account_config_1.id, matrix_client_1.user)
        self.assertEqual(
            self.fake_account_config_1.device_id, matrix_client_1.device_id
        )
        self.assertEqual(
            self.fake_account_config_1.homeserver_url, matrix_client_1.homeserver
        )
        self.assertEqual(self.fake_config.store_dir, matrix_client_1.store_path)
        self.assertEqual(6, len(matrix_client_1.event_callbacks))
        self.assertEqual(4, len(matrix_client_1.to_device_callbacks))
        self.assertEqual(5, matrix_client_1.config.max_limit_exceeded)
        self.assertEqual(3, matrix_client_1.config.max_timeouts)
        self.assertTrue(matrix_client_1.config.store_sync_tokens)
        self.assertFalse(matrix_client_1.config.encryption_enabled)


if __name__ == "__main__":
    unittest.main()
