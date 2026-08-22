import pandas as pd

dados = pd.read_csv("data/vendas.csv")

print(dados.head())
print(dados.info())
print(dados.describe())

print("\nProdutos:")
print(dados["Produto"].unique())

print("\nCategorias:")
print(dados["Categoria"].unique())

print("\nQuantidade de produtos:")
print(dados["Produto"].nunique())

print("\nRegistos inválidos:")
print(dados[(dados["Quantidade"] < 0) | (dados["Preco"] <= 0)])

dados_limpos = dados[
    (dados["Quantidade"] >= 0) &
    (dados["Preco"] > 0)
]

print("\nDados após limpeza:")
print(dados_limpos)

print("\nNúmero de registos válidos:")
print(len(dados_limpos))

print("\nNúmero de registos removidos:")
print(len(dados) - len(dados_limpos))


dados_limpos = dados_limpos.copy()

dados_limpos["Faturacao"] = (
    dados_limpos["Quantidade"] * dados_limpos["Preco"]
)
print("\nDados com faturação:")
print(dados_limpos.head())


total_faturado = dados_limpos["Faturacao"].sum()

print("\nTotal faturado:")
print(f"{total_faturado:.2f} €")



vendas_por_produto = (
    dados_limpos.groupby("Produto")["Quantidade"].sum()
)

print("\nQuantidade vendida por produto:")
print(vendas_por_produto)



produto_mais_vendido = vendas_por_produto.idxmax()
quantidade_mais_vendida = vendas_por_produto.max()

print("\nProduto mais vendido:")
print(
    f"{produto_mais_vendido} - "
    f"{quantidade_mais_vendida} unidades"
)


top_5_produtos = vendas_por_produto.sort_values(
    ascending=False
).head(5)

print("\nTop 5 produtos mais vendidos:")
print(top_5_produtos)


faturacao_por_produto = (
    dados_limpos.groupby("Produto")["Faturacao"].sum()
)

top_5_faturacao = faturacao_por_produto.sort_values(
    ascending=False
).head(5)

print("\nTop 5 produtos por faturação:")
print(top_5_faturacao)



faturacao_por_categoria = (
    dados_limpos.groupby("Categoria")["Faturacao"].sum()
    .sort_values(ascending=False)
)

print("\nFaturação por categoria:")
print(faturacao_por_categoria)

quantidade_por_categoria = (
    dados_limpos.groupby("Categoria")["Quantidade"].sum()
    .sort_values(ascending=False)
)

print("\nQuantidade vendida por categoria:")
print(quantidade_por_categoria)


