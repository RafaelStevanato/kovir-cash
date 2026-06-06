from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings
from app.models.user import Base
from app.models.lancamento import Lancamento

# --- Criar engine SQLAlchemy conectado ao PostgreSQL ----------------------------
engine = create_engine(
    settings.DATABASE_URL,
    echo = settings.DEBUG,  # --- Mostra SQL em DEBUG mode --- #
)

# --- Factory para criar sessions ------------------------------------------------
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine,
)

# --- Dependência do FastAPI que fornece uma sessão do banco ---------------------
# --- Cria uma nova session para cada requisição ---------------------------------
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Cria todas as tabelas no banco de dados ------------------------------------
# --- Executa os CREATE TABLE baseado nos Models ---------------------------------
def init_db() -> None:
    Base.metadata.create_all(bind=engine)

