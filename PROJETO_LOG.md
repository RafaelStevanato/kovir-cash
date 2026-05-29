# Kovir Cash - Projeto Log

## Data: 26/05/2026

### Ações Realizadas

#### 1. Criação do Repositório GitHub
- **O quê:** Repositório kovir-cash criado em GitHub
- **Opções escolhidas:**
  - Visibilidade: Public
  - README: Adicionado (automático)
  - .gitignore: Não (será criado manualmente)
  - License: Nenhuma (pode ser adicionada depois)
- **Por quê:** Estrutura inicial limpa, documentação desde o início

#### 2. Configuração SSH
- **O quê:** Geração de par de chaves SSH (RSA 4096)
- **Passos:**
  - Gerei chaves em ~/.ssh/id_rsa e ~/.ssh/id_rsa.pub
  - Adicionei chave pública ao GitHub
  - Testei conexão com 'ssh -T git@github.com'
- **Por quê:** SSH é mais seguro que HTTPS, melhor prática profissional

#### 3. Clone do Repositório
- **O quê:** Repositório clonado para C:\Users\Rafael Stevanato\Desktop\GitHub\kovir-cash
- **Comando:** git clone git@github.com:RafaelStevanato/kovir-cash.git
- **Por quê:** Trabalhar localmente com controle de versão

#### 4. Estrutura de Pastas
- **O quê:** Criadas pastas principais (backend, frontend, docs)
- **Comando:** mkdir backend, frontend, docs
- **Por quê:** Organizar código por contexto (separação de responsabilidades)

#### 5. Criação de .gitignore
- **O quê:** Arquivo .gitignore do zero, documentado
- **Seções:** Python, Node/React, Ambiente, SO
- **Por quê:** Evitar commitar arquivos desnecessários/sensíveis (venv/, node_modules/, .env, .DS_Store, etc)

#### 6. Primeiro Commit
- **Comando:** git commit -m "feat: estrutura inicial do projeto com .gitignore e documentação"
- **Hash:** 6a2726e
- **Arquivos:** .gitignore, PROJETO_LOG.md
- **Push:** Sincronizado com GitHub

---

## Status Atual
✅ Repositório criado e clonado
✅ Estrutura básica pronta
✅ .gitignore configurado
✅ Documentação iniciada

#### 7. Aprofundamento em Arquitetura e Conceitos

- **O quê:** Estudo detalhado de:
  - Relacionamentos de banco (1:N)
  - Normalização e Foreign Keys
  - Tipos de dados apropriados (DECIMAL para dinheiro, UUID)
  - Métodos HTTP (GET, POST, PUT, DELETE)
  - Status codes HTTP (401 vs 403)
  - JWT (tokens de autenticação)
  - Validação em 2 camadas (frontend + backend)
  - Isolamento de dados por usuário

- **Conceitos-chave aprendidos:**
  - Separação de responsabilidades entre camadas
  - Segurança: autenticação vs autorização
  - Por que não confiamos apenas em validação frontend
  - Como JWT funciona e por que não pode ser alterado

#### 8. Documento ARQUITETURA.md Completo

- **Seções criadas:**
  1. Visão Geral
  2. Padrão Arquitetural (Layered Architecture)
  3. Estrutura de Pastas (backend e frontend)
  4. Modelo de Dados (tabelas users e lancamentos)
  5. Endpoints da API (7 endpoints principais)
  6. Fluxos de Usuário (7 fluxos: login, criar, listar, editar, deletar, stats, logout)

- **Por quê:** Documentação sólida para entender e apresentar a arquitetura a recrutadores

---

## Resumo do Dia

✅ Repositório criado e sincronizado
✅ Estrutura inicial montada
✅ .gitignore configurado com entendimento
✅ Arquitetura documentada completamente
✅ Conceitos sênior de BD e API aprendidos
✅ 3 commits feitos com histórico limpo

## Próximas Sessões

- [ ] Criar estrutura de pastas do backend (models, routes, services, repositories)
- [ ] Criar estrutura de pastas do frontend (components, pages, services)
- [ ] Começar código: Models + Schemas do backend
- [ ] Configurar banco de dados PostgreSQL local

#### 9. Configuração do Ambiente Virtual (venv)

- **O quê:** Criado venv com Python 3.12 para isolar dependências do projeto
- **Problema encontrado:** Python 3.14 (inicial) tinha incompatibilidade com Pydantic-core (Rust)
- **Solução:** Downgrade para Python 3.12 (estável e production-grade)
- **Passos:**
  1. Deletado venv com Python 3.14
  2. Criado novo venv: `py -3.12 -m venv venv`
  3. Ativado: `.\venv\Scripts\Activate.ps1`
  4. Instaladas dependências: `pip install -r backend/requirements.txt`

#### 10. Instalação de Dependências do Backend

- **O quê:** Todas as dependências do backend foram instaladas com sucesso
- **Mudança no requirements.txt:**
  - `psycopg2-binary` → `psycopg[binary]` (compatibilidade Windows)
  - `pydantic==2.5.0` → `pydantic==2.6.0` (melhor compatibilidade)
- **Status:** ✅ Todas as 19 dependências instaladas com sucesso
- **Próximo passo:** Criar estrutura de pastas e Models do backend

#### 11. Criação de config.py e .env.example

- **O quê:** Arquivo de configurações centralizado da aplicação
- **config.py:** Classe Settings com Pydantic para ler variáveis de ambiente
  - DATABASE_URL
  - SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_HOURS
  - DEBUG
  - class Config interna (lê .env)
  - Instância global `settings`
- **.env.example:** Template com variáveis de exemplo
- **Por quê:** Centralizar configurações, modular por ambiente (dev/test/prod)
- **Status:** ✅ Pronto para ser copiado para .env

#### 12. Criação de backend/main.py (FastAPI básica)

- **O quê:** Arquivo raiz da aplicação que inicia o servidor
- **Conteúdo:**
  - Import FastAPI e settings
  - Criação da instância `app = FastAPI(...)`
  - Rota GET / (health check) que retorna status da aplicação
  - Bloco `if __name__ == "__main__"` para rodar com uvicorn
- **Teste:** `python main.py` → Uvicorn inicia em http://0.0.0.0:8000
- **Validação:** GET http://localhost:8000/ retorna JSON com status ✅
- **Status:** ✅ Pronto para montar as rotas de autenticação

#### 13. Criação de backend/app/models/user.py (primeiro Model SQLAlchemy)

- **O quê:** Definição da tabela 'users' usando SQLAlchemy ORM
- **Campos:**
  - id (UUID, primary key, auto-gerado)
  - email (String, unique, indexed, obrigatório)
  - password (String, obrigatório)
  - criado_em (DateTime, auto-timestamp UTC)
- **Base:** Criada class Base que todos os models herdam
- **Import centralizada:** models/__init__.py exporta User e Base
- **Teste:** `python -c "from app.models.user import User"` ✅
- **Status:** ✅ Pronto para criar o schema Pydantic

#### 14. Criação de backend/app/schemas/user_schema.py (Pydantic validation)

- **O quê:** Schemas para validação de entrada/saída de dados da API
- **Schemas criados:**
  - UserCreate: email (EmailStr) + password (min 8 chars) — o que vem do cliente
  - UserResponse: id + email + criado_em (sem password) — o que retorna da API
- **Config:** Ambos com json_schema_extra para exemplo no Swagger
- **from_attributes:** UserResponse pode converter Model SQLAlchemy direto
- **Dependência:** Atualizado requirements.txt: pydantic[email]==2.6.0
- **Import centralizada:** schemas/__init__.py exporta ambos
- **Teste:** `python -c "from app.schemas.user_schema import..."` ✅
- **Status:** ✅ Pronto para criar as rotas de autenticação

#### 15. Criação de backend/app/repositories/user_repository.py (acesso ao banco)

- **O quê:** Abstração de operações no banco de dados para User
- **Padrão:** Repository isolaça lógica de acesso ao banco
- **Métodos:**
  - `__init__(session)`: inicializa com sessão SQLAlchemy
  - `create_user(email, hashed_password)`: cria user no banco, retorna User com ID gerado
  - `get_user_by_email(email)`: busca user por email, retorna User ou None
- **Benefício:** Se mudar PostgreSQL para MongoDB, muda só aqui, não muda Service/Routes
- **Session:** Recebe Session como injeção de dependência (flexibilidade)
- **Teste:** `python -c "from app.repositories.user_repository import..."` ✅
- **Status:** ✅ Pronto para ser usado pelo Service

#### 16. Criação de backend/app/services/auth_service.py (lógica de autenticação)

- **O quê:** Serviço com lógica de negócio para autenticação
- **Configuração:** CryptContext (bcrypt) para hash seguro de senhas
- **Métodos estáticos:**
  - `hash_password(password)`: hash com bcrypt
  - `verify_password(plain, hashed)`: compara senha com hash
  - `create_access_token(user_id)`: gera JWT com exp 24h (HS256)
- **Métodos com dependência:**
  - `signup(email, password)`: valida email único, hash, cria user, retorna token
  - `login(email, password)`: busca user, valida password, retorna token
- **Segurança:** Mensagens de erro genéricas ("Email ou senha incorretos") em ambos casos
- **Retorno:** {"access_token", "token_type": "bearer", "user": {...}}
- **Teste:** `python -c "from app.services.auth_service import..."` ✅
- **Status:** ✅ Pronto para ser usado pelas rotas

#### 17. Criação de backend/app/routes/auth.py (endpoints de autenticação)

- **O quê:** Rotas HTTP para sign-up e login
- **Router:** APIRouter com prefix="/auth" (rotas em /auth/signup e /auth/login)
- **Endpoints:**
  - POST /auth/signup: cria user, retorna access_token + user
  - POST /auth/login: autentica user, retorna access_token + user
- **Validação:** Schemas Pydantic (UserCreate)
- **Injeção de dependência:** db: Session = Depends(get_db)
- **Erros:** HTTPException 400 (signup) e 401 (login)
- **Status codes:** 201 Created (signup), 200 OK (login)
- **Placeholder:** get_db() vazio por enquanto (será implementado com database.py)
- **Status:** ⏳ Aguardando database.py para estar funcional

#### 18. Criação de backend/app/database.py (conexão com PostgreSQL)

- **O quê:** Gerencia conexão SQLAlchemy com PostgreSQL
- **Conteúdo:**
  - `engine`: create_engine com DATABASE_URL (echo=DEBUG)
  - `SessionLocal`: sessionmaker factory para criar sessions
  - `get_db()`: generator que fornece session (yield) e fecha (finally)
  - `init_db()`: cria todas as tabelas via Base.metadata.create_all()
- **Driver:** psycopg (novo) — DATABASE_URL usa postgresql+psycopg://
- **Dependência:** FastAPI injeta get_db() nas rotas via Depends()
- **Padrão:** Session é criada por requisição, fechada após
- **Teste:** `python -c "from app.database import..."` ✅
- **Status:** ✅ Pronto para ser integrado em main.py

#### 19. Criação de docker-compose.yml (PostgreSQL containerizado)

- **O quê:** Arquivo que define e roda PostgreSQL em Docker
- **Serviços:** postgres:16 (imagem oficial PostgreSQL)
- **Credenciais padrão:** user=postgres, password=postgres, db=kovir_cash
- **Porta:** 5432 (padrão PostgreSQL)
- **Volume:** postgres_data (persiste dados entre `up/down`)
- **Uso:** `docker-compose up` → PostgreSQL rodando em 5s
- **Benefício:** Dev padronizado (qualquer máquina roda igual)
- **Status:** ✅ Pronto para testar conexão da API

---

## Data: 29/05/2026

#### 20. Debug e Resolução - Conflito PostgreSQL Nativo vs Docker

- **O quê:** Resolver erro persistente de autenticação psycopg com PostgreSQL
- **Problema:** API falhava ao iniciar com erro `FATAL: autenticação do tipo senha falhou para o usuário "postgres"`

- **Tentativas Iniciais (4 explorações):**
  1. Credenciais `user:password` → Usuário não criado automaticamente
  2. Usuário `postgres` com SCRAM-SHA-256 → psycopg rejeitava senha
  3. `POSTGRES_HOST_AUTH_METHOD: trust` → Pg_hba.conf não foi atualizado
  4. Forçar `password_encryption=md5` → Ainda falhava

- **Diagnóstico Profundo (O Eureka Moment!):**
  - Executado: `netstat -ano | Select-String 5432`
  - **Resultado:** DOIS processos escutando na porta 5432!
    - PID 18024: `com.docker.backend` (Docker container) ✅
    - PID 8072: `postgres.exe` (PostgreSQL 17 NATIVO no Windows!) ❌
  - **Causa Raiz:** psycopg estava conectando no PostgreSQL nativo do Windows, não no Docker
  - **Por quê:** O PostgreSQL nativo tinha credenciais/configuração diferentes

- **Validações Realizadas:**
  - ✅ Docker Compose: Container up, database criado
  - ✅ Conectividade TCP: `Test-NetConnection localhost:5432` → Success
  - ✅ Conexão direta (psql): `docker exec psql` → Conectava
  - ❌ SQLAlchemy/psycopg: Falhava sempre
  - 🔑 **Insight:** Port aberta ≠ Aplicação correta respondendo!

- **Solução Aplicada:**
  ```powershell
  Stop-Service postgresql-x64-17
  Set-Service postgresql-x64-17 -StartupType Manual
  ```
  - Parou o serviço PostgreSQL nativo do Windows
  - Configurou para não iniciar automaticamente no reboot
  - Liberou porta 5432 exclusivamente para Docker

- **Validação Final:**
  - `netstat` após parar: Apenas PID 18024 (Docker) ✅
  - Teste psycopg direto: `SUCESSO! Conectado ao PostgreSQL Docker` ✅
  - `SELECT version()`: `PostgreSQL 15.18 (Debian 15.18-1.pgdg13+1)` ✅
  - API iniciou sem erros: ✅

- **Lições Críticas Aprendidas:**
  1. **Multiplos processos na mesma porta** → Sempre usar `netstat -ano` ou `Get-Process` para diagnosticar
  2. **Port aberta ≠ Aplicação correta** → Verificar qual processo está realmente escutando
  3. **Ferramentas diferentes, comportamentos diferentes** → `psql` (libpq) vs `psycopg` (Python driver)
  4. **PostgreSQL 16 vs 15** → Mudança de autenticação SCRAM-SHA-256 causou confusão
  5. **Documentação salva vidas** → Criar RELATORIO-DEBUG-POSTGRESQL.md ajudou a organizar pensamento

- **Arquivos Criados Nesta Sessão:**
  - `RELATORIO-DEBUG-POSTGRESQL.md` → Documentação completa do debugging
  - Atualizado `docker-compose.yml` → postgres:15 (compatibilidade melhor)
  - Confirmado `config.py` e `database.py` estão corretos

- **Status:** ✅ API 100% funcional com PostgreSQL 15 Docker
- **Próximo passo:** Testar endpoints no Swagger (GET /, POST /auth/signup, POST /auth/login)

#### 21. Configuração Docker (Dockerfile + docker-compose.yml)

- **O quê:** Criar Dockerfile para empacotar API e atualizar docker-compose.yml com serviço api
- **Criado:** `backend/Dockerfile` (6 linhas: FROM python:3.12 → RUN pip → COPY → CMD uvicorn)
- **Atualizado:** `docker-compose.yml` → adicionado serviço `api` com `build: ./backend`, `ports: 8000:8000`
- **Debug:** 
  - ❌ DATABASE_URL em docker-compose faltava driver `+psycopg` → Corrigido
  - ❌ Host era `localhost` (local) → Mudado para `postgres` (service name em Docker)
  - ✅ Segundo `docker-compose up` → **API RODANDO!** Uvicorn em http://0.0.0.0:8000
  - ✅ SQLAlchemy criou tabela `users` automaticamente via `init_db()`
- **Resultado:** API + PostgreSQL rodando em Docker, containers conectados, volume persistindo dados
- **Status:** ✅ Docker funcional, pronto para commit
