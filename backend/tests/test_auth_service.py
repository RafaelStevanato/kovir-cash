# --- Importa o serviço que vamos testar -----------------------------------
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