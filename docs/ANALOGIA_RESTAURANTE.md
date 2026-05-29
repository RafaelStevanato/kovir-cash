# 🍽️ Analogia do Restaurante — Kovir Cash

**Instrução para Claude:** Sempre que desenvolvemos o Kovir Cash, use a analogia do restaurante para explicar conceitos de arquitetura.

---

## Mapeamento: Restaurante ↔ Kovir Cash API

| Restaurante | Kovir Cash | Função |
|---|---|---|
| **Cardápio** | **Schema (Pydantic)** | Valida **formato** dos dados (email é string? valor > 0?) |
| **Garçom** | **Route/Endpoint** | Recebe pedido do cliente, valida com cardápio |
| **Chef** | **Service** | Valida **regras de negócio** (email já existe? saldo é suficiente?) |
| **Estoque** | **Repository** | Executa operações no banco (INSERT, SELECT, UPDATE, DELETE) |
| **Livro de Registros** | **Model (SQLAlchemy)** | Define estrutura das tabelas (que colunas, que tipos) |
| **Banco de Dados** | **PostgreSQL** | Armazena dados em disco |

---

## Exemplo Prático: Criar Lançamento (Receita/Despesa)

### 1️⃣ Cliente (Frontend) Pede
```
POST /lancamentos
{
  "tipo": "receita",
  "categoria": "salário",
  "valor": 5000.50,
  "descricao": "Salário mês 5",
  "data": "2025-05-28"
}
```

### 2️⃣ Garçom (Route) Recebe
```python
@app.post("/lancamentos")
async def criar_lancamento(lancamento: LancamentoCreate):
    # Garçom valida com cardápio (Schema)
    # LancamentoCreate diz:
    # - tipo: deve ser "receita" ou "despesa"?
    # - valor: deve ser > 0?
    # - data: não pode ser no futuro?
```

❌ Se erro de formato → "Prato não existe no cardápio!" (400)

### 3️⃣ Chef (Service) Pensa
```python
def criar_lancamento(self, usuario_id, lancamento_create):
    # Chef valida regras de negócio:
    # - "Este usuário existe?"
    # - "A data é válida (não futura)?"
    # - "Categoria existe para este usuário?"
    # - "Valor faz sentido para essa categoria?"
```

❌ Se erro de negócio → "Não posso fazer isso!" (400/422)

### 4️⃣ Estoque (Repository) Executa
```python
def create_lancamento(self, lancamento_data):
    lancamento = Lancamento(**lancamento_data)
    self.session.add(lancamento)
    self.session.commit()
    # Estoque registra no livro
```

### 5️⃣ Livro (Model) Define Estrutura
```python
class Lancamento(Base):
    __tablename__ = "lancamentos"
    
    id = Column(UUID, primary_key=True)
    usuario_id = Column(UUID, ForeignKey("users.id"))
    tipo = Column(String, nullable=False)  # receita ou despesa
    valor = Column(Numeric(10, 2), nullable=False)  # sempre > 0
    data = Column(Date, nullable=False)
```

### 6️⃣ Banco (PostgreSQL) Armazena
```
INSERT INTO lancamentos (id, usuario_id, tipo, valor, data, ...)
VALUES ('550e8400...', '...', 'receita', 5000.50, '2025-05-28', ...)
```

✅ Resposta ao Cliente:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "usuario_id": "...",
  "tipo": "receita",
  "categoria": "salário",
  "valor": 5000.50,
  "descricao": "Salário mês 5",
  "data": "2025-05-28",
  "criado_em": "2025-05-28T10:30:00"
}
```

---

## Quando Usar Qual Camada?

### Pergunta: "Valor não pode ser negativo"

- **Schema?** ✅ `valor: float = Field(gt=0)` — é validação de **formato**
- **Service?** ❌ Service não entra aqui (já foi bloqueado no Schema)

---

### Pergunta: "Despesa não pode ser maior que renda do mês"

- **Schema?** ❌ Schema não sabe sobre renda (não tem esse contexto)
- **Service?** ✅ Service consulta Repository, vê renda, valida — é **regra de negócio**

---

### Pergunta: "Categoria salário só funciona para receitas"

- **Schema?** ✅ Parcialmente (validação de enum)
- **Service?** ✅ Melhor aqui! (regra: "se tipo=despesa, categoria ≠ salário")

---

## Checklist: Onde Colocar Cada Validação?

| Validação | Camada | Por quê |
|---|---|---|
| Email é string válido? | Schema | Formato de dados |
| Email tem @ e .com? | Schema | Formato de dados |
| Email já existe? | Service | Regra de negócio |
| Senha tem 8+ caracteres? | Schema | Formato de dados |
| Valor > 0? | Schema | Formato de dados |
| Valor não viola limite mensal? | Service | Regra de negócio |
| Data é hoje ou passado? | Service | Regra de negócio |
| Tipo é "receita" ou "despesa"? | Schema | Formato de dados |
| Categoria existe? | Service | Regra de negócio |

---

## Resumo Para Lembrar

> **Schema = Cardápio** (o que é PERMITIDO)
> 
> **Service = Chef** (o que FAZ SENTIDO)
> 
> **Repository = Estoque** (o que EXECUTA)

Se não souber onde colocar validação, pense:

- **Pergunta o cardápio?** → Schema
- **Pergunta a regra do restaurante?** → Service
- **Pergunta ao livro de estoque?** → Repository

---

**Use essa analogia TODA VEZ que explicar arquitetura do Kovir Cash.** 🍽️