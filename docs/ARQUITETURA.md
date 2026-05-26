# Arquitetura - Kovir Cash

## 1. Visão Geral

**O que é:** API REST + Frontend para gerenciar lançamentos financeiros (receitas/despesas).

**Objetivo:** Permitir que usuários autenticados criem, leiam, atualizem e deletem lançamentos com filtros e paginação.

**Stack:**
- Backend: FastAPI + SQLAlchemy + PostgreSQL
- Frontend: React + TypeScript + Vite + Tailwind CSS
- DevOps: Docker, Docker Compose

## 2. Padrão Arquitetural: Layered Architecture

### O que é?

Layered Architecture separa o código em camadas horizontais, cada uma com responsabilidade específica:

ROUTES (recebe requisições HTTP)
  ↓
SERVICES (lógica de negócio, regras)
  ↓
REPOSITORIES (acessa banco de dados)
  ↓
MODELS (define estrutura dos dados)

### Por que essa escolha?

1. **Separação de Responsabilidades**
   - Cada camada faz UMA coisa bem
   - Fácil entender o código

2. **Testabilidade**
   - Você testa cada camada isoladamente
   - Mais fácil mockar (simular) dados

3. **Manutenção**
   - Mudança no banco? Muda só em repositories/
   - Mudança na lógica? Muda em services/

4. **Padrão Conhecido**
   - Recrutadores reconhecem
   - Indústria usa bastante

### Alternativas Consideradas

- Clean Architecture: Mais complexa, melhor para projetos gigantes
- Domain-Driven Design: Melhor para negócios complexos
- Monolítica simples: Sem separação, fica bagunçado rápido

Decisão: Layered é equilibrada para projeto pequeno com escalabilidade.

## 3. Estrutura de Pastas

### Backend - Estrutura Completa

backend/
├── app/
│   ├── routes/                 (PORTÕES DE ENTRADA - recebe requisições HTTP)
│   │   ├── __init__.py
│   │   ├── auth.py             → POST /login, POST /logout
│   │   └── lancamentos.py      → GET/POST/PUT/DELETE /lançamentos
│   │
│   ├── services/               (CÉREBRO - lógica de negócio, regras)
│   │   ├── __init__.py
│   │   ├── auth_service.py  → Valida senha, gera JWT, logout
│   │   └── lancamento_service.py → Cria, edita, valida lançamentos
│   │
│   ├── repositories/           (GUARDIÕES DO BANCO - SQL queries)
│   │   ├── __init__.py
│   │   ├── user_repo.py        → SELECT/INSERT/UPDATE na tabela users
│   │   └── lancamento_repo.py  → SELECT/INSERT/UPDATE na tabela lancamentos
│   │
│   ├── models/                 (ESTRUTURA NO BANCO - definem tabelas)
│   │   ├── __init__.py
│   │   ├── user.py             → Tabela users (id, email, password_hash, created_at)
│   │   └── lancamento.py       → Tabela lancamentos (id, user_id, tipo, valor, data, descricao)
│   │
│   ├── schemas/                (VALIDADORES - checam entrada antes de processar)
│   │   ├── __init__.py
│   │   ├── user_schema.py       → Valida: email único, senha ≥ 8 chars
│   │   └── lancamento_schema.py → Valida: valor > 0, data não futura, tipo válido
│   │
│   ├── __init__.py
│   └── config.py               (CONFIGURAÇÕES - lê .env)
│
├── main.py                     (INICIAR AQUI - cria app FastAPI e monta rotas)
├── requirements.txt            (DEPENDÊNCIAS - pip install -r requirements.txt)
├── .env.example                (EXEMPLO - copia para .env e preenche valores)
└── .gitignore                  (já criado)

### Frontend - Estrutura Completa

frontend/
├── src/
│   ├── components/             (BLOCOS REUTILIZÁVEIS - componentes React)
│   │   ├── LoginForm.tsx       → Formulário de login (email + senha)
│   │   ├── LancamentoForm.tsx  → Formulário criar/editar lançamento
│   │   ├── LancamentoList.tsx  → Lista com paginação e filtros
│   │   └── NavBar.tsx          → Barra de navegação (logout, usuário)
│   │
│   ├── pages/                  (TELAS COMPLETAS - cada página é uma rota)
│   │   ├── LoginPage.tsx       → Tela de login (mostra LoginForm)
│   │   └── DashboardPage.tsx   → Tela principal (lista, filtros, criar)
│   │
│   ├── services/               (COMUNICA COM API - chamadas HTTP)
│   │   └── api.ts              → fetch/axios: POST /login, GET /lançamentos, etc
│   │
│   ├── hooks/                  (LÓGICA REUTILIZÁVEL - custom React hooks)
│   │   └── useAuth.ts          → Gerencia login, logout, token JWT
│   │
│   ├── types/                  (TIPAGEM TypeScript - interfaces/tipos)
│   │   └── index.ts            → interface User, interface Lancamento, etc
│   │
│   ├── App.tsx                 (RAIZ - monta rotas e componentes principais)
│   └── main.tsx                (INICIAR AQUI - monta React no HTML)
│
├── index.html                  (HTML base - React monta aqui)
├── package.json                (DEPENDÊNCIAS - npm install)
├── vite.config.ts              (CONFIG VITE - bundler)
├── tsconfig.json               (CONFIG TypeScript)
└── .env.example                (EXEMPLO - copia para .env: VITE_API_URL=...)

### Visualização Completa

kovir-cash/
├── backend/                    (API FastAPI)
├── frontend/                   (React + TypeScript)
├── docs/
│   ├── ARQUITETURA.md          (Este arquivo)
│   └── kovir-cash-context.md   (Contexto do projeto)
├── PROJETO_LOG.md              (Log de todas as ações)
├── README.md                   (Como rodar o projeto)
├── docker-compose.yml          (Vai criar depois)
└── .gitignore                  (Já criado)

## 4. Modelo de Dados

### Tabelas do PostgreSQL

#### Tabela: users

Armazena informações de usuários cadastrados.

Colunas:
- id (UUID) → Identificador único do usuário
- email (VARCHAR) → Email único, não pode repetir
- password_hash (VARCHAR) → Senha criptografada com bcrypt (NUNCA senha em texto puro)
- created_at (TIMESTAMP) → Data/hora que criou a conta

Exemplo:
  id: 550e8400-e29b-41d4-a716-446655440000
  email: rafael@example.com
  password_hash: $2b$12$abcdef...xyz
  created_at: 2026-05-26 10:30:00

#### Tabela: lancamentos

Armazena receitas e despesas de cada usuário.

Colunas:
- id (UUID) → Identificador único do lançamento
- user_id (UUID) → FK para users.id (qual usuário criou)
- tipo (ENUM) → 'receita' ou 'despesa'
- categoria (ENUM) → 'salário', 'alimentação', 'transporte', 'saúde', 'outro'
- descricao (VARCHAR) → Descrição (ex: "Salário de maio")
- valor (DECIMAL) → Valor em dinheiro, SEMPRE > 0
- data (DATE) → Data do lançamento, NÃO pode ser futura
- created_at (TIMESTAMP) → Quando criou
- updated_at (TIMESTAMP) → Última alteração

Exemplo:
  id: 660e8400-e29b-41d4-a716-446655440001
  user_id: 550e8400-e29b-41d4-a716-446655440000
  tipo: receita
  categoria: salário
  descricao: Salário de maio 2026
  valor: 5000.00
  data: 2026-05-26
  created_at: 2026-05-26 11:00:00
  updated_at: 2026-05-26 11:00:00

### Relacionamentos

users (1) ──── (N) lancamentos

Um usuário pode ter MUITOS lançamentos.
Um lançamento pertence a EXATAMENTE UM usuário.

Quando deleta usuário, seus lançamentos também deletam (CASCADE).

### Validações no Banco

- email: Único, formato válido
- password_hash: Sempre bcrypt, nunca texto puro
- valor: SEMPRE > 0 (não pode ser negativo ou zero)
- data: NÃO pode ser no futuro (máximo hoje)
- tipo: Apenas 'receita' ou 'despesa'
- categoria: Apenas valores da enum

### Estrutura Visual do Banco

kovir-cash (Database PostgreSQL)
├── Schema: public
│   ├── Table: users
│   │   ├── id (UUID, PK)
│   │   ├── email (VARCHAR, UNIQUE)
│   │   ├── password_hash (VARCHAR)
│   │   └── created_at (TIMESTAMP)
│   │
│   └── Table: lancamentos
│       ├── id (UUID, PK)
│       ├── user_id (UUID, FK → users.id)
│       ├── tipo (ENUM: receita | despesa)
│       ├── categoria (ENUM: salário | alimentação | transporte | saúde | outro)
│       ├── descricao (VARCHAR)
│       ├── valor (DECIMAL > 0)
│       ├── data (DATE ≤ hoje)
│       ├── created_at (TIMESTAMP)
│       └── updated_at (TIMESTAMP)

Legendas:
PK = Primary Key (identificador único)
FK = Foreign Key (referencia outra tabela)
ENUM = Apenas valores pré-definidos
UNIQUE = Não pode repetir
VARCHAR = Texto
DECIMAL = Número com casas decimais
TIMESTAMP = Data e hora
DATE = Apenas data

## 5. Endpoints da API

### Autenticação

POST /auth/login
  Descrição: Fazer login com email e senha
  Entrada: { email, password }
  Saída: { access_token, token_type, expires_in }
  Exemplo: POST /auth/login
    Entrada: { "email": "rafael@example.com", "password": "123456" }
    Resposta: { "access_token": "eyJhbGc...", "token_type": "bearer", "expires_in": 86400 }

POST /auth/logout
  Descrição: Fazer logout (invalidar token)
  Requer: Authorization: Bearer <token>
  Saída: { message: "Logout realizado" }

### Lançamentos (CRUD)

GET /lancamentos
  Descrição: Lista lançamentos do usuário autenticado (com paginação e filtros)
  Requer: Authorization: Bearer <token>
  Query params: skip=0, limit=10, data_inicio=2026-01-01, data_fim=2026-05-26, categoria=salário
  Saída: { total, items: [...], page, pages }
  Exemplo:
    GET /lancamentos?skip=0&limit=10&categoria=salário
    Resposta: { "total": 5, "items": [{id, tipo, valor, descricao, data}, ...], "page": 1, "pages": 1 }

POST /lancamentos
  Descrição: Criar novo lançamento
  Requer: Authorization: Bearer <token>
  Entrada: { tipo, categoria, descricao, valor, data }
  Saída: { id, user_id, tipo, categoria, descricao, valor, data, created_at }
  Exemplo:
    POST /lancamentos
    Entrada: { "tipo": "receita", "categoria": "salário", "descricao": "Salário maio", "valor": 5000, "data": "2026-05-26" }
    Resposta: { "id": "660e8400...", "user_id": "550e8400...", "tipo": "receita", ... }

PUT /lancamentos/{id}
  Descrição: Editar lançamento existente
  Requer: Authorization: Bearer <token> + usuário dono do lançamento
  Entrada: { tipo, categoria, descricao, valor, data }
  Saída: { id, user_id, tipo, categoria, descricao, valor, data, updated_at }

DELETE /lancamentos/{id}
  Descrição: Deletar lançamento
  Requer: Authorization: Bearer <token> + usuário dono do lançamento
  Saída: { message: "Lançamento deletado" }

### Estatísticas

GET /stats
  Descrição: Resumo financeiro (total receita, total despesa, saldo)
  Requer: Authorization: Bearer <token>
  Query params: data_inicio=2026-01-01, data_fim=2026-05-26
  Saída: { total_receita, total_despesa, saldo }
  Exemplo:
    GET /stats?data_inicio=2026-01-01&data_fim=2026-05-26
    Resposta: { "total_receita": 10000, "total_despesa": 3000, "saldo": 7000 }

### Códigos de Resposta HTTP

200 OK → Sucesso, dados retornados
201 Created → Recurso criado com sucesso
204 No Content → Sucesso, sem dados (DELETE)
400 Bad Request → Dados inválidos (email sem @, valor negativo, etc)
401 Unauthorized → Token inválido ou expirado
403 Forbidden → Usuário não tem permissão (deletar lançamento de outro)
404 Not Found → Recurso não existe
500 Internal Server Error → Erro do servidor

## 6. Fluxos de Usuário

### Flow 1: Login

Usuário abre o Kovir Cash
  ↓
Vê página de login (email + senha)
  ↓
Digita email: rafael@example.com
Digita senha: MinhaSenha123
  ↓
Clica em "Entrar"
  ↓
Frontend: POST /auth/login
  { "email": "rafael@example.com", "password": "MinhaSenha123" }
  ↓
Backend:
  1. Procura usuário com esse email em users
  2. Valida se email existe
  3. Valida se senha está correta (bcrypt)
  4. Gera token JWT
  ↓
Resposta: { "access_token": "eyJhbGc...", "expires_in": 86400 }
  ↓
Frontend: Salva token em localStorage
  ↓
Redireciona para Dashboard
  ↓
✅ Usuário logado!

Possíveis erros:
  400: Email ou senha vazios
  401: Email inexistente ou senha errada
  500: Erro na API

---

### Flow 2: Criar Lançamento

Usuário está no Dashboard
  ↓
Clica em "Novo Lançamento"
  ↓
Abre formulário com campos:
  - Tipo (receita/despesa)
  - Categoria (salário/alimentação/transporte/saúde/outro)
  - Descrição
  - Valor
  - Data
  ↓
Preenche e clica "Salvar"
  ↓
Frontend valida:
  ✓ Descrição não vazia
  ✓ Valor > 0
  ✓ Data não no futuro
  ✓ Tipo é receita ou despesa
  ✓ Categoria é válida
  ↓
Se válido:
  POST /lancamentos
    Authorization: Bearer eyJhbGc...
    {
      "tipo": "receita",
      "categoria": "salário",
      "descricao": "Salário maio",
      "valor": 5000.00,
      "data": "2026-05-26"
    }
  ↓
Backend:
  1. Valida token JWT (está autenticado?)
  2. Extrai user_id do token
  3. Valida dados novamente (server-side)
  4. Insere na tabela lancamentos
  5. Retorna lançamento criado
  ↓
Resposta: { "id": "660e8400...", "user_id": "550e...", "tipo": "receita", ... }
  ↓
Frontend: Atualiza lista (mostra novo lançamento)
  ↓
✅ Lançamento criado!

Possíveis erros:
  400: Dados inválidos (valor negativo, data futura)
  401: Token inválido/expirado
  500: Erro ao salvar no banco

---

### Flow 3: Listar e Filtrar Lançamentos

Usuário abre Dashboard
  ↓
Vê lista de lançamentos com filtros:
  - Data inicial
  - Data final
  - Categoria
  - Paginação (página atual, limite por página)
  ↓
Digita filtros e clica "Filtrar"
  ↓
Frontend: GET /lancamentos
    Authorization: Bearer eyJhbGc...
    ?skip=0&limit=10&data_inicio=2026-01-01&data_fim=2026-05-26&categoria=salário
  ↓
Backend:
  1. Valida token
  2. Extrai user_id do token
  3. Consulta banco: SELECT * FROM lancamentos WHERE user_id = ? AND ... (filtros)
  4. Aplica paginação (skip 0, limit 10)
  5. Conta total de resultados
  ↓
Resposta:
  {
    "total": 5,
    "items": [
      { "id": "660...", "tipo": "receita", "valor": 5000, "data": "2026-05-26", ... },
      { "id": "661...", "tipo": "despesa", "valor": 50, "data": "2026-05-25", ... },
      ...
    ],
    "page": 1,
    "pages": 1
  }
  ↓
Frontend: Mostra lista filtrada
  ↓
✅ Dados carregados!

Possíveis erros:
  400: Filtros inválidos (data mal formatada)
  401: Token inválido

---

### Flow 4: Editar Lançamento

Usuário está na lista
  ↓
Clica em lançamento para editar
  ↓
Abre formulário pre-preenchido com valores atuais
  ↓
Muda algo (ex: valor de 5000 para 5500)
  ↓
Clica "Salvar"
  ↓
Frontend valida dados novamente
  ↓
PUT /lancamentos/660e8400-e29b-41d4-a716-446655440001
    Authorization: Bearer eyJhbGc...
    {
      "tipo": "receita",
      "categoria": "salário",
      "descricao": "Salário maio - revisado",
      "valor": 5500.00,
      "data": "2026-05-26"
    }
  ↓
Backend:
  1. Valida token
  2. Extrai user_id do token
  3. Verifica se lançamento com ID 660... existe
  4. Verifica se pertence a user_id (é do usuário autenticado?)
  5. Atualiza campos
  ↓
Resposta: { "id": "660...", "valor": 5500.00, "updated_at": "2026-05-26 14:30:00", ... }
  ↓
✅ Lançamento atualizado!

Possíveis erros:
  400: Dados inválidos
  401: Token inválido
  403: Tentando editar lançamento de outro usuário
  404: Lançamento não existe

---

### Flow 5: Deletar Lançamento

Usuário está na lista
  ↓
Clica em botão "Deletar" do lançamento
  ↓
Confirmação: "Tem certeza? Não dá para desfazer."
  ↓
Clica "Sim, deletar"
  ↓
Frontend:
  DELETE /lancamentos/660e8400-e29b-41d4-a716-446655440001
    Authorization: Bearer eyJhbGc...
  ↓
Backend:
  1. Valida token
  2. Extrai user_id
  3. Verifica se lançamento existe
  4. Verifica se pertence ao usuário
  5. Deleta do banco
  ↓
Resposta: { "message": "Lançamento deletado" } (204 No Content)
  ↓
Frontend: Remove da lista
  ↓
✅ Lançamento deletado!

Possíveis erros:
  401: Token inválido
  403: Tentando deletar lançamento de outro
  404: Lançamento não existe

---

### Flow 6: Ver Estatísticas

Usuário abre Dashboard
  ↓
Vê cards com resumo:
  - Total Receita: R$ 10.000,00
  - Total Despesa: R$ 3.000,00
  - Saldo: R$ 7.000,00
  ↓
(Opcional: Pode filtrar por período)
  ↓
Frontend: GET /stats
    Authorization: Bearer eyJhbGc...
    ?data_inicio=2026-01-01&data_fim=2026-05-26
  ↓
Backend:
  1. Valida token
  2. Extrai user_id
  3. Soma todos lancamentos com tipo='receita' do user_id
  4. Soma todos lancamentos com tipo='despesa' do user_id
  5. Calcula: saldo = receita - despesa
  ↓
Resposta:
  {
    "total_receita": 10000.00,
    "total_despesa": 3000.00,
    "saldo": 7000.00
  }
  ↓
Frontend: Mostra cards com valores
  ↓
✅ Estatísticas atualizadas!

---

### Flow 7: Logout

Usuário clica em "Sair"
  ↓
(Opcional: POST /auth/logout)
  ↓
Frontend: Remove token de localStorage
  ↓
Redireciona para página de login
  ↓
✅ Sessão encerrada!