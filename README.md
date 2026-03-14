# 📚☕🖊️ Sistema de Gestão — Cafeteria, Livraria & Papelaria

Sistema web desenvolvido com **Django** para gerenciamento integrado de três estabelecimentos: cafeteria, livraria e papelaria. O projeto segue a arquitetura padrão de múltiplos apps do Django, com cada estabelecimento encapsulado em seu próprio módulo independente.

---

## 🗂️ Estrutura do Projeto

```
backend/
├── patas_paginas/          # App principal (core do projeto)
├── cafeteria/              # App do módulo de cafeteria
├── livraria/               # App do módulo de livraria
├── papelaria/              # App do módulo de papelaria
├── assets/                 # Arquivos estáticos globais
└── manage.py               # Utilitário de linha de comando do Django
```

---

## 📁 App Principal — `patas_paginas/`

Este é o **coração do projeto**. Criado automaticamente pelo Django ao iniciar o projeto, é responsável pelas configurações globais e pelo roteamento central de toda a aplicação.

| Arquivo | Responsabilidade |
|---|---|
| `__init__.py` | Marca o diretório como um pacote Python. Também pode ser usado para configurar o Celery ou outros serviços globais na inicialização. |
| `settings.py` | Centraliza **todas as configurações** do projeto: banco de dados, apps instalados, middlewares, arquivos estáticos, idioma, fuso horário, e variáveis de ambiente. |
| `urls.py` | Define o **roteador principal** da aplicação. Agrega e delega as rotas de cada app através de `include()`, funcionando como o ponto de entrada de todas as URLs. |
| `wsgi.py` | Interface de comunicação entre o Django e servidores web compatíveis com **WSGI** (ex: Gunicorn, uWSGI). Usado em ambientes de produção tradicionais. |
| `asgi.py` | Interface de comunicação para servidores compatíveis com **ASGI** (ex: Daphne, Uvicorn). Necessário para suporte a WebSockets e comunicação assíncrona. |

---

## 📁 Apps de Negócio — `cafeteria/`, `livraria/`, `papelaria/`

Cada um desses diretórios representa um **app Django independente**, responsável por toda a lógica de negócio do seu respectivo módulo. A estrutura interna é idêntica nos três apps:

| Arquivo | Responsabilidade |
|---|---|
| `__init__.py` | Marca o diretório como um pacote Python. Geralmente vazio; necessário para que o Django reconheça o app. |
| `admin.py` | Registra os models no **painel administrativo** do Django (`/admin`). Permite visualizar, criar, editar e excluir registros diretamente pela interface web nativa. |
| `apps.py` | Contém a **classe de configuração** do app (nome, label, configurações específicas). É referenciado em `INSTALLED_APPS` no `settings.py` para registrar o app no projeto. |
| `models.py` | Define as **entidades de banco de dados** (tabelas) usando o ORM do Django. É onde ficam as classes que representam os dados do domínio (ex: `Produto`, `Pedido`, `Livro`, `ItemCafeteria`). |
| `views.py` | Contém a **lógica de negócio e de apresentação**. As views recebem requisições HTTP, interagem com os models, e retornam respostas (HTML via templates, ou JSON via APIs REST). |
| `tests.py` | Centraliza os **testes automatizados** do app: testes unitários de models, testes de views, e testes de integração. Executados com `python manage.py test`. |
| `migrations/` | Pasta gerada automaticamente pelo Django. Armazena o **histórico de alterações do banco de dados** em arquivos versionados, permitindo evoluir o schema com segurança via `makemigrations` e `migrate`. |

---

## ⚙️ Comandos Essenciais

```bash
# Criar e aplicar migrações de banco de dados
python manage.py makemigrations
python manage.py migrate

# Rodar o servidor de desenvolvimento
python manage.py runserver

# Criar superusuário para acessar o painel admin
python manage.py createsuperuser

# Executar os testes automatizados
python manage.py test

# Coletar arquivos estáticos para produção
python manage.py collectstatic
```

---

## 🧱 Tecnologias Utilizadas

- **Python 3.x**
- **Django** — Framework web principal
- **SQLite** (desenvolvimento) / **PostgreSQL** (recomendado para produção)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd backend
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor**
   ```bash
   python manage.py runserver
   ```

6. Acesse em: [http://localhost:8000]

---

## 📌 Observações

- Cada app pode ter seu próprio arquivo `urls.py` para organizar as rotas localmente, sendo incluído no roteador principal em `patas_paginas/urls.py`.
- Recomenda-se utilizar variáveis de ambiente (ex: via `python-decouple` ou `django-environ`) para proteger dados sensíveis como `SECRET_KEY` e credenciais de banco de dados.
- Em produção, defina `DEBUG = False` e configure corretamente o `ALLOWED_HOSTS` no `settings.py`.