"""
This module provides configurations and utilities for the COGFlow plugins.

Attributes:
    TRACKING_URI (str): The URI for tracking experiments.
    TIMER_IN_SEC (int): Timer interval in seconds.
    ML_TOOL (str): Machine learning tool being used.
    ACCESS_KEY_ID (str): Access key ID for authentication.
    SECRET_ACCESS_KEY (str): Secret access key for authentication.
    S3_ENDPOINT_URL (str): Endpoint URL for Amazon S3.
"""

from cogflow.plugin_config import (
    TRACKING_URI,
    TIMER_IN_SEC,
    ML_TOOL,
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY,
    S3_ENDPOINT_URL,
)
from cogflow.plugin_status import plugin_statuses
from cogflow.pluginerrors import PluginErrors
from cogflow.pluginmanager import PluginManager
