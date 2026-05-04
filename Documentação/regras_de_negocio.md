# Regras de Negócio e Cruzamento de Estoque

Este documento define a estratégia fundamental para gerenciar os diferentes estoques do **Patas&Páginas** e como eles se cruzam na operação de vendas geral (PDV).

## 1. O Problema da Divergência de Estoque
Temos 3 naturezas de produtos que não compartilham as mesmas características:
- **Livraria:** O livro *1984* tem ISBN, Autor (George Orwell), Editora. O lote não importa muito e ele não "estraga".
- **Papelaria:** A caneta esferográfica azul tem Cor (Azul), Marca (Bic).
- **Café:**
  - **Insumos/Perecíveis:** O leite tem Unidade de Medida (ml) e Data de Validade. Não é vendido diretamente ao cliente.
  - **Receitas/Compostos:** O "Café Macchiato" é vendido ao cliente final, mas, ao ser vendido, deve abater 50ml do leite e 15g de café em pó do estoque de insumos.

## 2. A Estratégia de Polimorfismo (Produto Base)
Para que o Caixa consiga adicionar qualquer coisa no mesmo *Carrinho de Compras*, sem que o código fique cheio de "ifs" (`if produto_tipo == 'livro'`), utilizaremos o modelo de **Herança/Polimorfismo de Banco de Dados**.

### O Módulo Central: Tabela `Produto Base`
Todos os itens compartilháveis existirão em uma tabela central chamada de `Produto Base`. 
A tabela base conterá tudo o que é comum financeiramente e a todo sistema de varejo:
- `ID`, `Nome`, `SKU` (Código de barras genérico), `Preço de Venda`, `Preço de Custo`, `Quantidade em Estoque`, e `Tipo_Produto` (Livro, Papelaria, Cafe_Reven_Direta, Cafe_Insumo, Cafe_Receita).

### As Tabelas Específicas (Filhas)
- `Livro:` Vai ter apenas um ID fazendo referência ao `Produto Base`, mais as colunas `ISBN`, `Autor`, `Editora`, `Paginas`.
- `Papelaria:` Referência ao `Produto Base`, mais `Cor`, `Marca`.
- `Cafe Insumo:` Referência ao `Produto Base`, mais `Unidade` (Gr, Ml, Unidade), `Data Validade`.

## 3. Regras de Cruzamento Funcional no Fluxo de Venda (O PDV)

1. **Ação de Adição ao Carrinho:** O operador bipará o SKU ou pesquisará pelo NOME. A busca acontece sempre de forma global na tabela de `Produto Base`. O sistema traz o item e seu preço com facilidade.
2. **Conclusão da Venda (Baixa de Estoque):**
   - **Fluxo Simples (Livros, Papelaria e Revenda Direta do Café como Refrigerante em lata):**
      - A regra do banco subtrai a `Quantidade Vendida` do `Quantidade em Estoque` direto na tabela `Produto Base`.
   - **Fluxo Composto (Receitas do Café - Ex: Expresso Duplo):**
      - O *Expresso Duplo* é cadastrado como um produto, mas ele **não possui** quantidade em estoque no Produto Base (fica com `NULL` ou `0` com flag `is_composicao=True`).
      - Existirá uma tabela chamada `Receita` e `Receita_Item`. O sistema vai lá, checa que o Expresso Duplo requer `20g` de "Café Moído" (este sim é um Cafe_Insumo). Ele então reduz os `20g` multiplicados pelo número de cafés comprados do estoque real do Café Moído.
3. **Restrições de Fechamento:** Se a operação de venda falhar no gateway financeiro ou o cartão não passar, a ação no estoque deve ser estritamente bloqueada ("Rollback de Transação Db"). O PIX sem confirmação em 3 minutos devolve dinamicamente o estoque flutuante ao registro `Produto Base`.

## 4. Resumo de Entidades para Implementação no Banco/ORM
A estrutura que será alimentada para o backend (Django) seguirá o seguinte conceito ORM:

```python
# Pseudo-código de Modelagem (Django)
class Produto(models.Model):
    nome = CharField()
    sku = CharField()
    preco = DecimalField()
    estoque = DecimalField() # Pode lidar com G/Ml se for insumo
    tipo = CharField(choices=[('livro', 'Livraria'), ('cafe_receita', 'Receita Café'), ...])

class Livro(models.Model):
    produto = OneToOneField(Produto)
    isbn = CharField()
    autor = CharField()

class ReceitaComposicao(models.Model):
    produto_receita = ForeignKey(Produto) # O que será vendido (ex: Café Expresso)
    insumo = ForeignKey(Produto) # O que será gasto (ex: Pó de café)
    quantidade_gasta = DecimalField()
```
