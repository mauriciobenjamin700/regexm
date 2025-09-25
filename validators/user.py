"""
Main Validation Functions

This module provides a comprehensive validation function that combines
all validation types used in forms and user data.
"""

from .email import validate_email
from .password import validate_password_length, validate_password_match
from .phone import validate_brazilian_phone


def validate_user_data(data: dict) -> dict:
    """
    Validates user registration/profile data.

    Args:
        data (dict): Dictionary containing user data with keys:
                    'name', 'email', 'phone', 'password', 'confirm_password'

    Returns:
        dict: Dictionary with validation results and error messages
    """
    result = {"valid": True, "errors": [], "field_errors": {}}

    # Check required fields
    required_fields = ["name", "email", "phone", "password"]
    for field in required_fields:
        if not data.get(field):
            result["valid"] = False
            result["errors"].append(f"Faltam dados a preencher: {field}")
            result["field_errors"][field] = f"Campo {field} é obrigatório"

    # Validate name
    if data.get("name"):
        if len(data["name"].strip()) == 0:
            result["valid"] = False
            result["errors"].append("Nome inválido")
            result["field_errors"]["name"] = "Nome inválido"

    # Validate email
    if data.get("email"):
        if not validate_email(data["email"]):
            result["valid"] = False
            result["errors"].append("Email inválido")
            result["field_errors"]["email"] = "Email inválido"

    # Validate password
    if data.get("password"):
        if not validate_password_length(data["password"], 8):
            result["valid"] = False
            result["errors"].append("A senha precisa ter pelo menos 8 dígitos")
            result["field_errors"][
                "password"
            ] = "A senha precisa ter pelo menos 8 dígitos"

    # Validate password confirmation
    if data.get("confirm_password") is not None:
        if not validate_password_match(
            data.get("password", ""), data["confirm_password"]
        ):
            result["valid"] = False
            result["errors"].append("As senhas não conferem")
            result["field_errors"][
                "confirm_password"
            ] = "As senhas não conferem"

    # Validate phone
    if data.get("phone"):
        if not validate_brazilian_phone(data["phone"]):
            result["valid"] = False
            result["errors"].append(
                "Número de celular precisa de pelo menos 11 dígitos"
            )
            result["field_errors"][
                "phone"
            ] = "Número de celular precisa de pelo menos 11 dígitos"

    return result


def validate_user_data_simple(data: dict) -> bool:
    """
    Simple validation that returns only True/False.

    Args:
        data (dict): Dictionary containing user data

    Returns:
        bool: True if all data is valid, False otherwise
    """
    validation = validate_user_data(data)
    return validation["valid"]
