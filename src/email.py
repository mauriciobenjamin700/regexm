"""
Email Validation Functions

This module provides functions to validate email addresses.
"""

import re


def validate_email(email: str) -> bool:
    """
    Validates an email address using regex pattern.

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email is valid, False otherwise

    Example:
        - validate_email("test@example.com")  # Returns: True
        - validate_email("invalid-email")  # Returns: False
        - validate_email("user.name+tag+sorting@example.com")  # Returns: True
    """
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(pattern, email))


def is_email_format(email: str) -> bool:
    """
    Checks if the string has a valid email format.

    Args:
        email (str): String to check

    Returns:
        bool: True if string has email format, False otherwise

    Example:
        - is_email_format("test@example.com")  # Returns: True
        - is_email_format("invalid-email")  # Returns: False
        - is_email_format("user.name+tag+sorting@example.com") # Returns: True
    """
    return validate_email(email)


def extract_domain(email: str) -> str:
    """
    Extracts the domain part from an email address.

    Args:
        email (str): Email address

    Returns:
        str: Domain part of the email, or empty string if invalid

    Example:
        - extract_domain("test@example.com")  # Returns: "example.com"
        - extract_domain("invalid-email")  # Returns: ""
        - extract_domain("user.name+ta@example.com")  # Returns: "example.com"
    """
    if validate_email(email):
        return email.split("@")[1]
    return ""


def extract_username(email: str) -> str:
    """
    Extracts the username part from an email address.

    Args:
        email (str): Email address

    Returns:
        str: Username part of the email, or empty string if invalid

    Example:
        - extract_username("test@example.com")  # Returns: "test"
        - extract_username("invalid-email")  # Returns: ""
        - extract_username("user.name@example.com")  # Returns: "user.name"
    """
    if validate_email(email):
        return email.split("@")[0]
    return ""
