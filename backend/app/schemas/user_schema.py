from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID


# --- Schema para criação de usuário ---------------------------------------------
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, description="Mínimo 8 caracteres")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "rafael@example.com",
                "password": "senha123456"
            }
        }

# --- Schema para resposta ao usuário (após login) -------------------------------
class UserResponse(BaseModel):
    id: UUID
    email: str
    criado_em: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "email": "rafael@example.com",
                "criado_em": "2025-05-27T10:30:00"
            }
        }