# Kovir Cash — Contexto do Projeto

## O que é
API REST + Frontend para gerenciar lançamentos financeiros (receitas/despesas) com autenticação, paginação e filtros. Escopo MVP, produção-grade.

## Stack
- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2.x, Pydantic v2, PostgreSQL 16, Alembic
- **Frontend:** React 19, TypeScript, Vite, Tailwind CSS
- **DevOps:** Docker, Docker Compose, GitHub Actions, pytest + Vitest

## Modelo de dados

### Tabela: users
```
id (UUID, PRIMARY KEY)
email (VARCHAR, UNIQUE)
password_hash (VARCHAR) - bcrypt
created_at (TIMESTAMP)
```

### Tabela: lancamentos
```
id (UUID, PRIMARY KEY)
user_id (UUID, FOREIGN KEY → users.id, CASCADE)
tipo (ENUM: receita, despesa)
categoria (ENUM: salário, alimentação, transporte, saúde, outro)
descricao (VARCHAR, NOT NULL)
valor (DECIMAL(10,2), > 0)
data (DATE, ≤ hoje)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
```

## API Endpoints

### Autenticação
- `POST /auth/login` → Retorna JWT (access_token, expires_in: 86400s)
- `POST /auth/logout` → Invalida token

### Lançamentos (CRUD)
- `GET /lancamentos` → Listagem paginada com filtros (skip, limit, data_inicio, data_fim, categoria)
- `POST /lancamentos` → Criar novo lançamento
- `PUT /lancamentos/{id}` → Editar lançamento existente
- `DELETE /lancamentos/{id}` → Deletar lançamento

### Estatísticas
- `GET /stats` → Resumo (total_receita, total_despesa, saldo)

**Nota:** Todos endpoints (exceto login) requerem `Authorization: Bearer <token>`

## Frontend
- Página de login/logout
- Dashboard com lista paginada de lançamentos + filtros (data inicial/final, categoria)
- Form de novo lançamento (validação client-side)
- Edição/deleção de lançamentos
- Gráfico simples (receitas vs despesas por mês)
- Saldo em tempo real

## Validações

### Client-Side (Frontend)
- Email formato válido
- Senha ≥ 8 caracteres
- Valor > 0
- Data não no futuro
- Descrição não vazia
- Tipo e categoria em enum

### Server-Side (Backend)
- Email único no banco
- Senha criptografada com bcrypt
- Valor > 0 (não confia apenas em frontend)
- Data ≤ hoje (não confia apenas em frontend)
- Lançamento pertence ao usuário autenticado (autorização)
- Tipo e categoria válidos (enum)

## Autenticação & Segurança

### JWT (JSON Web Token)
- Access token com validade de 24h
- Header: `Authorization: Bearer <token>`
- Payload contém: user_id, email, iat, exp
- Signature: HS256 (não pode ser alterado sem SECRET_KEY)

### Isolamento de Dados
- Cada usuário vê apenas seus lançamentos
- Queries sempre filtram por `user_id` do token
- Edição/deleção: verifica se lançamento pertence ao usuário (403 Forbidden se não)

## Padrão Arquitetural

Este projeto segue **Layered Architecture** (Arquitetura em Camadas).

**Para detalhes completos:** Ver `/docs/ARQUITETURA.md`

Resumo das camadas:
- **Routes:** Recebem requisições HTTP, validam formato
- **Services:** Lógica de negócio (regras, cálculos)
- **Repositories:** Acesso ao banco de dados (queries)
- **Models:** Definição das tabelas (SQLAlchemy ORM)
- **Schemas:** Validação Pydantic (entrada/saída)

## Testes
- Backend: pytest (unitários + integração com banco de teste)
- Frontend: Vitest + Testing Library (componentes principais)
- CI: GitHub Actions rodando testes na PR

## Deploy
- Docker Compose para dev
- API roda em `localhost:8000`, Frontend em `localhost:5173`
- Swagger automaticamente em `/docs`
- `.env.example` com variáveis necessárias

## Critério de "pronto"
- ✅ Roda localmente com `docker-compose up`
- ✅ Testes passando (pytest + Vitest)
- ✅ CRUD funcional em produção (banco real, não in-memory)
- ✅ Autenticação JWT funcionando
- ✅ README com screenshots e "como rodar"
- ✅ Git com histórico limpo
- ✅ Nenhum secret hardcoded (use .env)

## Documentação

- `/docs/ARQUITETURA.md` — Padrão arquitetural, estrutura de pastas, endpoints detalhados, fluxos de usuário
- `/docs/kovir-cash-context.md` — Este arquivo (contexto geral)
- `/PROJETO_LOG.md` — Log de todas as ações e decisões tomadas
- `/README.md` — Como rodar o projeto (será criado)

## Próximas etapas (depois do MVP)
- Multitenancy (RLS no PostgreSQL)
- Export para CSV/PDF
- Categorias customizadas por usuário
- Recorrência de lançamentos
- Relatórios avançados

## Status do Projeto

**Sessão 1:**
- ✅ Repositório GitHub criado
- ✅ Estrutura de pastas (backend, frontend, docs)
- ✅ .gitignore configurado com entendimento
- ✅ Arquitetura documentada completamente
- ✅ Conceitos sênior de BD e API aprendidos
- ⏳ Código em desenvolvimento
