"""Utility functions"""

import os
from typing import Optional
import hashlib
import random
import string


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


def generate_random_string(length: int = 10) -> str:
    """Generate a random string of specified length.

    Args:
        length: Length of the random string to generate. Default is 10.

    Returns:
        str: Random string of specified length.

    Example:
        >>> generate_random_string(8)
        'y94ZpBc7'
    """
    letters_and_digits = string.ascii_letters + string.digits
    random_string = "".join(random.choice(letters_and_digits) for _ in range(length))
    return random_string


def generate_md5_hash(data: str) -> str:
    """Generate the MD5 hash of the input data.

    Args:
        data: The string to be hashed.

    Returns:
        str: MD5 hash of the input data as a hexadecimal string.

    Example:
        >>> generate_md5_hash('Hello, World!')
        'ed076287532e86365e841e92bfc50d8c'
    """
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode("utf-8"))
    hashed_data = md5_hash.hexdigest()
    return hashed_data
