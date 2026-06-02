# --- Importa o serviço que vamos testar -----------------------------------
import pytest
from unittest.mock import MagicMock
from app.services.auth_service import AuthService


# --- Teste 1: Hash de senha -----------------------------------------------
# Garante que a senha não é salva em texto puro no banco
def test_hash_password():
    # Gera o hash de uma senha
    hashed = AuthService.hash_password("senha123")
    
    # O hash NUNCA pode ser igual à senha original
    assert hashed != "senha123"


# --- Teste 2: Senha correta deve ser verificada ---------------------------
# Garante que o login funciona com a senha certa
def test_verify_password_correct():
    # Primeiro gera o hash (como no signup)
    hashed = AuthService.hash_password("senha123")
    
    # Verifica se a senha original bate com o hash — deve ser True
    assert AuthService.verify_password("senha123", hashed) == True


# --- Teste 3: Senha errada deve ser rejeitada -----------------------------
# Garante que o login falha com senha incorreta
def test_verify_password_wrong():
    # Gera o hash da senha original
    hashed = AuthService.hash_password("senha123")
    
    # Tenta verificar com senha diferente — deve ser False
    assert AuthService.verify_password("senha_errada", hashed) == False

# Teste de e-mail já existente (deve ser rejeitado)
def test_signup_email_exists():
    # --- Arrange (preparar) ---
    mock_repository = MagicMock()
    mock_repository.get_user_by_email.return_value = {"id": 1, "email": "rafael@example.com"}

    service = AuthService(mock_repository)

    with pytest.raises(ValueError) as exc_info:
        service.signup("rafael@example.com", "senha123")
    
    assert str(exc_info.value) == "E-mail já registrado por outro usuário."

def test_signup_success():
    # --- Arrange ---
    mock_repository = MagicMock()
    mock_repository.get_user_by_email.return_value = None  # Email NÃO existe
    
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.email = "rafael@example.com"
    
    mock_repository.create_user.return_value = mock_user
    
    service = AuthService(mock_repository)
    
    # --- Act ---
    result = service.signup("rafael@example.com", "senha123")
    
    # --- Assert ---
    assert "access_token" in result
    assert "token_type" in result
    assert result["user"]["email"] == "rafael@example.com"

def test_login_success():
    # --- Arrange ---
    mock_repository = MagicMock()
    
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.email = "rafael@example.com"
    mock_user.password = AuthService.hash_password("senha123")  # Hash correto
    
    mock_repository.get_user_by_email.return_value = mock_user
    
    service = AuthService(mock_repository)
    
    # --- Act ---
    result = service.login("rafael@example.com", "senha123")
    
    # --- Assert ---
    assert "access_token" in result
    assert result["user"]["email"] == "rafael@example.com"

def test_create_access_token():
    # --- Arrange ---
    user_id = "123"
    
    # --- Act ---
    token = AuthService.create_access_token(user_id)
    
    # --- Assert ---
    assert isinstance(token, str)
    assert len(token) > 0


