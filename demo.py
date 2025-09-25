#!/usr/bin/env python3
"""
Demo completa da biblioteca de validadores brasileiros

Este arquivo demonstra todos os recursos da biblioteca.
Execute: python3 demo.py
"""

from validators.cpf import validate_cpf, format_cpf
from validators.crv import validate_crv, format_crv
from validators.cnh import validate_cnh, format_cnh
from validators.plate import validate_plate, format_plate
from validators.email import validate_email, extract_domain
from validators.phone import format_brazilian_phone, validate_brazilian_phone
from validators.password import validate_password_strength
from validators.user import validate_user_data
from validators.driver import validate_driver_data


def demo_cpf():
    """Demonstração das funções de CPF."""
    print("📄 DEMONSTRAÇÃO CPF")
    print("-" * 40)
    
    cpfs = [
        "11144477735",      # Válido
        "111.444.777-35",   # Válido com formatação
        "11111111111",      # Inválido (todos iguais)
        "123.456.789-00",   # Inválido (dígitos verificadores errados)
    ]
    
    for cpf in cpfs:
        is_valid = validate_cpf(cpf)
        formatted = format_cpf(cpf)
        print(f"CPF: {cpf:15} | Válido: {is_valid:5} | Formatado: {formatted}")
    print()


def demo_phone():
    """Demonstração das funções de telefone."""
    print("📱 DEMONSTRAÇÃO TELEFONE")
    print("-" * 40)
    
    phones = [
        "11987654321",
        "1187654321",       # Sem o 9 - será adicionado
        "(11) 98765-4321", 
        "11 98765 4321",
        "85999887766",      # Ceará
    ]
    
    for phone in phones:
        is_valid = validate_brazilian_phone(phone)
        formatted = format_brazilian_phone(phone)
        print(f"Telefone: {phone:15} | Válido: {is_valid:5} | Formatado: {formatted}")
    print()


def demo_plates():
    """Demonstração das funções de placas."""
    print("🚗 DEMONSTRAÇÃO PLACAS")
    print("-" * 40)
    
    plates = [
        "BRA2E19",     # Mercosul
        "BRA-2E19",    # Mercosul com hífen
        "ABC1234",     # Formato antigo
        "ABC-1234",    # Formato antigo com hífen
        "XYZ9Z99",     # Mercosul válido
    ]
    
    from validators.plate import is_old_format_plate, is_mercosul_format_plate
    
    for plate in plates:
        is_valid = validate_plate(plate)
        is_old = is_old_format_plate(plate)
        is_mercosul = is_mercosul_format_plate(plate)
        formatted = format_plate(plate, 'dash')
        
        format_type = "Antigo" if is_old else ("Mercosul" if is_mercosul else "Inválido")
        
        print(f"Placa: {plate:10} | Válido: {is_valid:5} | Tipo: {format_type:8} | Formatado: {formatted}")
    print()


def demo_documents():
    """Demonstração de CRV e CNH."""
    print("📋 DEMONSTRAÇÃO DOCUMENTOS")
    print("-" * 40)
    
    # CRV
    crvs = ["ABC12345678", "12345678901", "XYZ0987654A"]
    print("CRV:")
    for crv in crvs:
        is_valid = validate_crv(crv)
        formatted = format_crv(crv)
        print(f"  {crv:12} | Válido: {is_valid:5} | Limpo: {formatted}")
    
    print("\nCNH:")
    cnhs = ["12345678901", "123.456.789-01", "98765432100"]
    for cnh in cnhs:
        is_valid = validate_cnh(cnh)
        formatted = format_cnh(cnh)
        print(f"  {cnh:15} | Válido: {is_valid:5} | Limpo: {formatted}")
    print()


def demo_email():
    """Demonstração das funções de email."""
    print("✉️  DEMONSTRAÇÃO EMAIL")
    print("-" * 40)
    
    emails = [
        "usuario@exemplo.com",
        "nome.sobrenome@empresa.com.br",
        "test@domain.co.uk",
        "invalid.email",
        "@domain.com",
    ]
    
    for email in emails:
        is_valid = validate_email(email)
        domain = extract_domain(email) if is_valid else "N/A"
        print(f"Email: {email:25} | Válido: {is_valid:5} | Domínio: {domain}")
    print()


def demo_password():
    """Demonstração da validação de senhas."""
    print("🔐 DEMONSTRAÇÃO SENHAS")
    print("-" * 50)
    
    passwords = [
        "MinhaSenh@123!",   # Perfeita
        "senha123",         # Sem maiúscula e especial
        "SENHA123!",        # Sem minúscula
        "SenhaForte!",      # Sem número
        "12345678",         # Só números
        "abc",              # Muito fraca
    ]
    
    for password in passwords:
        result = validate_password_strength(password)
        strength = ["Muito Fraca", "Fraca", "Regular", "Boa", "Forte", "Muito Forte"][result['score']]
        
        print(f"Senha: {'*' * len(password):15} | Score: {result['score']}/5 | Força: {strength}")
        if result['errors']:
            for error in result['errors'][:2]:  # Mostra só os 2 primeiros erros
                print(f"  ⚠️  {error}")
    print()


def demo_user_validation():
    """Demonstração da validação completa de usuário."""
    print("👤 DEMONSTRAÇÃO VALIDAÇÃO DE USUÁRIO")
    print("-" * 50)
    
    # Usuário válido
    valid_user = {
        'name': 'Ana Silva',
        'email': 'ana.silva@email.com',
        'phone': '11987654321',
        'password': 'MinhaSenh@123!',
        'confirm_password': 'MinhaSenh@123!'
    }
    
    # Usuário com problemas
    invalid_user = {
        'name': '',
        'email': 'email-invalido',
        'phone': '123',
        'password': 'abc',
        'confirm_password': 'xyz'
    }
    
    print("✅ Usuário válido:")
    result = validate_user_data(valid_user)
    print(f"   Status: {'APROVADO' if result['valid'] else 'REJEITADO'}")
    if result['errors']:
        for error in result['errors']:
            print(f"   ❌ {error}")
    
    print("\n❌ Usuário inválido:")
    result = validate_user_data(invalid_user)
    print(f"   Status: {'APROVADO' if result['valid'] else 'REJEITADO'}")
    for error in result['errors']:
        print(f"   ❌ {error}")
    print()


def demo_driver_validation():
    """Demonstração da validação de dados de motorista."""
    print("🚚 DEMONSTRAÇÃO VALIDAÇÃO DE MOTORISTA")
    print("-" * 50)

    # Motorista válido
    valid_driver = ('12345678901', 'ABC12345678', 'BRA2E19')

    # Motorista inválido  
    invalid_driver = ('123', 'ABC', 'XYZ')

    print("✅ Motorista válido:")
    result = validate_driver_data(*valid_driver)
    print(f"   Status: {'APROVADO' if result['valid'] else 'REJEITADO'}")
    print(f"   CNH: {result['cnh_valid']} | CRV: {result['crv_valid']} | Placa: {result['plate_valid']}")
    
    print("\n❌ Motorista inválido:")
    result = validate_driver_data(*invalid_driver)
    print(f"   Status: {'APROVADO' if result['valid'] else 'REJEITADO'}")
    print(f"   CNH: {result['cnh_valid']} | CRV: {result['crv_valid']} | Placa: {result['plate_valid']}")
    for error in result['errors']:
        print(f"   ❌ {error}")
    print()


def main():
    """Executa todas as demonstrações."""
    print("🇧🇷 BIBLIOTECA DE VALIDADORES BRASILEIROS")
    print("=" * 60)
    print("Demonstração completa de todas as funcionalidades\n")
    
    demo_cpf()
    demo_phone()
    demo_plates()
    demo_documents()
    demo_email()
    demo_password()
    demo_user_validation()
    demo_driver_validation()
    
    print("🎉 Demonstração concluída!")
    print("💡 Para usar em seus projetos:")
    print("   from validators.cpf import validate_cpf")
    print("   from validators.user import validate_user_data")
    print("   # ... e assim por diante")


if __name__ == "__main__":
    main()