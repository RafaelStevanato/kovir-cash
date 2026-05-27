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
