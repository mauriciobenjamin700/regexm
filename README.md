# REGEX LIB

Este projeto é uma biblioteca Python para validação de documentos brasileiros e dados de formulários comuns em aplicações web.

## 📋 Funcionalidades

### Documentos Brasileiros
- **CPF**: Validação com algoritmo oficial e formatação
- **CRV**: Validação de Certificado de Registro de Veículo  
- **CNH**: Validação de Carteira Nacional de Habilitação
- **Placas**: Suporte aos formatos antigo (AAA-0000) e Mercosul (AAA0A00)

### Dados de Formulários
- **Email**: Validação com regex e extração de domínio/usuário
- **Telefone**: Formatação automática para padrão brasileiro com DDD
- **Senha**: Validação de força e critérios de segurança
- **Dados de Usuário**: Validação completa de formulários de cadastro

## 🚀 Como Usar

### Instalação e Execução Rápida

```bash
# Clone o projeto
git clone <seu-repositorio>
cd regex-lib

# Execute os exemplos
python quick_start.py
```

### Exemplos de Uso

```python
from validators.cpf import validate_cpf, format_cpf
from validators.phone import format_brazilian_phone
from validators.user import validate_user_data

# Validação de CPF
cpf = "11144477735"
is_valid = validate_cpf(cpf)  # True
formatted = format_cpf(cpf)   # "111.444.777-35"

# Formatação de telefone
phone = "11987654321"
formatted_phone = format_brazilian_phone(phone)  # "(11) 98765-4321"

# Validação completa de usuário
user_data = {
    'name': 'João Silva',
    'email': 'joao@email.com',
    'phone': '11987654321', 
    'password': 'MinhaSenh@123',
    'confirm_password': 'MinhaSenh@123'
}

result = validate_user_data(user_data)
print(result['valid'])  # True/False
print(result['errors']) # Lista de erros, se houver
```

## 📁 Estrutura do Projeto

```
regex-lib/
├── validators/
│   ├── __init__.py
│   ├── cpf.py          # Validação de CPF
│   ├── crv.py          # Validação de CRV
│   ├── cnh.py          # Validação de CNH
│   ├── plate.py        # Validação de placas de veículos
│   ├── email.py        # Validação de email
│   ├── phone.py        # Validação e formatação de telefone
│   ├── password.py     # Validação de senhas
│   ├── driver.py       # Validação combinada para motoristas
│   └── user.py         # Validação combinada para usuários
├── examples.py         # Exemplos detalhados de uso
├── quick_start.py      # Guia de início rápido
└── README.md
```

## 🔧 Principais Funções

### CPF
- `validate_cpf(cpf)` - Valida CPF com algoritmo oficial
- `format_cpf(cpf)` - Formata para XXX.XXX.XXX-XX

### Telefone
- `validate_brazilian_phone(phone)` - Valida número brasileiro (11 dígitos)
- `format_brazilian_phone(phone)` - Formata para (XX) 9XXXX-XXXX

### Placas de Veículos
- `validate_plate(plate)` - Valida formatos antigo e Mercosul
- `is_old_format_plate(plate)` - Verifica formato antigo
- `is_mercosul_format_plate(plate)` - Verifica formato Mercosul

### Validação Combinada
- `validate_user_data(data)` - Valida dados completos de usuário
- `validate_driver_data(cnh, crv, plate)` - Valida dados de motorista

## 📝 Exemplos Completos

Execute `python examples.py` para ver todos os testes e exemplos de uso.

## 🎯 Casos de Uso

Esta biblioteca é ideal para:
- Validação de formulários de cadastro
- APIs de registro de usuários
- Sistemas de cadastro de motoristas/veículos
- Aplicações que precisam validar documentos brasileiros
- Formatação automática de dados de entrada

## 🔍 Regex Patterns Utilizados

- **CPF**: Algoritmo oficial com dígitos verificadores
- **Email**: `^[^\s@]+@[^\s@]+\.[^\s@]+$`  
- **Placa Antiga**: `^[A-Z]{3}\d{4}$`
- **Placa Mercosul**: `^[A-Z]{3}\d[A-Z]\d{2}$`
- **CRV**: `^[A-Z0-9]{11}$`
- **CNH**: `^\d{11}$`

## ⚡ Performance

Todas as validações são otimizadas com regex e algoritmos eficientes, adequadas para uso em produção com grande volume de dados.

---

**Autor**: Maurício Benjamim  
**Versão**: 1.0.0
