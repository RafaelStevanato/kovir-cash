from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from sqlalchemy.orm import declarative_base


# --- Base para todos os models herdarem -----------------------------------------
Base = declarative_base()


# --- Representa a tabela "users" no banco de dados ------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    criado_em = Column(DateTime, nullable=False, default=datetime.utcnow)