from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
import uuid
from app.models.user import Base

# --- Representa a tabela "lancamentos" no banco de dados ------------------------------
class Lancamento(Base):
    __tablename__ = "lancamentos"

    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    usuario_lancamento = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    tipo_lancamento = Column(String, nullable = False)
    valor_lancamento = Column(Numeric(precision=10, scale=2), unique = False, nullable = False, index = True)
    data_lancamento = Column(DateTime, nullable = False)
    descricao_lancamento = Column(String, nullable = True)
    criado_em = Column(DateTime, nullable = False, default = lambda: datetime.now(timezone.utc))