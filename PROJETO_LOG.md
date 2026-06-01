# Kovir Cash — Projeto Log

> Histórico de desenvolvimento organizado em Sprints.
> Cada Sprint tem objetivo claro, logs detalhados e status.
> Formato profissional para apresentação a recrutadores.

---

## ÍNDICE DE SPRINTS

| Sprint | Objetivo | Status |
|--------|----------|--------|
| [Sprint 1](#sprint-1) | Setup e Fundação do Projeto | ✅ Concluída |
| [Sprint 2](#sprint-2) | Arquitetura e Modelagem | ✅ Concluída |
| [Sprint 3](#sprint-3) | Backend Core (Autenticação) | ✅ Concluída |
| [Sprint 4](#sprint-4) | Docker e DevOps | ✅ Concluída |
| [Sprint 5](#sprint-5) | Segurança e Boas Práticas | ✅ Concluída |

---

<a name="sprint-1"></a>
## Sprint 1 — Setup e Fundação do Projeto

**Período:** 26/05/2026
**Objetivo:** Criar repositório, configurar ambiente git e estabelecer estrutura base do projeto.
**Branch:** `main`

---

### Log 1 — Criação do Repositório GitHub

- **O quê:** Repositório kovir-cash criado no GitHub
- **Decisões:**
  - Visibilidade: Public (recrutadores vão ver)
  - README: Adicionado automaticamente
  - .gitignore: Não (criado manualmente para aprender)
  - License: Nenhuma por enquanto
- **Por quê:** Estrutura inicial limpa, documentação desde o início

---

### Log 2 — Configuração SSH

- **O quê:** Geração de par de chaves SSH (RSA 4096)
- **Passos:**
  1. Gerei chaves em `~/.ssh/id_rsa` e `~/.ssh/id_rsa.pub`
  2. Adicionei chave pública ao GitHub
  3. Testei conexão com `ssh -T git@github.com`
- **Por quê:** SSH é mais seguro que HTTPS — melhor prática profissional

---

### Log 3 — Clone do Repositório

- **O quê:** Repositório clonado localmente
- **Comando:** `git clone git@github.com:RafaelStevanato/kovir-cash.git`
- **Destino:** `C:\Users\Rafael Stevanato\Desktop\GitHub\kovir-cash`
- **Por quê:** Trabalhar localmente com controle de versão via SSH

---

### Log 4 — Estrutura de Pastas

- **O quê:** Criadas pastas principais do projeto
- **Estrutura:** `backend/`, `frontend/`, `docs/`
- **Por quê:** Separação de responsabilidades desde o início (backend ≠ frontend)

---

### Log 5 — Criação de .gitignore

- **O quê:** Arquivo `.gitignore` criado do zero com documentação interna
- **Seções:** Python, Node/React, Ambiente, Sistema Operacional
- **Por quê:** Evitar commitar arquivos sensíveis (`venv/`, `node_modules/`, `.env`, `.DS_Store`)

---

### Log 6 — Primeiro Commit

- **Commit:** `6a2726e feat: estrutura inicial do projeto com .gitignore e documentação`
- **Arquivos:** `.gitignore`, `PROJETO_LOG.md`
- **Por quê:** Registrar ponto inicial no histórico do projeto

---

**✅ Sprint 1 Concluída**
- Repositório público no GitHub
- SSH configurado (seguro)
- Estrutura base criada
- Histórico iniciado com commit profissional

---

<a name="sprint-2"></a>
## Sprint 2 — Arquitetura e Modelagem

**Período:** 26/05/2026
**Objetivo:** Desenhar e documentar a arquitetura antes de começar a codar.
**Branch:** `main`

---

### Log 7 — Aprofundamento em Arquitetura e Conceitos

- **O quê:** Estudo detalhado de fundamentos antes de codar
- **Conceitos estudados:**
  - Relacionamentos de banco (1:N entre users e lancamentos)
  - Normalização e Foreign Keys
  - Tipos de dados: `DECIMAL` para dinheiro, `UUID` para IDs
  - Métodos HTTP: GET, POST, PUT, DELETE
  - Status codes: 401 vs 403 (autenticação vs autorização)
  - JWT (tokens de autenticação stateless)
  - Validação em 2 camadas: Schema (formato) + Service (lógica de negócio)
  - Isolamento de dados por usuário (um usuário não vê dados de outro)
- **Decisão de Arquitetura:** Layered Architecture (Route → Service → Repository → Model)
- **Por quê:** Arquitetura pensada antes de codar evita retrabalho. Devs sênior planejam primeiro.

---

### Log 8 — Documento ARQUITETURA.md

- **O quê:** Documentação completa da arquitetura do sistema
- **Seções criadas:**
  1. Visão Geral
  2. Padrão Arquitetural (Layered Architecture)
  3. Estrutura de Pastas (backend e frontend)
  4. Modelo de Dados (tabelas `users` e `lancamentos`)
  5. Endpoints da API (7 endpoints principais)
  6. Fluxos de Usuário (login, criar, listar, editar, deletar, stats, logout)
- **Por quê:** Documentação visível no GitHub mostra maturidade técnica ao recrutador

---

**✅ Sprint 2 Concluída**
- Arquitetura decidida e documentada
- Modelo de dados definido antes de implementar
- Fluxos de usuário mapeados
- Pronto para começar o código com clareza

---

<a name="sprint-3"></a>
## Sprint 3 — Backend Core (Autenticação)

**Período:** 26/05/2026 → 27/05/2026
**Objetivo:** Implementar toda a stack de autenticação (signup + login) seguindo Layered Architecture.
**Branch:** `main`
**Stack:** Python 3.12, FastAPI, SQLAlchemy 2.x, Pydantic v2, bcrypt, JWT

---

### Log 9 — Configuração do Ambiente Virtual (venv)

- **O quê:** Criado venv com Python 3.12 para isolar dependências
- **Problema encontrado:** Python 3.14 tinha incompatibilidade com `pydantic-core` (compilado em Rust)
- **Solução:** Downgrade para Python 3.12 (versão estável e production-grade)
- **Passos:**
  1. Deletado venv com Python 3.14
  2. `py -3.12 -m venv venv`
  3. `.\venv\Scripts\Activate.ps1`
  4. `pip install -r backend/requirements.txt`
- **Lição:** Sempre usar Python LTS em projetos profissionais

---

### Log 10 — Instalação de Dependências do Backend

- **O quê:** Todas as dependências instaladas com sucesso
- **Ajustes no requirements.txt:**
  - `psycopg2-binary` → `psycopg[binary]` (compatibilidade Windows)
  - `pydantic==2.5.0` → `pydantic==2.6.0` (melhor compatibilidade com Python 3.12)
- **Resultado:** ✅ 19 dependências instaladas sem erros

---

### Log 11 — config.py e .env.example

- **O quê:** Arquivo de configurações centralizado usando Pydantic BaseSettings
- **config.py:** Classe `Settings` com:
  - `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_HOURS`, `DEBUG`
  - Lê automaticamente do arquivo `.env`
  - Instância global `settings` (importada em todo o projeto)
- **.env.example:** Template público com variáveis (sem valores reais)
- **Analogia:** `config.py` é o "painel de controle" da aplicação
- **Por quê:** Centralizar configurações facilita mudança entre ambientes (dev/test/prod)

---

### Log 12 — backend/main.py (FastAPI)

- **O quê:** Ponto de entrada da aplicação
- **Conteúdo:**
  - Instância `app = FastAPI(title="Kovir Cash API")`
  - Rota `GET /` (health check)
  - Bloco `if __name__ == "__main__"` para rodar com uvicorn
- **Validação:** `GET http://localhost:8000/` → JSON com status ✅

---

### Log 13 — app/models/user.py (SQLAlchemy ORM)

- **O quê:** Definição da tabela `users` no banco
- **Campos:**
  - `id`: UUID, primary key, auto-gerado
  - `email`: String, unique, indexed
  - `password`: String (hash bcrypt, nunca plain text)
  - `criado_em`: DateTime com timestamp UTC automático
- **Analogia:** Model é o "livro de registros" — define a estrutura da tabela
- **Teste:** `python -c "from app.models.user import User"` ✅

---

### Log 14 — app/schemas/user_schema.py (Pydantic)

- **O quê:** Schemas para validação de entrada/saída da API
- **Schemas:**
  - `UserCreate`: `email` (EmailStr) + `password` (mínimo 8 chars) — o que vem do cliente
  - `UserResponse`: `id` + `email` + `criado_em` (sem password) — o que retorna
- **Lição crítica:** Schema nunca retorna `password` — segurança por design
- **Analogia:** Schema é o "cardápio" — valida o formato do pedido antes de passar ao chef
- **Teste:** `python -c "from app.schemas.user_schema import UserCreate"` ✅

---

### Log 15 — app/repositories/user_repository.py

- **O quê:** Camada de acesso ao banco de dados
- **Métodos:**
  - `create_user(email, hashed_password)` → cria user, retorna User com UUID gerado
  - `get_user_by_email(email)` → busca user, retorna `User | None`
- **Princípio:** Repository recebe Session como injeção de dependência
- **Benefício:** Se mudar PostgreSQL → MongoDB, muda só aqui. Service e Routes não mudam.
- **Analogia:** Repository é o "estoque" — sabe onde estão os ingredientes (dados)
- **Teste:** `python -c "from app.repositories.user_repository import UserRepository"` ✅

---

### Log 16 — app/services/auth_service.py

- **O quê:** Lógica de negócio de autenticação
- **Métodos:**
  - `hash_password(password)` → bcrypt hash
  - `verify_password(plain, hashed)` → compara com hash
  - `create_access_token(user_id)` → JWT com expiração configurável
  - `signup(email, password)` → valida email único → hash → cria user → retorna token
  - `login(email, password)` → busca user → valida senha → retorna token
- **Segurança:** Mensagens de erro genéricas ("Email ou senha incorretos") nos dois casos
- **Por quê:** Erro específico ("email não existe") ajuda atacantes — erro genérico protege
- **Analogia:** Service é o "chef" — recebe pedido validado e executa a lógica real
- **Teste:** `python -c "from app.services.auth_service import AuthService"` ✅

---

### Log 17 — app/routes/auth.py

- **O quê:** Endpoints HTTP de autenticação
- **Endpoints:**
  - `POST /auth/signup` → cria conta → retorna `access_token` (201 Created)
  - `POST /auth/login` → autentica → retorna `access_token` (200 OK)
- **Tratamento de erros:**
  - `ValueError` → `HTTPException 400` (signup) ou `401` (login)
- **Placeholder:** `get_db()` vazio — implementado após `database.py`
- **Analogia:** Route é o "garçom" — recebe pedido do cliente, passa pro chef (Service)

---

### Log 18 — app/database.py (Conexão PostgreSQL)

- **O quê:** Gerenciamento de conexão SQLAlchemy com PostgreSQL
- **Conteúdo:**
  - `engine`: `create_engine` com `DATABASE_URL` e `echo=DEBUG`
  - `SessionLocal`: factory para criar sessions por requisição
  - `get_db()`: generator com `yield` — fornece session e fecha no `finally`
  - `init_db()`: cria todas as tabelas via `Base.metadata.create_all()`
- **Padrão:** Uma session por requisição HTTP, fechada ao final
- **Driver:** `psycopg` (novo driver async-compatible) — URL usa `postgresql+psycopg://`
- **Teste:** `python -c "from app.database import get_db, init_db"` ✅

---

**✅ Sprint 3 Concluída**
- Layered Architecture implementada (Route → Service → Repository → Model)
- Signup e login funcionais
- JWT gerado com bcrypt
- Validação em 2 camadas (Schema + Service)
- Todos os imports testados

---

<a name="sprint-4"></a>
## Sprint 4 — Docker e DevOps

**Período:** 29/05/2026
**Objetivo:** Containerizar a API e o banco de dados. Resolver conflito de portas no ambiente local.
**Branch:** `main`

---

### Log 19 — docker-compose.yml (PostgreSQL containerizado)

- **O quê:** Arquivo que define e roda PostgreSQL em Docker
- **Serviços:** `postgres:16` (imagem oficial)
- **Configurações:** usuário, senha, banco `kovir_cash`
- **Volume:** `postgres_data` — persiste dados entre `up/down`
- **Por quê:** Dev padronizado — qualquer máquina roda igual com um comando

---

### Log 20 — Debug: Conflito PostgreSQL Nativo vs Docker

- **Problema:** API falhava com `FATAL: autenticação do tipo senha falhou`
- **Tentativas sem sucesso:**
  1. Credenciais `user:password` → usuário não criado automaticamente
  2. SCRAM-SHA-256 → psycopg rejeitava
  3. `POSTGRES_HOST_AUTH_METHOD: trust` → pg_hba.conf não atualizado
  4. `password_encryption=md5` → ainda falhava

- **Diagnóstico (o momento "eureka"):**
  ```powershell
  netstat -ano | Select-String 5432
  ```
  **Resultado:** DOIS processos escutando na porta 5432!
  - PID 18024: `com.docker.backend` (Docker ✅)
  - PID 8072: `postgres.exe` (PostgreSQL 17 NATIVO no Windows ❌)

  **Causa raiz:** psycopg conectava no PostgreSQL nativo, não no Docker.

- **Solução:**
  ```powershell
  Stop-Service postgresql-x64-17
  Set-Service postgresql-x64-17 -StartupType Manual
  ```

- **Validação final:**
  - Apenas Docker escutando na porta 5432 ✅
  - `SELECT version()` → PostgreSQL 15 Docker ✅
  - API iniciou sem erros ✅

- **Lições:**
  1. Porta aberta ≠ aplicação correta respondendo
  2. Sempre usar `netstat -ano` para diagnosticar conflitos de porta
  3. Ferramentas diferentes (psql vs psycopg) podem se comportar diferente
  4. Documentar o processo de debug ajuda a organizar o raciocínio

---

### Log 21 — Dockerfile + docker-compose.yml atualizado

- **O quê:** Containerizar a API junto com o banco
- **Criado:** `backend/Dockerfile`
  ```
  FROM python:3.12-slim
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
  ```
- **Adicionado ao docker-compose.yml:** serviço `api` com `build: ./backend`, `ports: 8000:8000`
- **Bugs encontrados e corrigidos:**
  - `DATABASE_URL` sem `+psycopg` no driver → corrigido
  - Host `localhost` → `postgres` (nome do serviço Docker)
- **Resultado:** API + PostgreSQL rodando juntos em Docker ✅
- **Commit:** `daf7de5 feat: adicionar backend/Dockerfile para empacotamento da API em Docker`

---

**✅ Sprint 4 Concluída**
- API containerizada no Docker
- PostgreSQL em container com volume persistente
- Conflito de portas diagnosticado e resolvido
- `docker-compose up` sobe tudo com um comando

---

<a name="sprint-5"></a>
## Sprint 5 — Segurança e Boas Práticas

**Período:** 31/05/2026
**Objetivo:** Remover credenciais hardcoded, externalizar para `.env`, documentar práticas de segurança e incorporar fluxo profissional (branches, PRs, sprints) nas instruções do projeto.
**Branch:** `main`

---

### Log 22 — Externalizar credenciais para .env

- **Problema identificado:** `config.py` tinha `DATABASE_URL` e `SECRET_KEY` com valores reais hardcoded
- **Risco:** Qualquer um com acesso ao repositório público poderia ver as credenciais
- **O quê foi feito:**
  - Removidos valores hardcoded de `config.py`
  - Adicionado `Field(..., description="...")` com descrições em português
  - Criado `backend/.env` local (nunca commitado — está no `.gitignore`)
  - Padronizado `backend/.env.example` (template público sem valores reais)
  - Corrigido typo: `ACCES_TOKEN_EXPIRE_HOURS` → `ACCESS_TOKEN_EXPIRE_HOURS`
- **Validação:** `python -c "from app.config import settings; print(settings.DATABASE_URL)"` → valor correto ✅
- **Commit:** `9a7521c security: externalizar credenciais sensíveis para .env`

---

### Log 23 — Remover credenciais hardcoded do docker-compose.yml

- **Problema identificado:** `docker-compose.yml` tinha `POSTGRES_USER`, `POSTGRES_PASSWORD` e `DATABASE_URL` com valores fixos
- **O quê foi feito:**
  - `DATABASE_URL: "postgresql+psycopg://..."` → `DATABASE_URL: ${DATABASE_URL}`
  - `POSTGRES_USER: postgres` → `POSTGRES_USER: ${POSTGRES_USER}`
  - `POSTGRES_PASSWORD: postgres` → `POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}`
  - Adicionadas `POSTGRES_USER` e `POSTGRES_PASSWORD` ao `backend/.env`
- **Princípio:** docker-compose lê automaticamente o `.env` na raiz
- **Commit:** `bbb4986 security: remover credenciais hardcoded de docker-compose.yml`

---

### Log 24 — Criar docs/SECURITY.md

- **O quê:** Guia completo de segurança para o projeto
- **Conteúdo:**
  - Diferença entre `.env` (privado) e `.env.example` (template público)
  - Passo a passo de configuração do ambiente
  - Como gerar `SECRET_KEY` segura para produção
  - Checklist de segurança
  - Referências: 12-factor app, OWASP
- **Por quê:** Recrutador vê que além de implementar segurança, você documenta para outros
- **Commit:** `d996c10 docs: adicionar SECURITY.md com guia de configuração de variáveis de ambiente`

---

### Log 25 — Fluxo profissional nas instruções de desenvolvimento

- **O quê:** Seção `[FLUXO PROFISSIONAL - GITHUB & GIT]` adicionada a `docs/INSTRUCOES-CLAUDE-CODE.md`
- **Conteúdo adicionado:**
  - Padrão de branches (`feature/*`, `security/*`, `bugfix/*`, `hotfix/*`)
  - Conventional Commits com tipos e exemplos reais
  - Template profissional de Pull Request
  - Estrutura de Sprint (planejamento → desenvolvimento → review)
  - Checklist de Code Review
  - O que recrutadores veem no GitHub
  - Passo a passo para aplicar na próxima feature
- **Por quê:** Trabalhar como um profissional requer pensar como um profissional
- **Commit:** `6b0b515 docs: adicionar fluxo profissional (branches, PRs, sprints) às instruções de desenvolvimento`

---

**✅ Sprint 5 Concluída**
- Zero credenciais hardcoded no repositório
- `.env` local e nunca commitado
- `.env.example` como template público
- Segurança documentada em SECURITY.md
- Fluxo profissional documentado nas instruções
- 4 commits profissionais no histórico

---

## STATUS GERAL DO PROJETO

| Camada | Componente | Status |
|--------|-----------|--------|
| Config | `config.py` + `.env` | ✅ Seguro |
| Model | `user.py` | ✅ Pronto |
| Schema | `user_schema.py` | ✅ Pronto |
| Repository | `user_repository.py` | ✅ Pronto |
| Service | `auth_service.py` | ✅ Pronto |
| Route | `auth.py` | ✅ Pronto |
| Database | `database.py` | ✅ Pronto |
| DevOps | `Dockerfile` + `docker-compose.yml` | ✅ Funcional |
| Segurança | `.env` + `SECURITY.md` | ✅ Documentado |
| Docs | `ARQUITETURA.md` + `SECURITY.md` | ✅ Completo |

---

---

<a name="sprint-6"></a>
## Sprint 6 — Testes Unitários (EM PROGRESSO)

**Período:** 31/05/2026
**Objetivo:** Implementar testes unitários para AuthService usando pytest.
**Branch:** `main`

---

### Log 26 — Estrutura de testes e testes básicos para AuthService

- **O quê:** Criada estrutura de testes com pytest e 3 testes para métodos de senha
- **Passos:**
  1. Criada pasta `backend/tests/` com `__init__.py`
  2. Criado `backend/tests/test_auth_service.py` com 3 testes:
     - `test_hash_password()` → valida que senha é hasheada (nunca salva em texto puro)
     - `test_verify_password_correct()` → valida que senha correta retorna True
     - `test_verify_password_wrong()` → valida que senha errada retorna False
  3. Configurado `.env` na raiz do projeto (necessário para pytest rodar)
  4. Executado `pytest backend/tests/test_auth_service.py -v` → **3/3 testes passando** ✅
- **Aprendizado:** Testes unitários isolam e validam cada método sem precisar rodar a API inteira
- **Por quê:** Recrutador vê: "Sabe TDD, código confiável, pronto pra trabalhar em equipe"

### Log 27 — Refatoração de config.py (Pydantic 2.6+ best practices)

- **O quê:** Atualizado `config.py` para usar `SettingsConfigDict` (forma nova recomendada)
- **Mudança:**
  - ❌ Antes: classe `Config` interna (deprecada)
  - ✅ Agora: `model_config = SettingsConfigDict(...)` (Pydantic 2.6+)
- **Importes atualizadas:** `from pydantic_settings import SettingsConfigDict`
- **Resultado:** Warning do Pydantic desapareceu, código alinhado com best practices
- **Por quê:** Código limpo e futuro-proof (Pydantic 3.0 removerá forma antiga)

---

**✅ Sprint 6 Parcialmente Concluída**
- 3 testes básicos funcionando
- Estrutura de testes pronta para adicionar mais testes (signup/login)
- Config.py refatorado para Pydantic 2.6+
- Próximas features terão testes desde o início

## PRÓXIMAS SPRINTS (BACKLOG)

| Sprint | Objetivo | Prioridade |
|--------|----------|-----------|
| Sprint 6 | Testes unitários (pytest) para AuthService | 🔴 Alta |
| Sprint 7 | CI/CD com GitHub Actions | 🟡 Média |
| Sprint 8 | Feature: Lançamentos (CRUD completo) | 🔴 Alta |
| Sprint 9 | Frontend React + TypeScript | 🟡 Média |
| Sprint 10 | Integração Frontend ↔ Backend | 🟡 Média |
