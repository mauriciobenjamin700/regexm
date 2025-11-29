"""
Password Validation Functions

This module provides functions to validate password requirements.
"""

import re


def validate_password_length(password: str, min_length: int = 8) -> bool:
    """
    Validates if password meets minimum length requirement.

    Args:
        password (str): Password to validate
        min_length (int): Minimum required length (default: 8)

    Returns:
        bool: True if password meets length requirement, False otherwise

    Example:
        - validate_password_length("mypassword")  # Returns: True
        - validate_password_length("short", 6)  # Returns: False
        - validate_password_length("longenough", 10)  # Returns: True
    """
    return len(password) >= min_length


def validate_password_strength(password: str) -> dict:
    """
    Validates password strength based on common criteria.

    Args:
        password (str): Password to validate

    Returns:
        dict: Dictionary with strength validation results

    Example:
        - validate_password_strength("Password123!")
          - Returns: {
            "valid": True,
            "score": 5,
            "errors": [],
            "has_lowercase": True,
            "has_uppercase": True,
            "has_digit": True,
            "has_special": True,
            "has_min_length": True
            }
        - validate_password_strength("weakpass")
          - Returns: {
            "valid": False,
            "score": 2,
            "errors": [
                "Password must contain uppercase letters",
                "Password must contain numbers",
                "Password must contain special characters"
            ],
            "has_lowercase": True,
            "has_uppercase": False,
            "has_digit": False,
            "has_special": False,
            "has_min_length": True
            }
    """
    result = {
        "valid": True,
        "score": 0,
        "errors": [],
        "has_lowercase": False,
        "has_uppercase": False,
        "has_digit": False,
        "has_special": False,
        "has_min_length": False,
    }

    # Check minimum length (8 characters)
    if len(password) >= 8:
        result["has_min_length"] = True
        result["score"] += 1
    else:
        result["valid"] = False
        result["errors"].append("Password must be at least 8 characters long")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        result["has_lowercase"] = True
        result["score"] += 1
    else:
        result["errors"].append("Password must contain lowercase letters")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        result["has_uppercase"] = True
        result["score"] += 1
    else:
        result["errors"].append("Password must contain uppercase letters")

    # Check for digits
    if re.search(r"\d", password):
        result["has_digit"] = True
        result["score"] += 1
    else:
        result["errors"].append("Password must contain numbers")

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        result["has_special"] = True
        result["score"] += 1
    else:
        result["errors"].append("Password must contain special characters")

    # Password is considered valid if it meets at least minimum length
    # and has a score of at least 3
    if result["score"] < 3:
        result["valid"] = False

    return result


def validate_password_match(password: str, confirm_password: str) -> bool:
    """
    Validates if password and confirmation match.

    Args:
        password (str): Original password
        confirm_password (str): Confirmation password

    Returns:
        bool: True if passwords match, False otherwise

    Example:
        - validate_password_match("mypassword", "mypassword")  # Returns: True
        - validate_password_match("mypassword", "different")  # Returns: False
    """
    return password == confirm_password
