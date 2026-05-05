# Diagrama Entidade-Relacionamento (DER)

Abaixo está a representação visual do DER modelado para suportar os três nichos usando uma base única de Produtos através do conceito de Polimorfismo e Relacionamento Composto.
Essa modelagem garante máxima flexibilidade enquanto mantém a consistência financeira na hora do fechamento do caixa no cruzamento do estoque.

### Diagrama (Mermaid)

```mermaiderDiagram
    PRODUTO {
        int id PK
        string nome
        string sku
        decimal preco_venda
        decimal quantidade_estoque
        string tipo "ENUM('livro', 'papelaria', 'insumo', 'receita')"
    }

    LIVRO {
        int produto_id FK
        string isbn
        string autor
        string editora
    }

    PAPELARIA {
        int produto_id FK
        string marca
        string cor
    }

    INSUMO {
        int produto_id FK
        string unidade_medida "Ex: gramas, ml"
        date validade
    }

    RECEITA_COMPOSICAO {
        int id PK
        int receita_produto_id FK "Produto final vendido"
        int insumo_produto_id FK "Produto descontado do estoque"
        decimal quantidade_necessaria "O que se consome por preparo"
    }

    PEDIDO {
        int id PK
        int usuario_id FK "Funcionário do caixa"
        decimal total_calculado
        string status "Pendente, Pago, Cancelado"
        datetime data_criacao
    }

    PEDIDO_ITEM {
        int id PK
        int pedido_id FK
        int produto_id FK
        int quantidade "Quantidade ou Fração adicionada por bipagem"
        decimal preco_unitario_aplicado "Para suportar descontos à parte"
    }

    PRODUTO ||--o| LIVRO : Herda
    PRODUTO ||--o| PAPELARIA : Herda
    PRODUTO ||--o| INSUMO : Herda
    
    PRODUTO ||--o{ RECEITA_COMPOSICAO : "Possui N ingredientes"
    PRODUTO ||--o{ RECEITA_COMPOSICAO : "É ingrediente de"
    
    PEDIDO ||--o{ PEDIDO_ITEM : "Contém"
    PRODUTO ||--o{ PEDIDO_ITEM : "É vendido através de"

```

### O que o Diagrama Demonstra
- **Unificação para o PDV:** O `PEDIDO_ITEM` (no carrinho de compras do caixa) se liga diretamente ao `PRODUTO` base. O caixa jamais vai precisar saber no banco de dados "se é um livro ou uma caneta", ele bipa o código, cai num *Produto*, e fatura.
- **Isolamento de Domínios:** Se uma caneta possui `marca` e `cor`, isso é armazenado estritamente na tabela de `PAPELARIA`, não deixando a tabela Base entupida de colunas que só a papelaria usa.
- **Insumos Dinâmicos:** Se um `PRODUTO` Base (como o Expresso Simples) entrar no Recibo de Venda, o backend será instruído a ir até a tabela de `RECEITA_COMPOSICAO` e subtrair os ingredientes atrelados dela diretamente de seus respectivos itens marcados como `INSUMO`.
