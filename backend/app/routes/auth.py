from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository


# --- Criar router para agrupar rotas de autenticação ----------------------------
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

# --- Dependência que fornece uma sessão do banco (placeholder) ------------------
def get_db() -> Session:
    pass  # Implementaremos quando criar database.py

# --- Rota de sign up ------------------------------------------------------------
@router.post("/signup", response_model=dict, status_code=status.HTTP_201_CREATED)

# --- Função que cria um novo usuário --------------------------------------------
async def signup(
    user_create: UserCreate,
    db: Session = Depends(get_db),
) -> dict:
    try:
        # --- Criar service e repository --- #
        user_repository = UserRepository(db)
        auth_service = AuthService(user_repository)
        
        # --- Chamar signup --- #
        result = auth_service.signup(user_create.email, user_create.password)
        
        return result
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
# --- Rota de login --------------------------------------------------------------
@router.post("/login", response_model=dict)

# --- Autentica um usuário e retorna JWT token -----------------------------------
async def login(
    user_create: UserCreate,  # Reutiliza schema (email + password)
    db: Session = Depends(get_db),
) -> dict:
    
    try:
        # --- Criar service e repository --- #
        user_repository = UserRepository(db)
        auth_service = AuthService(user_repository)
        
        # --- Chamar login --- #
        result = auth_service.login(user_create.email, user_create.password)
        
        return result
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )
    





    