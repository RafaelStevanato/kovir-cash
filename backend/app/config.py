from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# --- Configurações da aplicação Kovir Cash --------------------------------------
class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
    

    # --- Banco de Dados ---------------------------------------------------------

    DATABASE_URL: str = Field(
        ...,
        description="URL de conexão PostgreSQL. Formato: postgresql+psycopg://usuario:senha@host:porta/nome-banco-de-dados"
    )


    # --- JWT (Autenticação) -----------------------------------------------------

    SECRET_KEY: str = Field(
        ...,
        description="Chave secreta para autenticação de JWT. Gere com: python -c 'import secrets; print(secrets.token_urlsafe(32))'"
    )
    
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24


    # --- Aplicação --------------------------------------------------------------

    DEBUG: bool = True
    

# --- Instância global de configurações ------------------------------------------

settings = Settings()                                     