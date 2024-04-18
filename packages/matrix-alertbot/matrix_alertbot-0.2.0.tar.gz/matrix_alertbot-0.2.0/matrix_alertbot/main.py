#!/usr/bin/env python3
from __future__ import annotations

import asyncio
import logging
import sys

from diskcache import Cache

from matrix_alertbot.alertmanager import AlertmanagerClient
from matrix_alertbot.config import Config
from matrix_alertbot.matrix import MatrixClientPool
from matrix_alertbot.webhook import Webhook

logger = logging.getLogger(__name__)


def main() -> None:
    """The first function that is run when starting the bot"""

    # Read user-configured options from a config file.
    # A different config file path can be specified as the first command line argument
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        config_path = "config.yaml"

    # Read the parsed config file and create a Config object
    config = Config(config_path)

    # Configure the cache
    cache = Cache(config.cache_dir)

    # Configure Alertmanager client
    alertmanager_client = AlertmanagerClient(config.alertmanager_url, cache)

    # Create matrix clients
    matrix_client_pool = MatrixClientPool(alertmanager_client, cache, config)
    # Configure webhook server
    webhook_server = Webhook(matrix_client_pool, alertmanager_client, cache, config)

    loop = asyncio.get_event_loop()
    loop.create_task(matrix_client_pool.switch_active_client())
    loop.create_task(webhook_server.start())
    for account in config.accounts:
        loop.create_task(matrix_client_pool.start(account, config))

    try:
        loop.run_forever()
    except Exception as e:
        logger.error(e)
    finally:
        loop.run_until_complete(webhook_server.close())
        loop.run_until_complete(alertmanager_client.close())
        loop.run_until_complete(matrix_client_pool.close())
        cache.close()
