
# 1. Visão geral do projeto

**Resumo do projeto:** O Patas&Páginas é uma aplicação web multiplataforma focada no <gerenciamento unificado> de três nichos de negócio distintos, mas integrados: cafeteria, livraria e papelaria. O sistema é voltado para controle comercial e operacional desses setores.

**Objetivo principal:** Prover uma solução tecnológica rentável e manutenível que permita a empresas gerenciarem vendas, estoque integrado e fluxo de caixa de produtos diversificados (alimentos, livros e itens de papelaria) em um único sistema, otimizando processos e reduzindo desperdícios.

### Decisões e Definições Fundamentais do Projeto:

- **Escopo do Produto:** Solução mercadológica direcionada para empresas que agrupam espaços de cafeteria, livraria e papelaria. O foco é solucionar as dores do gerenciamento de estoques com naturezas distintas (perecíveis vs dados editoriais vs SKUs genéricos) rodando em um fluxo de caixa ou PDV unificado.
- **Stack Tecnológica Consolidada:** O backend utiliza a stack Django/Python (API), com banco de dados central e único em PostgreSQL, servindo um painel Frontend escrito em React. Toda a orquestração e deploy priorizam o uso de Docker.
- **Convergência de Domínios:** O modelo de negócio assume que as regras de negócio de cada estoque se mantêm isoladas nas pontas, porém todas desembocam sem gargalos numa única transação via Carrinho de Compra / Ponto de Venda (PDV).
- **Licenciamento:** Software Proprietário / Venda Comercial (Código Fechado B2B), garantindo inteira e exclusiva propriedade intelectual aos autores.

# 2. Roadmap profissional de desenvolvimento

Abaixo, a trilha sequencial para garantir que o software seja entregue com qualidade Enterprise.

### Fase 1: Levantamento e Refinamento de Requisitos

- **Objetivo:** Definir com exatidão o software antes de escrever código.
- **Entregáveis:** Documento de Requisitos (Funcionais e Não Funcionais), Casos de Uso, Matriz de Perfis (RBAC).
- **Prioridades:** Escopar apenas o necessário para a v1.0 (MVP) para chegar mais rápido ao mercado.
- **Dependências:** Nenhuma.
- **Boas práticas:** Fazer entrevistas com possíveis clientes reais (donos de cafeterias/papelarias).
- **Erros a evitar:** Tentar criar todas as funcionalidades na primeira versão (Ex: começar com sistema de fidelidade complexo antes de faturar vendas simples).

### Fase 2: Definição de Arquitetura e Modelagem

- **Objetivo:** Fixar tecnologias, infraestrutura em nuvem e desenhar o banco de dados.
- **Entregáveis:** DER (Diagrama de Entidade-Relacionamento), diagrama de arquitetura AWS/GCP, repositórios criados com CI inicial.
- **Prioridades:** Modelar corretamente o estoque híbrido.
- **Boas práticas:** Normalização do banco de dados para evitar anomalias de atualização.
- **Erros a evitar:** Acoplar o banco de dados diretamente ao front-end. O intermediário (API) é inegociável.

### Fase 3: Backend (A API Central)

- **Objetivo:** Criar o motor que lidará com a lógica do negócio de forma segura.
- **Entregáveis:** API RESTful ou GraphQL documentada (ex: Swagger), rotas de gestão de inventário e vendas.
- **Dependências:** Fase 2 concluída.
- **Boas práticas:** Arquitetura em camadas (Controllers, Services, Repositories). Retornar códigos HTTP precisos.
- **Erros a evitar:** Lógicas de faturamento dispersas nos controllers; devem ficar isoladas em "services".

### Fase 4: Frontend (A Face do Produto)

(Detalhado na seção 4)

### Fase 5: Autenticação, Autorização e Segurança

(Detalhado na seção 5)

### Fase 6: Testes e Validação

- **Objetivo:** Prevenir que falhas cheguem ao cliente, o que mancharia o produto comercialmente.
- **Entregáveis:** Cobertura de testes de pelo menos 70% da lógica de negócios.
- **Boas práticas:** Testes unitários para regras de cálculo (ex: cálculo de troco, unificação de carrinhos); Testes de E2E (Cypress/Playwright) para o fluxo principal de venda.
- **Erros a evitar:** Gastar tempo testando frameworks de prateleira ou bibliotecas de terceiros; teste o "seu" código.

### Fase 7: Deploy, Observabilidade e Manutenção

(Detalhado na seção 6)

# 3. Pontos que devem ser acompanhados e documentados

Uma aplicação comercial exige a pasta `/docs` muito bem alimentada. Cada item tem o seguinte motivo:

- **Regras de negócio:** Como funciona o abatimento do estoque ao vender um café? (Essencial para não haver falhas financeiras).
- **Requisitos funcionais e não-funcionais:** Documentar metas como "A API deve consultar um livro em < 200ms" garante clareza no acordo comercial.
- **Decisões de arquitetura (ADRs):** Por que usar Django (Python) no backend centralizado em vez de microsserviços Node? Se o CTO mudar, o histórico justifica a base técnica.
- **Padrões de código e convenções de pastas:** Evita código com estilos divergentes, agiliza a entrada de novos desenvolvedores (onboarding).
- **APIs e contratos:** Via Swagger/OpenAPI. O frontend necessita disso para não ser bloqueado pela equipe backend.
- **Modelagem de banco:** Dicionário de dados; sem isso, ninguém além de quem criou o banco sabe como cruzar um Autor com uma Compra.
- **Autenticação e permissões:** Tabela de quem pode fazer o que (Caixa vs Gerente vs Admin).
- **Critérios de aceite:** O que define que a tarefa está "pronta" e faturável.
- **Processo de Deploy e Rollback:** Como colocar no ar e, se o sistema explodir às 22h numa sexta-feira, o passo a passo exato para reverter para a versão anterior.
- **Logs e monitoramento:** Para cobrar do provedor caso os servidores caiam, e resolver falhas silenciosas antes que os clientes percebam.

# 4. Melhor abordagem para o frontend em React/JavaScript

Para montar o painel de gerenciamento, a robustez é prioritária sobre o design "artístico".

**Estrutura de pastas recomendada:** Utilizar "Feature-Sliced Design" (agrega por módulos) ou organização por tipo. Estrutura profissional:

```text
/src
  ├── /assets        # Imagens e ícones
  ├── /components    # Componentes burros/UI (Botão, Input, Modal)
  ├── /features      # Lógicas agrupadas (ex: /inventory, /sales, /auth)
  ├── /pages         # Agrupamento das features em telas roteáveis
  ├── /services      # Integração via Axios/Fetch API
  ├── /hooks         # Hooks reutilizáveis (ex: useAuth)
  ├── /store         # Estado global (Zustand ou Context)
  ├── /styles        # Regras de CSS global / Variáveis HSL
  └── /utils         # Conversores de moeda, datas, etc.
```

- **Layout e Design System:** Como requisitado o uso de Vanilla CSS, crie um arquivo global de Design Tokens usando variáveis nativas `var(--color-primary)`. Abordagem recomendada: CSS Modules (`styles.module.css`). Isso garante controle absoluto, carregamento minificado e sem risco de colisão de classes nativas de CSS.
- **Gerenciamento de estado:**
  - **Estado do servidor (dados vindos das APIs):** Opcionalmente use React Query (TanStack Query) para lidar com cache inteligente, loading states e deduplicação de requests. (Altamente Recomendado)
  - **Estado do cliente (dark mode, carrinho voador temporário):** Zustand (é leve e limpo, substitui o verboso Redux).
- **Formulários e validações:** Gerenciar inventário requer muitos forms. Use React Hook Form aliado ao Zod para garantir validações fortes antes do request sair do front.
- **Comunicação com API:** Centralizar chamadas Axios usando os interceptors. Dessa forma, se o seu token expirar, todo o sistema pode deslogar e ir para o login ou tentar reciclar o token silenciosamente em apenas um lugar.
- **Escalabilidade (Crescimento):** Fazer Code Splitting nas rotas. A área da cafeteria não deve baixar os códigos da área de relatórios financeiros até que o gerente clique nela. Use React.lazy.

# 5. Segurança da informação

**Obrigatório desde o início (Baseado em riscos owasp):**

- **Variáveis de ambiente (.env):** Nunca faça commit de chaves AWS, Banco ou JWT Secret no Git.
- **Autenticação Segura:** Senhas devem usar hashing unidirecional pesado como Argon2 ou bcrypt.
- **Tokens JWT por Cookies (Essencial):** Tokens salvos no localStorage do React são facilmente roubados por XSS. O padrão comercial de defesa é usar Cookies configurados como HttpOnly, Secure e SameSite=Strict.
- **Proteção de SQL Injection / NoSQL Injection:** Usar um ORM robusto (ex: Prisma, TypeORM, Sequelize) em vez de concatenar queries na mão.
- **CORS rigoroso:** Configurar o backend para aceitar requisições APENAS do domínio oficial do painel frontend do seu cliente.

**Deve entrar no Roadmap/Fases futuras:**

- **Rate Limiting:** Evitar ataques de exaustão e botnets nas rotas de Login (bloquear após X tentativas). Pode ser implementado no servidor/API depois do MVP rodar.
- **LGPD:** Mecanismo de deleção forçada ou anonimização de clientes do sistema após encerramento do contrato. Criptografia no banco de dados para dados altamente sensíveis de clientes da livraria.
- **Auditoria de Entidades:** Tabelas com histórico ("Quem alterou o preço do livro Y"). Opcional no MVP, obrigatório no faturamento.

# 6. Preparação para deploy e execução no servidor

O repositório estará no GitHub. Pensando no deploy profissional e sem atritos no seu provedor:

- **Organização e Mono vs Multi Repos:** Se não for usar Monorepo estruturado (via Turborepo/Nx), mantenha o Backend e Frontend em pastas 100% isoladas (`/web` e `/api` respectivamente no seu repo), ou crie repositórios no GitHub distintos.
- **Docker:** Colocar suas aplicações em Containers Docker é a melhor abordagem profissional atual.
  Crie um Dockerfile no front (criando um build estático com Nginx puro) e um Dockerfile no backend.
  Tenha um `docker-compose.yml` que sobe Banco, Front e Back. No servidor a execução será literalmente dar um `git pull` e `docker-compose up -d --build`. Imbatível pela praticidade.
- **Healthcheck:** Rota `/api/health` vital no backend que retorna HTTP 200 OK e tempo de resposta do banco. Útil para scripts de reinício automático.
- **Scripts CI/CD:** Arquivo `.github/workflows/deploy.yml`. O ambiente do GitHub Actions deve automatizar o rodar de testes (`npm run test`) para cada "Pull Request". Só libera o botão verde de merge se o código passar.
- **Variáveis no servidor:** Ter um arquivo `.env.example` mapeando todas as chaves exigidas para que o responsável da infraestrutura crie e injete no servidor antes de plugar o sistema.

# 7. Melhor estratégia de banco de dados

**Recomendação Focada:** Utilize APENAS UM BANCO DE DADOS: PostgreSQL.

- **Por que?** Você está lidando simultaneamente com estoques, vendas (dinheiro/transações financeiras) e relacionamentos (Livros -> Autores/Editoras; Insumos -> Receitas). Isso exige ACIDidade forte (Atomicidade e Consistência).
- **Ausência de Múltiplos Bancos (Abordagem "Boring is Good"):** Não recomendo misturar SQL e NoSQL e criar um ecossistema complexo nesta fase. O PostgreSQL consegue trabalhar com dados JSON complexos nativamente perfeitamente bem caso você precise de flexibilidade, suprindo totalmente a necessidade primária de um NoSQL sem adicionar sobrecarga infraestrutural na manutenção.
- **Vantagens:** Manutenção zero em sincronismo, curva mais baixa, segurança superior das entidades (não corre risco de vender produto esgotado facilmente). Simplicidade que atrai escalabilidade para projetos nascentes.

# 8. Roadmap final consolidado (Guia de Execução)

Este é o plano unificado, da estaca zero de código até você ganhar dinheiro com o software:

1. **Definição de Produto e Documentação Básica (Semana 1):** []
    - Completar lacunas do README (Licença, Stack, Proposta). []
        - **Objetivo:** Ter um documento central que qualquer desenvolvedor possa ler para entender de imediato do que se trata o projeto e regras de negócio essenciais.
        - **Como executar:** Preencha os tópicos em branco do seu README. Defina a licença (ex: Proprietária/Fechada), detalhe as tecnologias escolhidas (Django, React, PostgreSQL) deixando claro o porquê escolheu cada uma.
    - Definir regras do estoque e cruzamento Livraria x Papelaria x Café. []
        - **Objetivo:** Entender como produtos de naturezas completamente diferentes coexistem na mesma base de dados e no mesmo fluxo de venda sem causar caos.
        - **O que considerar nas regras:** 
          - *Livraria:* Produtos focados em edições, número de páginas, ISBN, autores e editoras. Não quebram ou estragam facilmente.
          - *Papelaria:* SKU genérico, cores, marcas (ex: cadernos, canetas). A venda é transacional simples (pegou do estoque e levou).
          - *Café:* Produtos de consumo rápido. Alguns itens são diretos (ex: Lata de refrigerante), outros são compostos (vender um *Café Expresso* requer descontar dezenas de gramas de pó de café do estoque de insulmos e usa também 1 copo descartável).
        - **Como definir cruzamentos na prática:** Documente que sua venda central (o PDV) agrupará tudo no mesmo "carrinho", mas por baixo dos panos precisaremos de um controle de *Polimorfismo*. Todos herdam de uma classe "Produto Base" (preço, quantidade) e detalhes específicos (ISBN pra livro, ou Ingredientes pro Expresso) ficam em tabelas atreladas (Tabela de Herança).
    - Desenhar DER (Diagrama Entidade-Relacionamento) do PostgreSQL para suportar os 3 nichos usando uma base única. 
        - **Objetivo:** Ter um "mapa visual de arquitetura" que demonstre como as tabelas do banco conversam antes que você escreva uma linha de código, prevendo refatorações dolorosas.
        - **Como executar:** Inscreva-se numa ferramenta grátis como draw.io ou dbdiagram.io. Crie relacionalmente as tabelas principais. Faça a si mesmo perguntas provocativas: "Seguindo esse meu mapa, consigo fazer um pedido contendo 1 livro da Agatha Christie, 2 borrachas e cobrar tudo no PIX?". Se a resposta for sim, o DER foi validado.

2. **Setup do Projeto e CI Inicial (Semana 2):** []
    - Configurar repositório estruturado (`/backend` e `/frontend`). []
        - **Objetivo:** Isolar as responsabilidades de infraestrutura (Backend não afeta Frontend) facilitando manutenções e o uso do Git.
        - **Como executar:** No diretório raiz, crie as pastas independentes. Evite misturar arquivos `.json` nativos do Node/React com configurações do Pip/Django lado a lado na raiz. Inicialize repositório no seu GitHub.
    - Configurar Docker local e `docker-compose`.[]
        - **Objetivo:** Garantir que tudo vai rodar de forma idêntica tanto na sua máquina local, quanto no servidor final lá na AWS / DigitalOcean, acabando com a famosa desculpa "Na minha máquina funcionava".
        - **Como executar:** Estude sobre como Docker "isola mini sistemas operacionais (containers)"! Crie um `Dockerfile` na raiz do backend que puxe a imagem de Python. Faça outro `Dockerfile` no frontend no ambiente Node. Finalize criando um `docker-compose.yml` na raiz global do projeto que suba 3 serviços ao mesmo tempo: um container Front, um Back e a base de dados oficial PostgreSQL. 
    - Criar rotina de Linter (ESLint/Prettier).[]
        - **Objetivo:** Padronizar qual estilo de código será gravado nos arquivos limitando subidas de código mal indentado, forçando boas práticas em um projeto profissional.
        - **Como executar:** Na pasta do React instale as regras ESLint. Na pasta do Django configure o formatador `Black`. Caso queira, configure a biblioteca "Husky", que será ativada impedindo dar "git commit" toda vez que o código testado contiver péssimas práticas (Ex: console.log perdidos, espaços desnecessários, variáveis não utilizadas).

3. **Desenvolvimento Central da API em TDD/Backend (Semanas 3 a 5):** []
    - Estabelecer modelagem e integração com PostgreSQL focado no Django ORM nativo. []
        - **Objetivo:** Transportar a matriz e raciocínio pensados no seu desenho do DER lá da Semana 1, em códigos definitivos para as classes Python que moldam o banco.
        - **Como executar:** Nos seus arquivos internos do Django (`models.py`), crie as classes essenciais (`class Livro ProdutoBase`). Analise limitações dos seus campos (`models.CharField`, `models.DecimalField`). Prepare tudo pra rodar a documentação final `manage.py makemigrations`.
    - Criar CRUDS básicos das entidades (Produtos, Usuários).[]
        - **Objetivo:** Dar os "Controles Direcionais" para o software: rotas protegidas que conseguem criar, ler, editar e deletar itens. Sem essas regras básicas, o FrontEnd inteiro não interage com o Banco de modo útil.
        - **Como executar:** Usando a biblioteca "Django Restaurante Framework" (DRF), componha os `Serializers` (Tradutores que intermedeiam Python e JSON) atrelados à suas Views ou ViewSets. Faça isso numa mentalidade "TDD" escrevendo regras automatizadas (`test_produtos.py`) de permissões na API em paralelo, assegurando estabilidade.
    - Implementar rota de Login com Cookies Httponly e RBAC. []
        - **Objetivo:** Proporcionar login robusto onde somente o sistema pode confirmar credenciais autênticas enquanto previne invasões cruzando papeis gerenciais (O que é Controle de Papel Baseado - RBAC).
        - **Como executar:** Configurando uma View baseada em JWT Tokens de verificação via Cookies de Segurança HttpOnly que nem ataques Javascript conseguem visualizar externamente; Depois crie as restrições: "Essa View `Apagar Produto` necessita de classe `IsGerente` ou `IsAdmin`, enquanto a view de listagem não".
    - Construção do fluxo de Pedido/Caixa PDV transacional. []
        - **Objetivo:** Prevenir furos de caixa terríveis da área contábil na jornada do estagiário. Exemplo do risco: "Adicionei o produto à sacola, o estoque reduziu, mas no último segundo o cartão falhou." (Produto some, não houve dinheiro vivo, você tomou prejuízo fantasma).
        - **Como executar:** Trabalhando o bloco atômico no Django `with transaction.atomic():`. Nele tudo deve completar 100% (Gravação contábil, pedido com sucesso, estoque reduzido). Se qualquer variável for recusada ou estourar erro, a operação aborta (faz rollback) revogando toda e qualquer mudança que dependa um do outro em sequência na gravação para impedir estado inconsistente de base de dados.

4. **Construção do Frontend em React (Semanas 6 a 8):** []
    - Montar layout System e Design Tokens em CSS puro/modules visando alta velocidade.[]
        - **Objetivo:** Desenvolver bases visuais estéticas independentes e minimalistas reduzindo dependência de pacotes gulosos, facilitando tempo de render instantâneo aos botões de cliques da sua loja, o que aumenta velocidade.
        - **Como executar:** Configure na pasta raiz `styles` todo seu escopo e paletas principais globalmente como varíaveis (Ex: `:root { --color-primary: x;}`). Mova os estúdios de botões usando CSS Modules isolado em cada componente (`Button.module.css`) impedindo que uma atualização visual do grid de Livros interfira esteticamente nos painéis secundários de Papelarias ou na fonte do Botão Comprar do Café da lateral da sua tela.
    - Integração de Auth com rotas privadas no React Router. []
        - **Objetivo:** Engatar as rotas seguras blindando que acessos anônimos espiem dados da nuvem pela visão local e deslogada, criando experiência contínua segura de um ERP sério.
        - **Como executar:** Elaborando Wrappers em volta do `BrowserRouter/Routes`. Implemente instâncias centralizadas de `<PrivateRoute>` exigindo validações daquele token interno (vindo do Backend) confirmando as credenciais no ato. Se as respostas negarem: Dispare um `Navigate` imperativo enviando à área neutra "/login".
    - Integração completa Zustand + Hook Form para o motor do Painel PDV e dashboards gerenciais. []
        - **Objetivo:** Impedir lentidões infernais na aba da listagem de Caixa (onde múltiplos produtos são imputados num leitor de código de barras a cada segundo na base de dados num carrinho voador pendente antes da aprovação).
        - **Como executar:** Evite prop-drilling cansativo ou o complexo Redux, escolha  **Zustand** para orquestrar "Lojas Temporárias" como variáveis flutuantes para sub-totals contábeis e arrays dos Pedidos-Carinho em cache em toda aplicação React; Associado ao pacote enxuto e escalável  **React Hook Form** lidando com campos dinâmicos pesados no check-out dispensando re-rendering destrutivos na raiz do VDOM do aplicativo principal a toda digitação humana de digitos.

5. **Segurança de Borda e Validações Finais (Semana 9):** []
    - Blindar API contra injeções. []
        - **Objetivo:** Adicionar portas fechadas evitando vulnerabilidades de ataques diretos do lado dos invasores externos para os nossos endpoints protegidos sem aviso prévio.
        - **Como executar:** Não relaxe pois Django Rest cuida quase todo trabalho massivo básico (Proteção de CSRF + SQL), mas você deve assegurar checagens brutas nos Inputs via RegEx minucioso validado pelo lado Serializado para evitar injeção extra. Configure estritas proteções nas políticas CORS definindo somente `http://localhost-front` permitidos.
    - Adicionar criptografia nos arquivos de secrets. []
        - **Objetivo:** Impedir perdas e exposição crítica na conta AWS. Nunca se chumbam (Hardcode) em código variáveis de pagamento que expõem e vazam cartões virtuais numa branch de GitHub que venha estar por algum dia em acesso Aberto sem querer - pois botes interceptam automaticamente na web e cobram de sua conta milhares de reais em criptografia ilícita online, se não cuidados nestes dias sensíveis na engenharia moderna livre.
        - **Como executar:** Consolidando seu `python-dotenv`, arme um arquivo mestre que guardará "apenas variáveis cruciais soltas ali dentro que os botes da Cloud consigam interceptar localmente." Dê o comando claro nas configurações globais `GitIgnore` instrução que nunca envie nada daqueles para Nuvem/Histórico dos Commits (a nuvem lê `.env.example`).
    - Realizar varredura por vazamentos e permissões cruzadas por cargos. []
        - **Objetivo:** Eliminar de vez as brechas lógicas na qual funções secundárias do painel da Papelaria realizem apagamentos no menu Global do Painel que afeta Administradores que são superiores no contrato e não pode ocorrer de baixo escalões de acesso.
        - **Como executar:** Via Jest/PostMan teste intensivo validando que com Token emitidos nas rotas por níveis CAIXA não permitam POST nem PUT nem GET da rota `api/usuarios/admin-deletes/`, retornando falhas 403.

6. **Deploy de Homologação (Staging) (Semana 10):** []
    - Subir ambiente isolado em uma VPS/Cloud usando Docker-Compose via Github Actions manual. []
        - **Objetivo:** Ver o sistema fora da redoma quebra-galho "local computador pessoal", funcionando na nuvem com um servidor independente pronto para acesso global via Ip Externo e testando as transações na AWS sem a pressa irrecuperável de quem faria o mesmissimo direto apontado  do dia de estreia e a arquitetura fizesse sua empresa ir à falência instantanea com base da inatividade geral da mesma que causou perda de dinheiro em clientes ativos e empolgados!
        - **Como executar:** Contrate alugéis num Server (VPV). Acesse o Root Linux interno instale dependências do Docker. Monte a Pipeline CI/CD num gatilhos de evento Workflow local GitHub, ordenando subir cópia do software ativado numa Virtual port "Staging" sem a chance interagir base de dados da original futura para que faça as modificações via Push nas áreas "branch homolgation".
    - Convidar lojistas (clientes de teste) para usar uma versão fake do seu software e procurar gargalos ("Alpha Testing"). []
        - **Objetivo:** Feito exclusivamente para que você descubra comportamentos absurdos criados pelas necessidades humanas onde nenhum log poderia documentar ou o desenvolvedor não saberia modelar. Você acha que as coisas vão rodar simples; e então usuários clicam nos check-out mil vezes criando bug que tu jamais teria clicado 2 vezes testando sozinho antes da subida em nuvem global do Staging - A famosa teoria sobre a Vida testar mais fundo!
        - **Como executar:** Marque papo direto na agenda de comerciantes ou chame clientes. Disponibilize para eles "Brincarem à vontade de gerir papelaria ali enquanto criam ou pagamm seus lances irreais com os carrinhos deles!" Sente-se observem suas intersecções! E conserte essas falhas e buracos de UX ali encontrados.

7. **Refinamento e Release 1.0 (Produção) (Semana 11):** []
    - Corrigir bugs reportados. []
        - **Objetivo:** "Finalizar arestas perdidas no código ou pontas brutas".
        - **Como executar:** Reforçar lógicas no Frontend pra dar melhor visões em caixas/botões ou bugs na arquitetura. Listar as reclamações no Alpha Staging de Testes que paravam fluxos (Ex: Produto nao achado no scan não renderiza na tela de modo agradavel pro comerciante, dando "Tela Cinza Morte"), de maior criticidade primeiro, pra a de menor cor ou forma nas fontes CSS.
    - Implementação de rotinas de Backup diário no PostgreSQL. []
        - **Objetivo:** Preparar proteção salva-vidas de ouro no controle anti-morte prematura de Software por perda nos bancos na cloud caso explodam corrompendo no Servidor Real de hospedagens em datas comemorativas - não te deixando arruinado a perder milhares de dados em contratos, onde um cliente perder seu Histórico vai parar na delegacia! É fundamental como apolice seguros para não quebrar a vida da marca SaaS criada recenemente de sua equipe Dev!.
        - **Como executar:** Via scripts "Cron Tab" configure na nuvem VPS uma trigger da execução `.sql_dump` isolando num backup limpinho todos os dias, a base inteira, salvado automaticamente num pacote compactado mandado (sem ninguém solicitar manualmente para ti não esquecer) à rede externa segura AWS (Amazon S3), guardada eternamente nos logs isolados pra acesso se faltar no Original da Virtual AWS - que garante tu durmir tranquilamente todas e as eventuais madrugadas turbulentas do ano comercial da Sua primeira empresa Software criado!.
    - Venda oficial e Lançamento (Monitorado via chamadas e logs do servidor). []
        - **Objetivo:** Entregar seu código na mãos do Comércio no Brasil. Realizar os ciclos de vida dos Softwares SaaS comercializados: Vender de verdade, fazer onboarding das Loja, Treinar seu painel para os donos, ganhar experiência em Engenharia corporativa sólida monitorada! Parabéns!.
        - **Como executar:** Troque domínio, anexe IP, ponha `SSL LetEncryp` em rodízio de criptografia do certificado Seguro, instale um Gerenciador da Qualidade das requisições (Sentry.io). Veja num relator local caso aconteça lentidões ou chamadas explodidas na interface Front pro Backend nas métricas reais na primeira semaninha no uso da nuvem Oficial (Production API Endpoint Global Branch). Emitir Recibos comerciais! Aproveitar as lições como Dev-Eng na Empresa e crescer junto de tudo novo aprendizado!.