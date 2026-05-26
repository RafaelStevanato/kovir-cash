from pydantic_settings import BaseSettings

# --- Configurações da aplicação Kovir Cash --------------------------------------
class Settings(BaseSettings):
    

    # --- Banco de Dados ---------------------------------------------------------

    DATABASE_URL: str = "postgresql://user:password@localhost:5432/kovir_cash"


    # --- JWT (Autenticação) -----------------------------------------------------

    SECRET_KEY: str = "minha-chave-secreta-mude-em-producao"  # type: ignore
    ALGORITHM : str = "HS256"                                 # type: ignore
    ACCES_TOKEN_EXPIRE_HOURS: int = 24


    # --- Aplicação --------------------------------------------------------------

    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


    # --- Instância global de configurações --------------------------------------

    settings = Settings()