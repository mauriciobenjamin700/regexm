"""
Quick Start Guide and Usage Examples

Run this file to test all validation functions:
python examples.py
"""

# Example of how to use the validation functions
from validators.cpf import validate_cpf, format_cpf
from validators.crv import validate_crv
from validators.cnh import validate_cnh  
from validators.plate import validate_plate
from validators.email import validate_email
from validators.phone import validate_brazilian_phone, format_brazilian_phone
from validators.user import validate_user_data


def quick_examples():
    """Quick examples of main validation functions."""
    
    print("🔍 REGEX LIB - Brazilian Validators")
    print("=" * 50)
    
    # CPF Example
    cpf_test = "11144477735"
    print(f"CPF {cpf_test}: {validate_cpf(cpf_test)} - {format_cpf(cpf_test)}")
    
    # CRV Example  
    crv_test = "ABC12345678"
    print(f"CRV {crv_test}: {validate_crv(crv_test)}")
    
    # CNH Example
    cnh_test = "12345678901" 
    print(f"CNH {cnh_test}: {validate_cnh(cnh_test)}")
    
    # Plate Example
    plate_test = "BRA2E19"
    print(f"Plate {plate_test}: {validate_plate(plate_test)}")
    
    # Email Example
    email_test = "user@example.com"
    print(f"Email {email_test}: {validate_email(email_test)}")
    
    # Phone Example
    phone_test = "11987654321"
    is_valid = validate_brazilian_phone(phone_test)
    formatted = format_brazilian_phone(phone_test)
    print(f"Phone {phone_test}: {is_valid} - {formatted}")
    
    # Complete user validation
    user_data = {
        'name': 'João Silva',
        'email': 'joao@email.com', 
        'phone': '11987654321',
        'password': 'MyPassword123!',
        'confirm_password': 'MyPassword123!'
    }
    
    result = validate_user_data(user_data)
    print(f"User data valid: {result['valid']}")
    
    print("=" * 50)
    print("✅ All basic validations completed!")
    print("📚 Check examples.py for detailed tests")


if __name__ == "__main__":
    quick_examples()