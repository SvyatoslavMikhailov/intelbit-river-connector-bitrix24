"""Коннектор Bitrix24 (CRM + Торговый каталог) для Интелбит:Река."""

from intelbit_river_connector_bitrix24.connector import Bitrix24Connector
from intelbit_river_connector_bitrix24.webhooks import (
    Bitrix24WebhookReceiver,
    WebhookValidationError,
)

__version__ = "0.1.0"

__all__ = [
    "Bitrix24Connector",
    "Bitrix24WebhookReceiver",
    "WebhookValidationError",
]
