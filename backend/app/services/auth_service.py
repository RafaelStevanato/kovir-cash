from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.config import settings


# --- Configurar bcrypt para hash de passwords -----------------------------------
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")



# --- Serviço de autenticação (validação, hash, JWT) -----------------------------
class AuthService:
    
    # --- Inicializa o serviço com o repositório de usuários ---------------------
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    # --- Faz hash de uma senha com bcrypt ---------------------------------------
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    # --- Verifica se uma senha corresponde ao hash ------------------------------
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    # --- Cria um JWT token de acesso --------------------------------------------
    @staticmethod
    def create_access_token(user_id: str) -> str:
        payload = {
            "sub": user_id,  # subject = user_id
            "exp": datetime.now(timezone.utc) + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        return token
    
    # --- Registra um novo usuário -----------------------------------------------
    def signup(self, email: str, password: str) -> dict:
        
        # --- 1. Verificar se email já existe --- #
        existing_user = self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("E-mail já registrado por outro usuário.")
        
        # --- 2. Hash a password --- #
        hashed_password = self.hash_password(password)
        
        # ---  3. Criar user no banco --- #
        user = self.user_repository.create_user(email, hashed_password)
        
        # --- 4. Gerar token --- #
        access_token = self.create_access_token(str(user.id))
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {"id": str(user.id), "email": user.email}
        }

    # --- Autentica um usuário e gera token JWT ----------------------------------
    def login(self, email: str, password: str) -> dict:

        # --- 1. Buscar user por email --- #
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("Email ou senha incorretos.")
        
        # --- 2. Verificar password --- #
        if not self.verify_password(password, user.password):
            raise ValueError("Email ou senha incorretos.")
        
        # --- 3. Gerar token --- #
        access_token = self.create_access_token(str(user.id))
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {"id": str(user.id), "email": user.email}
        }