from fastapi import FastAPI
from app.config import settings                                     

# --- Criar instância da aplicação -----------------------------------------------
app = FastAPI(
    title = "Kovir Cash API",
    description = "API de gerenciamento de lançamentos financeiros",
    version = "0.1.0",
)

# --- Rota de health check (verifica se a API está rodando) ----------------------
@app.get("/")
async def root():
    return {
        "message": "Kovir Cash API rodando!",
        "debug": settings.DEBUG,
        "version": "0.1.0",
    }

# --- Executar servidor localmente com o uvicorn ---------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "0.0.0.0",
        port = 8000,
        reload = settings.DEBUG,
    )