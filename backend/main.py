from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config import settings
from app.database import init_db
from app.routes import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event: startup e shutdown da aplicação."""
    init_db()
    yield


# Criar instância da aplicação
app = FastAPI(
    title="Kovir Cash API",
    description="API de gerenciamento de lançamentos financeiros",
    version="0.1.0",
    lifespan=lifespan,
)

# Incluir router de autenticação
app.include_router(auth_router)


# Rota de health check
@app.get("/")
async def root():
    """
    Verifica se a API está rodando.
    Retorna status da aplicação.
    """
    return {
        "message": "Kovir Cash API rodando!",
        "debug": settings.DEBUG,
        "version": "0.1.0",
    }


# Executar servidor localmente com uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )