"""Utility functions"""

import os
from typing import Optional


def get_config(
    config_name: str,
    default_value: Optional[str] = None,
    required: bool = False,
) -> Optional[str]:
    """Retrieve a configuration value from the environment.

    Args:
        config_name: Name of the configuration to retrieve.
        default_value: Default value if the configuration is not
            found in the environment (default=None).
        required: Whether the configuration is required (default=False).

    Returns:
        Configuration value retrieved from the environment or the
        default value.

    Raises:
        ValueError: If the configuration is required and not found
            in the environment.

    Examples:
        >>> # Retrieve the value of 'DB_HOST' configuration, which is required
        >>> db_host = get_config('DB_HOST', required=True)
        >>>
        >>> # Retrieve the value of 'DEBUG' configuration with a default value
        >>> debug_mode = get_config('DEBUG', default_value='False')
        >>>
        >>> # Retrieve a non-required configuration with a default value
        >>> non_required_config = get_config('SOME_OPTIONAL_CONFIG', default_value='default_value')
    """
    value = os.getenv(config_name, default_value)

    if required and value is None:
        raise ValueError(
            f"Required configuration '{config_name}' is missing in environment variables."
        )

    return value
