import os
import sys
import unittest
from datetime import timedelta
from unittest.mock import Mock, patch

import yaml

import matrix_alertbot.config
from matrix_alertbot.config import DEFAULT_REACTIONS, Config
from matrix_alertbot.errors import (
    InvalidConfigError,
    ParseConfigError,
    RequiredConfigKeyError,
)

WORKING_DIR = os.path.dirname(__file__)
CONFIG_RESOURCES_DIR = os.path.join(WORKING_DIR, "resources", "config")


class DummyConfig(Config):
    def __init__(self, filepath: str):
        with open(filepath) as file_stream:
            self.config_dict = yaml.safe_load(file_stream.read())


def mock_path_isdir(path: str) -> bool:
    if path == "data/store":
        return False
    return True


def mock_path_exists(path: str) -> bool:
    if path == "data/store":
        return False
    return True


class ConfigTestCase(unittest.TestCase):
    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    @patch.object(matrix_alertbot.config, "logger", autospec=True)
    @patch.object(matrix_alertbot.config, "logging", autospec=True)
    def test_read_minimal_config(
        self,
        fake_logging: Mock,
        fake_logger: Mock,
        fake_mkdir: Mock,
        fake_path_exists: Mock,
        fake_path_isdir: Mock,
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = Config(config_path)

        fake_path_isdir.assert_called_once_with("data/store")
        fake_path_exists.assert_called_once_with("data/store")
        fake_mkdir.assert_called_once_with("data/store")

        fake_logger.setLevel.assert_called_once_with("DEBUG")
        fake_logger.addHandler.assert_called_once()
        fake_logging.StreamHandler.return_value.setLevel.assert_called_once_with("INFO")
        fake_logging.StreamHandler.assert_called_once_with(sys.stdout)

        self.assertEqual({"@fakes_user:matrix.example.com"}, config.user_ids)
        self.assertEqual(1, len(config.accounts))
        self.assertEqual("password", config.accounts[0].password)
        self.assertIsNone(config.accounts[0].token)
        self.assertIsNone(config.accounts[0].device_id)
        self.assertEqual("matrix-alertbot", config.device_name)
        self.assertEqual(
            "https://matrix.example.com", config.accounts[0].homeserver_url
        )
        self.assertEqual(["!abcdefgh:matrix.example.com"], config.allowed_rooms)
        self.assertEqual(DEFAULT_REACTIONS, config.allowed_reactions)

        self.assertEqual("0.0.0.0", config.address)
        self.assertEqual(8080, config.port)
        self.assertIsNone(config.socket)

        self.assertEqual("http://localhost:9093", config.alertmanager_url)

        expected_expire_time = timedelta(days=7).total_seconds()
        self.assertEqual(expected_expire_time, config.cache_expire_time)
        self.assertEqual("data/cache", config.cache_dir)

        self.assertEqual("data/store", config.store_dir)

        self.assertIsNone(config.template_dir)

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    @patch.object(matrix_alertbot.config, "logger", autospec=True)
    @patch.object(matrix_alertbot.config, "logging", autospec=True)
    def test_read_full_config(
        self,
        fake_logging: Mock,
        fake_logger: Mock,
        fake_mkdir: Mock,
        fake_path_exists: Mock,
        fake_path_isdir: Mock,
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.full.yml")
        config = Config(config_path)

        fake_path_isdir.assert_called_once_with("data/store")
        fake_path_exists.assert_called_once_with("data/store")
        fake_mkdir.assert_called_once_with("data/store")

        fake_logger.setLevel.assert_called_once_with("DEBUG")
        fake_logger.addHandler.assert_called_once()
        fake_logging.FileHandler.return_value.setLevel.assert_called_once_with("INFO")
        fake_logging.FileHandler.assert_called_once_with("fake.log")

        self.assertEqual(
            {"@fakes_user:matrix.example.com", "@other_user:matrix.domain.tld"},
            config.user_ids,
        )
        self.assertEqual(2, len(config.accounts))
        self.assertEqual("password", config.accounts[0].password)
        self.assertIsNone(config.accounts[0].token)
        self.assertEqual("fake_token.json", config.accounts[0].token_file)
        self.assertEqual("ABCDEFGHIJ", config.accounts[0].device_id)
        self.assertEqual(
            "https://matrix.example.com", config.accounts[0].homeserver_url
        )
        self.assertIsNone(config.accounts[1].password)
        self.assertEqual("token", config.accounts[1].token)
        self.assertEqual("other_token.json", config.accounts[1].token_file)
        self.assertEqual("KLMNOPQRST", config.accounts[1].device_id)
        self.assertEqual("https://matrix.domain.tld", config.accounts[1].homeserver_url)
        self.assertEqual("fake_device_name", config.device_name)
        self.assertEqual(["!abcdefgh:matrix.example.com"], config.allowed_rooms)
        self.assertEqual({"🤫", "😶", "🤐", "🤗"}, config.allowed_reactions)
        self.assertEqual({"🤗"}, config.insult_reactions)

        self.assertIsNone(config.address)
        self.assertIsNone(config.port)
        self.assertEqual("matrix-alertbot.socket", config.socket)

        self.assertEqual("http://localhost:9093", config.alertmanager_url)

        expected_expire_time = timedelta(days=7).total_seconds()
        self.assertEqual(expected_expire_time, config.cache_expire_time)
        self.assertEqual("data/cache", config.cache_dir)

        self.assertEqual("data/store", config.store_dir)

        self.assertEqual("data/templates", config.template_dir)

    def test_read_config_raise_config_error(self) -> None:
        with self.assertRaises(ParseConfigError):
            Config("")

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_storage_path_error(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = True

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        with self.assertRaises(ParseConfigError):
            Config(config_path)

        fake_path_isdir.assert_called_once_with("data/store")
        fake_path_exists.assert_called_once_with("data/store")
        fake_mkdir.assert_not_called()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_matrix_user_id(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["matrix"]["accounts"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_matrix_user_password(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["matrix"]["accounts"][0]["password"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_matrix_url(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["matrix"]["accounts"][0]["url"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_matrix_allowed_rooms(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["matrix"]["allowed_rooms"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_webhook_address(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["webhook"]["address"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_alertmanager_url(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["alertmanager"]["url"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_cache_path(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["cache"]["path"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_missing_storage_path(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        del config.config_dict["storage"]["path"]

        with self.assertRaises(RequiredConfigKeyError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_invalid_matrix_user_id(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)

        config.config_dict["matrix"]["accounts"][0]["id"] = ""
        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

        config.config_dict["matrix"]["accounts"][0]["id"] = "@fake_user"
        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

        config.config_dict["matrix"]["accounts"][0]["id"] = "@fake_user:"
        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

        config.config_dict["matrix"]["accounts"][0]["id"] = ":matrix.example.com"
        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

        config.config_dict["matrix"]["accounts"][0]["id"] = "@:matrix.example.com"
        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

        config.config_dict["matrix"]["accounts"][0]["id"] = "@:"
        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    def test_parse_config_with_both_webhook_socket_and_address(
        self, fake_mkdir: Mock, fake_path_exists: Mock, fake_path_isdir: Mock
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.minimal.yml")
        config = DummyConfig(config_path)
        config.config_dict["webhook"]["socket"] = "matrix-alertbot.socket"

        with self.assertRaises(InvalidConfigError):
            config._parse_config_values()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    @patch.object(matrix_alertbot.config, "logger")
    def test_parse_config_with_both_logging_disabled(
        self,
        fake_logger: Mock,
        fake_mkdir: Mock,
        fake_path_exists: Mock,
        fake_path_isdir: Mock,
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.full.yml")
        config = DummyConfig(config_path)
        config.config_dict["logging"]["file_logging"]["enabled"] = False
        config.config_dict["logging"]["console_logging"]["enabled"] = False

        config._parse_config_values()

        fake_logger.addHandler.assert_not_called()
        fake_logger.setLevel.assert_called_once_with("DEBUG")

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.mkdir")
    @patch.object(matrix_alertbot.config, "logger", autospec=True)
    @patch.object(matrix_alertbot.config, "logging", autospec=True)
    def test_parse_config_with_level_logging_different(
        self,
        fake_logging: Mock,
        fake_logger: Mock,
        fake_mkdir: Mock,
        fake_path_exists: Mock,
        fake_path_isdir: Mock,
    ) -> None:
        fake_path_isdir.return_value = False
        fake_path_exists.return_value = False

        config_path = os.path.join(CONFIG_RESOURCES_DIR, "config.full.yml")
        config = DummyConfig(config_path)
        config.config_dict["logging"]["file_logging"]["enabled"] = True
        config.config_dict["logging"]["file_logging"]["level"] = "WARN"
        config.config_dict["logging"]["console_logging"]["enabled"] = True
        config.config_dict["logging"]["console_logging"]["level"] = "ERROR"

        config._parse_config_values()

        self.assertEqual(2, fake_logger.addHandler.call_count)
        fake_logger.setLevel.assert_called_once_with("DEBUG")
        fake_logging.FileHandler.return_value.setLevel.assert_called_once_with("WARN")
        fake_logging.StreamHandler.return_value.setLevel.assert_called_once_with(
            "ERROR"
        )


if __name__ == "__main__":
    unittest.main()
