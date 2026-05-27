from sqlalchemy.orm import Session
from app.models.user import User

# --- Repository para operações com usuários no banco de dados -------------------
class UserRepository:
    
    # --- Inicializa o repository com uma sessão de banco ------------------------
    def __init__(self, session: Session):
        self.session = session


    # --- Cria um novo usuário no banco de dados ---------------------------------
    def create_user(self, email: str, hashed_password: str) -> User:
        user = User(email=email, password=hashed_password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    # --- Busca um usuário por email no banco de dados ---------------------------
    def get_user_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter(User.email == email).first()