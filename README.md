# 🚀 Patas&Páginas

## 📌 Visão Geral

Este projeto consiste em uma aplicação web desenvolvida com o objetivo de gerenciar uma aplicação de cafeteria, livraria e papelaria.

A aplicação foi projetada com foco em:
- Escalabilidade
- Segurança
- Manutenibilidade
- Comercialização (produto final vendável)

---

## 🎯 Objetivo do Projeto

O Patas&Páginas é uma aplicação web focada no gerenciamento unificado de três nichos de negócio distintos, mas integrados: **cafeteria, livraria e papelaria**.

- **Problema que resolve:** A dificuldade de empresas com estoques híbridos (ex: alimentos perecíveis vs. livros com ISBN) gerenciarem seus diferentes produtos e fluxos de caixa em sistemas ou planilhas separadas.
- **Público-alvo:** Proprietários e gerentes de estabelecimentos comerciais que combinam serviços de cafeteria com venda de livros e papelaria.
- **Valor entregue:** Uma solução tecnológica centralizada, rentável e manutenível que otimiza processos comerciais e operacionais, unificando vendas, estoques e controles financeiros em um único sistema, reduzindo desperdícios e aumentando a eficiência.

---

## ⚠️ Status Atual

- [x] Em desenvolvimento inicial
- [ ] MVP
- [ ] Em produção
- [ ] Escalando

---

## 🧠 Arquitetura do Sistema

### 📦 Visão Geral

- **Frontend:** React (JavaScript) + Vanilla CSS (CSS Modules)
- **Backend:** Django (API RESTful)
- **Banco de Dados:** PostgreSQL (Banco único/relacional para garantia ACID)
- **Deploy:** Docker / VPS na Nuvem

### 🧩 Estrutura de Alto Nível


/frontend
/backend
/docs
/docker
/scripts


---

## 🏢 Módulos de Negócio (Estoque Híbrido)

O sistema foi desenhado para lidar com as especificidades de três tipos de estoque, mantendo a consistência em um fluxo unificado de vendas:
- **Cafeteria (Alimentos):** Focado em controle de insumos e composição de receitas, exigindo controle rígido de perdas e validade de produtos perecíveis.
- **Livraria:** Gerenciamento baseado em metadados detalhados de publicações como ISBN, editoras, autores, gêneros e edições.
- **Papelaria:** Controle prático de produtos de revenda padronizados (SKU, marca, cor, modelo e lote).

A convergência ocorre no módulo de **Carrinho de Compras / PDV (Ponto de Venda)** e no **Financeiro**, onde qualquer item - seja ele um livro, um caderno ou gramas de pó de café - é abatido adequadamente no estoque e contabilizado no fluxo de caixa dentro da mesma transação.

---
## 🛠️ Roadmap de Desenvolvimento

### Fase 1 – Levantamento de Requisitos
- Definição de regras de negócio
- Identificação de usuários
- Casos de uso

### Fase 2 – Arquitetura
- Definição de stack
- Modelagem de dados
- Estrutura de pastas

### Fase 3 – Backend
- Criação de APIs
- Autenticação
- Regras de negócio

### Fase 4 – Frontend (React)
- Layout base
- Componentização
- Integração com API

### Fase 5 – Segurança
- Autenticação e autorização
- Proteção contra ataques comuns

### Fase 6 – Testes
- Testes unitários
- Testes de integração

### Fase 7 – Deploy
- CI/CD
- Build e execução
- Monitoramento

---

## 📚 Documentação Obrigatória

Durante o desenvolvimento, devem ser documentados:

- Regras de negócio
- Estrutura de APIs
- Modelagem do banco
- Fluxos de usuário
- Decisões técnicas
- Padrões de código
- Processo de deploy

📁 Pasta recomendada:


/docs
  ├── arquitetura.md
  ├── api.md
  ├── banco.md
  ├── decisoes.md


---

## 💻 Frontend (React)

### 📂 Estrutura recomendada


/src
  ├── components
  ├── pages
  ├── services
  ├── hooks
  ├── contexts
  ├── styles


### 🧩 Boas práticas

- Componentes reutilizáveis
- Separação de lógica e UI
- Uso de hooks customizados
- Controle de estado (Context API ou biblioteca)

### 📦 Sugestões de bibliotecas

- React Router
- Axios
- React Hook Form
- Zod/Yup
- Zustand ou Redux (se necessário)

---

## 🔐 Segurança

### 🔒 Práticas obrigatórias

- Uso de HTTPS
- Tokens JWT seguros
- Hash de senhas (bcrypt)
- Variáveis de ambiente (.env)
- Validação de entrada

### ⚠️ Proteções essenciais

- SQL Injection
- XSS
- CSRF
- CORS configurado corretamente

### 📌 Dados sensíveis

- Nunca versionar segredos
- Uso de .env e .env.example

---

## 🗄️ Banco de Dados

### 📌 Estratégia Definida

- Banco Principal e Único: **PostgreSQL**

### 📊 Justificativa

Lidar simultaneamente com estoques diversificados, transações financeiras do PDV e relacionamentos complexos (Livros -> Autores/Editoras; Insumos -> Receitas) exige forte consistência e atomicidade (ACID). A flexibilidade comum de um banco NoSQL para salvar metadados variáveis foi contornada pelo uso de campos nativos estruturados (JSON/JSONB) no PostgreSQL, mantendo total simplicidade na infraestrutura (já que haverá apenas um banco de dados rodando) sem sacrificar a flexibilidade requisitada para gerir o estoque híbrido do sistema.

---

## 🚀 Deploy e Execução

### 📦 Requisitos

- Python 3.x e Node.js instalados
- Banco de dados configurado
- Variáveis de ambiente definidas

### ⚙️ Passos

bash
git clone <repo>
cd projeto
# Setup do Backend (Django)
cd backend
python -m venv venv
# No Windows use: venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Em outro terminal - Setup do Frontend (React)
cd ../frontend
npm install
npm run dev


### 🐳 Docker 

bash
docker-compose up --build


---

## 🔄 CI/CD 

- Build automático
- Testes automáticos
- Deploy automático

Ferramentas:
- GitHub Actions
- GitLab CI
- Jenkins

---

## 🌍 Ambientes

- Desenvolvimento
- Homologação
- Produção

Cada ambiente deve ter:
- Configurações próprias
- Banco separado
- Variáveis de ambiente

---

## 📈 Monitoramento

- Logs estruturados
- Alertas de erro
- Métricas de uso

Sugestões:
- Sentry
- Grafana
- Prometheus

---

## 🧪 Testes

- Unitários
- Integração
- End-to-end

---

## 📦 Versionamento

- Git Flow ou trunk-based
- Commits semânticos

---

## 📌 Boas Práticas Gerais

- Código limpo
- Documentação atualizada
- Revisão de código (PR)
- Padronização

---

## 📄 Licenciamento

**Licença Proprietária / Comercial**
Sendo o Patas&Páginas um sistema desenvolvido com fins lucrativos voltado a comercialização profissional B2B, todos os direitos são reservados aos autores. O projeto **não possui licença de código aberto (Open Source)**. É estritamente proibida a cópia, distribuição, modificação, engenharia reversa ou o uso comercial não autorizado do código-fonte e de suas documentações atreladas sem o consentimento explícito dos detentores da propriedade intelectual.

---

## 👥 Contribuição

Trata-se de um projeto de software fechado (Closed Source). Contribuições externas de terceiros não são aceitas e o desenvolvimento do produto base é restrito à equipe técnica listada como oficial abaixo e pessoas previamente autorizadas em contrato.

---

## 📞 Contato

Responsáveis pelo projeto:
- Nomes: Eduardo Leite Braz e Matheus Ferreira de Souza
- Email: deveduardobz@gmail.com e mmmatheus.fsouza@gmail.com