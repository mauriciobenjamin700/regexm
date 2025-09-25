"""
Examples and Tests for Brazilian Document Validators

This module provides usage examples for all validation functions.
"""

from validators import cpf, crv, cnh, plate, email, phone, password, user, driver


def test_cpf_validation():
    """Test CPF validation functions."""
    print("=== CPF Validation Tests ===")
    
    # Valid CPFs for testing
    valid_cpfs = ["11144477735", "111.444.777-35"]
    # Invalid CPFs
    invalid_cpfs = ["11111111111", "123.456.789-00", "123"]
    
    for cpf_test in valid_cpfs:
        print(f"CPF {cpf_test}: Valid = {cpf.validate_cpf(cpf_test)}")
        print(f"Formatted: {cpf.format_cpf(cpf_test)}")
    
    for cpf_test in invalid_cpfs:
        print(f"CPF {cpf_test}: Valid = {cpf.validate_cpf(cpf_test)}")


def test_crv_validation():
    """Test CRV validation functions."""
    print("\n=== CRV Validation Tests ===")
    
    # Example CRVs (format examples)
    test_crvs = ["12345678901", "ABC1234567D", "123", "ABCDEFGHIJK"]
    
    for crv_test in test_crvs:
        print(f"CRV {crv_test}: Valid = {crv.validate_crv(crv_test)}")
        print(f"Formatted: {crv.format_crv(crv_test)}")


def test_cnh_validation():
    """Test CNH validation functions."""
    print("\n=== CNH Validation Tests ===")
    
    test_cnhs = ["12345678901", "123.456.789-01", "123", "1234567890123"]
    
    for cnh_test in test_cnhs:
        print(f"CNH {cnh_test}: Valid = {cnh.validate_cnh(cnh_test)}")
        print(f"Formatted: {cnh.format_cnh(cnh_test)}")


def test_plate_validation():
    """Test vehicle plate validation functions."""
    print("\n=== Plate Validation Tests ===")
    
    test_plates = ["BRA2E19", "BRA-2E19", "ABC1234", "ABC-1234", "123ABCD"]
    
    for plate_test in test_plates:
        print(f"Plate {plate_test}: Valid = {plate.validate_plate(plate_test)}")
        print(f"Old format: {plate.is_old_format_plate(plate_test)}")
        print(f"Mercosul format: {plate.is_mercosul_format_plate(plate_test)}")
        print(f"Formatted: {plate.format_plate(plate_test, 'dash')}")


def test_email_validation():
    """Test email validation functions."""
    print("\n=== Email Validation Tests ===")
    
    test_emails = [
        "test@example.com", 
        "invalid.email", 
        "user@domain.com.br",
        "@domain.com",
        "user@"
    ]
    
    for email_test in test_emails:
        print(f"Email {email_test}: Valid = {email.validate_email(email_test)}")
        if email.validate_email(email_test):
            print(f"Domain: {email.extract_domain(email_test)}")
            print(f"Username: {email.extract_username(email_test)}")


def test_phone_validation():
    """Test phone validation functions."""
    print("\n=== Phone Validation Tests ===")
    
    test_phones = ["11987654321", "(11) 98765-4321", "11 87654321", "1198765432"]
    
    for phone_test in test_phones:
        print(f"Phone {phone_test}: Valid = {phone.validate_brazilian_phone(phone_test)}")
        print(f"Formatted: {phone.format_brazilian_phone(phone_test)}")
        
        ddd = phone.clean_phone(phone_test)[:2]
        print(f"DDD {ddd} valid: {phone.is_valid_ddd(ddd)}")


def test_password_validation():
    """Test password validation functions."""
    print("\n=== Password Validation Tests ===")
    
    test_passwords = ["123456", "12345678", "Password123!", "weak"]
    
    for pwd in test_passwords:
        print(f"Password '{pwd}':")
        print(f"  Length valid: {password.validate_password_length(pwd)}")
        strength = password.validate_password_strength(pwd)
        print(f"  Strength score: {strength['score']}/5")
        print(f"  Strength valid: {strength['valid']}")
        
        if strength['errors']:
            print(f"  Errors: {', '.join(strength['errors'])}")


def test_user_data_validation():
    """Test complete user data validation."""
    print("\n=== User Data Validation Tests ===")
    
    # Valid user data
    valid_user = {
        'name': 'João Silva',
        'email': 'joao@email.com',
        'phone': '11987654321',
        'password': 'Password123!',
        'confirm_password': 'Password123!'
    }
    
    # Invalid user data
    invalid_user = {
        'name': '',
        'email': 'invalid-email',
        'phone': '123',
        'password': '123',
        'confirm_password': '456'
    }
    
    print("Valid user data:")
    result = user.validate_user_data(valid_user)
    print(f"  Valid: {result['valid']}")
    if result['errors']:
        print(f"  Errors: {result['errors']}")
    
    print("\nInvalid user data:")
    result = user.validate_user_data(invalid_user)
    print(f"  Valid: {result['valid']}")
    if result['errors']:
        print(f"  Errors: {result['errors']}")


def test_driver_data_validation():
    """Test driver data validation."""
    print("\n=== Driver Data Validation Tests ===")
    
    # Valid driver data
    valid_driver = {
        'cnh': '12345678901',
        'crv': 'ABC12345678',
        'car_plate': 'BRA2E19'
    }
    
    # Invalid driver data  
    invalid_driver = {
        'cnh': '123',
        'crv': '123',
        'car_plate': '123'
    }
    
    print("Valid driver data:")
    result = driver.validate_driver_data(
        valid_driver['cnh'], 
        valid_driver['crv'], 
        valid_driver['car_plate']
    )
    print(f"  Valid: {result['valid']}")
    if result['errors']:
        print(f"  Errors: {result['errors']}")
    
    print("\nInvalid driver data:")
    result = driver.validate_driver_data(
        invalid_driver['cnh'],
        invalid_driver['crv'], 
        invalid_driver['car_plate']
    )
    print(f"  Valid: {result['valid']}")
    if result['errors']:
        print(f"  Errors: {result['errors']}")


if __name__ == "__main__":
    test_cpf_validation()
    test_crv_validation() 
    test_cnh_validation()
    test_plate_validation()
    test_email_validation()
    test_phone_validation()
    test_password_validation()
    test_user_data_validation()
    test_driver_data_validation()