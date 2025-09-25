"""
Driver Data Validation Functions

This module provides functions to validate Brazilian driver-related documents
and information (CNH, CRV, and vehicle plates).
"""

from .cnh import validate_cnh
from .crv import validate_crv
from .plate import validate_plate


def validate_driver_data(cnh: str, crv: str, car_plate: str) -> dict:
    """
    Validates all driver-related data at once.

    Args:
        cnh (str): CNH (driver's license) to validate
        crv (str): CRV (vehicle registration) to validate
        car_plate (str): Vehicle plate to validate

    Returns:
        dict: Dictionary with validation results and error messages
    """
    result = {
        "valid": True,
        "errors": [],
        "cnh_valid": False,
        "crv_valid": False,
        "plate_valid": False,
    }

    # Verifica se todos os campos foram preenchidos
    if not cnh and not crv and not car_plate:
        result["valid"] = False
        result["errors"].append(
            "Todos os campos devem ser preenchidos para cadastrar o motorista."
        )
        return result

    # Valida CNH
    if not validate_cnh(cnh):
        result["valid"] = False
        result["cnh_valid"] = False
        result["errors"].append("CNH inválida. Geralmente 11 ou 12 números.")
    else:
        result["cnh_valid"] = True

    # Valida CRV
    if not validate_crv(crv):
        result["valid"] = False
        result["crv_valid"] = False
        result["errors"].append(
            "CRV inválido. Por favor, insira um CRV válido, "
            "geralmente 11 ou 12 números"
        )
    else:
        result["crv_valid"] = True

    # Valida placa
    if not validate_plate(car_plate):
        result["valid"] = False
        result["plate_valid"] = False
        result["errors"].append(
            "Placa inválida. Padrão Antigo: BRA-2E19, "
            "Padrão Mercosul: BRA-1234"
        )
    else:
        result["plate_valid"] = True

    return result


def validate_driver_data_simple(cnh: str, crv: str, car_plate: str) -> bool:
    """
    Simple validation that returns only True/False.

    Args:
        cnh (str): CNH to validate
        crv (str): CRV to validate
        car_plate (str): Vehicle plate to validate

    Returns:
        bool: True if all data is valid, False otherwise
    """
    if not cnh and not crv and not car_plate:
        return False

    return (
        validate_cnh(cnh) and validate_crv(crv) and validate_plate(car_plate)
    )
