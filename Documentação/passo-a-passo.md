# 🐾 Patas&Páginas — Guia Prático de Execução

> **Para quem é esse documento?** Para você, Matheus, que já sabe o "porquê" do projeto (leia o `manual.md` e o `regras_de_negocio.md` para isso), mas precisa saber **o que fazer hoje, amanhã e na próxima semana** sem se perder.

---

## 📍 Onde você está agora (Diagnóstico)

Antes de saber para onde ir, precisamos saber onde estamos. Com base na análise do projeto:

| Item | Status | Observação |
|---|---|---|
| README e documentação base | ✅ Feito | Muito bem documentado |
| Regras de negócio | ✅ Feito | `regras_de_negocio.md` completo |
| Manual técnico | ✅ Feito | `manual.md` detalhado |
| Repositório Git | ✅ Ativo | `.git` e `.gitignore` presentes |
| Ambiente virtual Python | ✅ Criado | Pasta `.venv` presente |
| Projeto Django iniciado | ✅ Feito | `manage.py` e apps criadas |
| Apps Django (`cafeteria`, `livraria`, `papelaria`) | ✅ Criadas | Estrutura base gerada |
| App `core` criada | ✅ Feito (04/05) | `python manage.py startapp core` |
| Model `Produto` + `TipoProduto` | ✅ Feito (04/05) | `core/models.py` |
| Model `Livro` | ✅ Feito (04/05) | `livraria/models.py` |
| Model `Papelaria` | ✅ Feito (04/05) | `papelaria/models.py` (bugs corrigidos) |
| Models `CafeInsumo`, `ReceitaDiretaAoCliente`, `ReceitaItem` | ✅ Feito (04/05) | `cafeteria/models.py` |
| `core` registrado em `INSTALLED_APPS` | ✅ Feito (04/05) | `settings.py` |
| `livraria/urls.py` criado | ✅ Feito (04/05) | Arquivo vazio, a ser preenchido com DRF |
| `patas_paginas/urls.py` atualizado | ✅ Feito (04/05) | Rotas `/api/livros/` e `/api/cafe/` |
| **`makemigrations` e `migrate`** | ⏳ **Pendente** | Erros corrigidos, rodar novamente |
| DER (Diagrama Entidade-Relacionamento) | ⏳ Em andamento | `der.md` iniciado |
| Banco de dados PostgreSQL | ❌ Não configurado | Usando SQLite3 temporário (OK por ora) |
| Django REST Framework (DRF) | ❌ Não instalado | Próxima etapa |
| Frontend React | ❌ Não iniciado | Fase 4 |
| Docker | ❌ Não configurado | Fase 6 |

**Conclusão atual (04/05/2026):** Fase 2 em andamento. Todos os models estão escritos. Falta rodar as migrações com sucesso e registrar no Admin para validar.

---

## 🗺️ O Caminho a Seguir (Visão Geral)

```
[✅ FEITO] Fase 1: Documentação e Regras de Negócio
   ↓
[🔄 EM ANDAMENTO] Fase 2: Modelagem do Banco de Dados
   → Models escritos ✅
   → makemigrations/migrate ⏳
   → Registrar no Admin e testar ⏳
   ↓
[PRÓXIMA] Fase 3: Backend Django (API com DRF)
   ↓
Fase 4: Frontend React
   ↓
Fase 5: Segurança e Testes
   ↓
Fase 6: Deploy
```

---

## ✅ FASE 2 — Modelagem do Banco de Dados

> **Objetivo:** Transformar o que você escreveu no `regras_de_negocio.md` em tabelas reais no banco de dados usando Django ORM.

### Passo 1 — Desenhar o DER (Diagrama Entidade-Relacionamento)

**Por que fazer isso ANTES de escrever código?** Porque mudar um campo no banco depois de ter dados reais é trabalhoso e arriscado. O DER é o "mapa" que evita isso.

**Como fazer:**
1. Acesse **[dbdiagram.io](https://dbdiagram.io)** (gratuito, funciona no navegador).
2. Modele as seguintes tabelas com base nas regras de negócio já documentadas:
   - `Produto` (tabela base — id, nome, sku, preco_venda, preco_custo, estoque, tipo)
   - `Livro` (OneToOne com Produto — isbn, autor, editora, paginas)
   - `Papelaria` (OneToOne com Produto — cor, marca)
   - `CafeInsumo` (OneToOne com Produto — unidade_medida, data_validade)
   - `Receita` (para produtos compostos como "Café Expresso")
   - `ReceitaItem` (ingredientes de cada receita — qual insumo e quanto usa)
   - `Pedido` (cabeçalho da venda — data, status, total)
   - `PedidoItem` (os produtos de cada pedido — produto, quantidade, preco_unitario)
3. Valide seu diagrama perguntando a si mesmo: *"Consigo registrar uma venda com 1 livro + 2 cadernos + 1 café macchiato, e o estoque de leite é abatido corretamente?"*

**Entregável:** Um screenshot ou link do DER salvo na pasta `/Documentação`.

---

### Passo 2 — Criar o app `core` e escrever os Models ✅ CONCLUÍDO (04/05/2026)

Com o DER como referência, os models foram criados em quatro arquivos.

#### 2a. Criar o app `core`

```bash
# Dentro da pasta backend/
python manage.py startapp core
```

Depois registrar em `settings.py`:
```python
INSTALLED_APPS = [
    # ... apps existentes ...
    'core',  # ← adicionado
]
```

> ⚠️ **Lição aprendida:** Toda app nova precisa estar em `INSTALLED_APPS`. Se esquecer, o Django lança `RuntimeError: Model class ... doesn't declare an explicit app_label`.

#### 2b. `core/models.py` — A tabela base compartilhada

```python
from django.db import models

class TipoProduto(models.TextChoices):
    LIVRO = 'livro', 'Livraria'
    PAPELARIA = 'papelaria', 'Papelaria'
    CAFE_INSUMO = 'cafe_insumo', 'Insumo de Café'
    CAFE_RECEITA = 'cafe_receita', 'Receita de Café'
    CAFE_DIRETO = 'cafe_direto', 'Venda Direta de Café'

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.DecimalField(max_digits=10, decimal_places=3)
    tipo = models.CharField(max_length=20, choices=TipoProduto.choices)
    is_composicao = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
```

#### 2c. `livraria/models.py` — Tabela filha de Livros

```python
from django.db import models
from core.models import Produto

class Livro(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='livro')
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    paginas = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.autor})"
```

#### 2d. `papelaria/models.py` — Tabela filha de Papelaria

```python
from django.db import models
from core.models import Produto

class Papelaria(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='papelaria')
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.marca})"
```

> 🐛 **Bugs corrigidos neste arquivo:**
> - `related_name='livro'` copiado da livraria → corrigido para `'papelaria'` (cada `related_name` deve ser único)
> - `self.produto.marca` → corrigido para `self.marca` (o campo `marca` está em `Papelaria`, não em `Produto`)

#### 2e. `cafeteria/models.py` — Insumos, Receitas e Ingredientes

```python
from django.db import models
from core.models import Produto

class CafeInsumo(models.Model):
    """Ingredientes físicos: Leite, Pó de Café, etc. Não vendidos diretamente."""
    class UnidadeMedida(models.TextChoices):
        GRAMAS = 'g', 'Gramas'
        MILILITROS = 'ml', 'Mililitros'
        UNIDADE = 'un', 'Unidade'

    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='cafe_insumo')
    unidade = models.CharField(max_length=2, choices=UnidadeMedida.choices)
    data_validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.unidade})"


class ReceitaDiretaAoCliente(models.Model):
    """Produto composto vendido ao cliente (ex: Café Macchiato)."""
    produto_final = models.OneToOneField(
        Produto, on_delete=models.CASCADE, related_name='receita',
        limit_choices_to={'is_composicao': True}
    )
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Receita: {self.produto_final.nome}"


class ReceitaItem(models.Model):
    """Cada ingrediente de uma receita. Ex: 15g de pó de café → Macchiato."""
    receita = models.ForeignKey(ReceitaDiretaAoCliente, on_delete=models.CASCADE, related_name='itens')
    insumo = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='usado_em_receitas')
    quantidade = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return f"{self.quantidade} de {self.insumo.nome} → {self.receita.produto_final.nome}"
```

> 🐛 **Bug corrigido:** Nome da classe foi alterado de `Receita_Direta_Ao_Cliente` (snake_case inválido para classes Python) para `ReceitaDiretaAoCliente` (PascalCase correto). O `ForeignKey` em `ReceitaItem` também precisou ser atualizado para o novo nome.

#### 2f. Rodar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

> ⚠️ **Importante:** Por enquanto, o banco é SQLite3 (`db.sqlite3`). OK para desenvolvimento. Será trocado por PostgreSQL na Fase 5.

---

### Passo 3 — Registrar no Django Admin

O Django Admin é uma interface web automática para gerenciar os dados. É útil para testar rapidamente se seus models funcionam.

```python
# backend/livraria/admin.py
from django.contrib import admin
from .models import Livro

admin.site.register(Livro)
```

**Para acessar o admin:**
```bash
# Crie um superusuário (só precisa fazer uma vez)
python manage.py createsuperuser

# Suba o servidor
python manage.py runserver

# Acesse no navegador: http://127.0.0.1:8000/admin
```

**O que testar no Admin:**
- Criar um `Produto` do tipo "Livro"
- Criar um `Livro` vinculado a esse produto
- Criar um `Produto` do tipo "Café Receita" com `is_composicao=True`
- Criar os itens da receita desse café

---

## ✅ FASE 3 — Backend: A API com Django REST Framework

> **Objetivo:** Transformar seus models em rotas de API que o frontend React poderá consumir.

### Passo 4 — Instalar o Django REST Framework (DRF)

```bash
# Com o ambiente virtual ativo
pip install djangorestframework

# Atualizar o arquivo de dependências
pip freeze > requirements.txt
```

Adicione ao `settings.py`:
```python
INSTALLED_APPS = [
    # ... apps existentes ...
    'rest_framework',
]
```

---

### Passo 5 — Criar Serializers

Serializers são os "tradutores" entre seus objetos Python e o formato JSON da API.

```python
# backend/livraria/serializers.py (arquivo novo)
from rest_framework import serializers
from .models import Livro
from core.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = Livro
        fields = '__all__'
```

---

### Passo 6 — Criar Views e URLs da API

```python
# backend/livraria/views.py
from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
```

```python
# backend/livraria/urls.py
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)

urlpatterns = router.urls
```

**Testar a API:**
- Suba o servidor: `python manage.py runserver`
- Acesse: `http://127.0.0.1:8000/api/livros/`
- A API navegável do DRF vai aparecer. Você pode criar, editar e deletar livros por ela.

---

### Passo 7 — Implementar Autenticação JWT

> Este é o ponto de aprendizado de **segurança** do projeto.

```bash
pip install djangorestframework-simplejwt
pip freeze > requirements.txt
```

Adicione ao `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

**O que você vai aprender aqui:**
- Como um token JWT é gerado (login) e validado (em cada requisição)
- Por que tokens em `HttpOnly Cookies` são mais seguros que no `localStorage`
- Como proteger rotas da API para que só usuários logados acessem

---

### Passo 8 — Implementar o Fluxo de Venda (PDV)

Esta é a parte mais complexa e importante do projeto do ponto de vista de **banco de dados**.

**O que você vai aprender:**
- Transações atômicas com `transaction.atomic()` — se qualquer etapa falhar, tudo é revertido (rollback)
- Como fazer uma operação que mexe em várias tabelas ao mesmo tempo de forma segura

```python
# Exemplo conceitual do fluxo de venda
from django.db import transaction

@transaction.atomic
def finalizar_venda(pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    
    for item in pedido.itens.all():
        produto = item.produto
        
        if produto.is_composicao:
            # Abate estoque dos insumos da receita
            for ingrediente in produto.receita_itens.all():
                insumo = ingrediente.insumo
                insumo.estoque -= ingrediente.quantidade_gasta * item.quantidade
                insumo.save()
        else:
            # Abate estoque direto
            produto.estoque -= item.quantidade
            produto.save()
    
    pedido.status = 'finalizado'
    pedido.save()
```

---

## ✅ FASE 4 — Frontend React

> Só comece esta fase quando a API estiver funcional e testada.

### Passo 9 — Iniciar o Projeto React

```bash
# Na raiz do projeto Patas_Paginas
npx create-vite@latest frontend --template react
cd frontend
npm install
npm run dev
```

### Passo 10 — Estrutura de Pastas do Frontend

```
frontend/src/
  ├── assets/          # Imagens e ícones
  ├── components/      # Botões, Inputs, Modais (componentes reutilizáveis)
  ├── features/        # Módulos por funcionalidade
  │   ├── auth/        # Login, logout
  │   ├── produtos/    # Listar, criar, editar produtos
  │   └── pdv/         # Tela do caixa/ponto de venda
  ├── pages/           # Telas completas (LoginPage, DashboardPage)
  ├── services/        # Chamadas à API (axios)
  ├── hooks/           # Hooks customizados (useAuth, useProdutos)
  ├── store/           # Estado global (Zustand)
  └── styles/          # CSS global e variáveis
```

### Passo 11 — Conectar Frontend à API (Axios)

```bash
npm install axios
```

```javascript
// frontend/src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  withCredentials: true, // Necessário para Cookies HttpOnly
});

export default api;
```

---

## ✅ FASE 5 — Segurança e Testes

> **O que você vai aprender de segurança nesta fase:**

### Passo 12 — Mover o `SECRET_KEY` para `.env`

Atualmente, o `SECRET_KEY` do Django está **hardcoded no `settings.py`** — isso é um risco de segurança real!

```bash
pip install python-dotenv
```

```python
# backend/patas_paginas/settings.py
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
```

```bash
# backend/.env (já existe na raiz do projeto, mova para o backend)
DJANGO_SECRET_KEY=seu-valor-secreto-aqui
```

> ⚠️ **Verifique se o `.env` está no `.gitignore`!** Se não estiver, adicione agora. Nunca suba segredos para o GitHub.

### Passo 13 — Configurar PostgreSQL

Quando os models estiverem estáveis e você quiser simular um ambiente mais próximo do real:

```bash
pip install psycopg2-binary
```

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

### Passo 14 — Escrever Testes no Django

```python
# backend/livraria/tests.py
from django.test import TestCase
from core.models import Produto, TipoProduto
from .models import Livro

class LivroModelTest(TestCase):
    def test_criar_livro(self):
        produto = Produto.objects.create(
            nome="1984",
            sku="ISBN-001",
            preco_venda=39.90,
            preco_custo=20.00,
            estoque=10,
            tipo=TipoProduto.LIVRO,
        )
        livro = Livro.objects.create(
            produto=produto,
            isbn="978-85-359-0277-5",
            autor="George Orwell",
            editora="Companhia das Letras",
        )
        self.assertEqual(str(livro), "1984 (George Orwell)")
```

```bash
# Rodar os testes
python manage.py test
```

---

## ✅ FASE 6 — Docker e Deploy

> Deixe esta fase para quando o MVP (funcionalidades básicas) estiver funcionando localmente.

### Passo 15 — Dockerizar o Projeto

**`backend/Dockerfile`:**
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

**`docker-compose.yml` (na raiz do projeto):**
```yaml
version: '3.8'
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: patas_paginas
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: senha_segura
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file:
      - ./backend/.env

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    depends_on:
      - backend
```

---

## 📋 Checklist de Progresso

### ✅ Fase 1 — Documentação (Concluída)
- [x] README completo
- [x] Regras de negócio documentadas
- [x] Manual técnico escrito
- [x] Repositório Git inicializado

### 🔄 Fase 2 — Modelagem do Banco (Em andamento)
- [x] DER iniciado (`Documentação/der.md`)
- [x] App `core` criada (`python manage.py startapp core`)
- [x] `core` registrada em `INSTALLED_APPS`
- [x] Model `Produto` e `TipoProduto` escritos em `core/models.py`
- [x] Model `Livro` escrito em `livraria/models.py`
- [x] Model `Papelaria` escrito em `papelaria/models.py`
- [x] Models `CafeInsumo`, `ReceitaDiretaAoCliente`, `ReceitaItem` escritos em `cafeteria/models.py`
- [x] `livraria/urls.py` criado (vazio, aguarda DRF)
- [x] `patas_paginas/urls.py` atualizado com rotas `/api/`
- [ ] **Rodar `makemigrations` e `migrate` com sucesso** ← PRÓXIMO PASSO
- [ ] Registrar models no Django Admin
- [ ] Criar superusuário e testar no Admin

### ⏳ Fase 3 — API com DRF (Não iniciada)
- [ ] Instalar `djangorestframework` e `simplejwt`
- [ ] Criar `Serializers` para cada app
- [ ] Criar `ViewSets` e URLs da API
- [ ] Testar API em `http://127.0.0.1:8000/api/`
- [ ] Implementar autenticação JWT com HttpOnly Cookies
- [ ] Implementar fluxo de venda com `transaction.atomic()`
- [ ] Mover `SECRET_KEY` para `.env`

### ⏳ Fase 4 — Frontend React (Não iniciada)
- [ ] Iniciar projeto com Vite (`npx create-vite@latest frontend --template react`)
- [ ] Estrutura de pastas por features
- [ ] Instalar Axios e configurar `services/api.js`
- [ ] Criar tela de Login conectada ao JWT
- [ ] Criar telas de gestão de produtos
- [ ] Integrar Zustand para estado global do carrinho

### ⏳ Fase 5 — Segurança e Testes (Não iniciada)
- [ ] Configurar PostgreSQL (substituir SQLite)
- [ ] Escrever testes unitários (`python manage.py test`)
- [ ] Blindar API: CORS restrito, validações nos Serializers

### ⏳ Fase 6 — Docker e Deploy (Não iniciada)
- [ ] Criar `backend/Dockerfile`
- [ ] Criar `docker-compose.yml` na raiz
- [ ] Configurar CI/CD com GitHub Actions
- [ ] Deploy em VPS

---

## 🐛 Registro de Bugs e Erros Encontrados

Um histórico do que quebrou e o que foi aprendido com cada erro.

### Sessão 04/05/2026

| Erro | Causa | Solução | Lição |
|---|---|---|---|
| `RuntimeError: Model class core.models.Produto ... isn't in INSTALLED_APPS` | App `core` criada mas não registrada no `settings.py` | Adicionar `'core'` em `INSTALLED_APPS` | Toda nova app Django precisa ser registrada |
| `NameError: name 'Receita_Direta_Ao_Cliente' is not defined` | Classe renomeada mas `ForeignKey` ainda usava o nome antigo | Atualizar a referência no `ForeignKey` também | Python diferencia maiúsculas — renomeou a classe, renomeie **todas** as referências |
| `ModuleNotFoundError: No module named 'livraria.urls'` | `urls.py` referenciado no projeto mas o arquivo não existia | Criar `livraria/urls.py` (vazio por ora) | `include('app.urls')` exige que o arquivo exista, mesmo vazio |
| `related_name='livro'` duplicado em `Papelaria` | Copiar/colar do model `Livro` sem alterar o `related_name` | Corrigir para `related_name='papelaria'` | Cada `related_name` deve ser único em todo o projeto |
| `self.produto.marca` em `Papelaria.__str__` | `marca` é campo de `Papelaria`, não de `Produto` | Corrigir para `self.marca` | Saber onde cada campo vive — no model base ou no filho |

---

## 💡 Dicas de Estudo — Aprenda Enquanto Constrói

| O que você vai construir | O que vai aprender |
|---|---|
| Models do Django | Como funciona um ORM, herança de tabelas, relacionamentos (FK, OneToOne) |
| DER | Normalização de banco de dados, como prevenir dados duplicados |
| Serializers do DRF | Como dados viajam entre Python e JSON, validação de entrada |
| JWT + Cookies HttpOnly | Autenticação segura, diferença entre XSS e CSRF, por que `localStorage` é inseguro |
| `transaction.atomic()` | Propriedades ACID, o que é um rollback, consistência de dados |
| Testes Django | TDD, como escrever testes que valem a pena |
| Docker | Containers, isolamento de ambiente, por que "na minha máquina funciona" não é desculpa |

---

## 🆘 Quando Travar

Se você travar em algum passo, antes de pedir ajuda, tente:
1. Ler a mensagem de erro **completa** — Django é muito descritivo nos erros
2. Procurar no **[Django Docs](https://docs.djangoproject.com/pt-br/5.2/)** — a documentação oficial é excelente e tem versão em português
3. Procurar no **[DRF Docs](https://www.django-rest-framework.org/)** para dúvidas de API

---

*Documento criado em: Maio de 2026 | Projeto: Patas&Páginas | Versão: 1.0*
