# Segurança - Kovir Cash

## Variáveis de Ambiente (.env)

### O que é .env?

Arquivo local (não commitado) que armazena credenciais e configurações sensíveis.

### .env vs .env.example

|      Arquivo   |              | O quê |              | Commit? |

| `.env`         | Valores REAIS (user, pass, secrets) | ❌ NÃO |
| `.env.example` | Template com PLACEHOLDERS           | ✅ SIM |

### Como configurar

1. Copie .env.example para .env

2. Preencha valores reais em backend/.env:
   DATABASE_URL=postgresql+psycopg://postgres:senha_real@localhost:5432/kovir_cash
   SECRET_KEY=sua-chave-secreta-gerada
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=senha_real
   ACCESS_TOKEN_EXPIRE_HOURS=24
   DEBUG=true

3. NUNCA commita .env (está em .gitignore)

## Gerar SECRET_KEY Segura

Execute: python -c "import secrets; print(secrets.token_urlsafe(32))"

Copie o resultado e cole em .env como SECRET_KEY

## Checklist de Segurança

- [ ] .env criado em backend/.env
- [ ] .env NÃO está commitado
- [ ] .env está em .gitignore
- [ ] .env.example é um template (sem senhas reais)
- [ ] SECRET_KEY é único e aleatório
- [ ] DATABASE_URL tem driver +psycopg
- [ ] Não há credenciais em config.py
- [ ] Não há credenciais em docker-compose.yml

## Referências

- 12-factor app - Config: https://12factor.net/config
- OWASP - Secrets Management

