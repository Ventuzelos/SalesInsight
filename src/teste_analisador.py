import pandas as pd

from analisador_vendas import AnalisadorVendas


dados = pd.read_csv("data/vendas.csv")

analisador = AnalisadorVendas(dados)

analisador.limpar_dados()

print("Total faturado:")
print(f"{analisador.total_faturado():.2f} €")

print("\nTotal de unidades vendidas:")
print(analisador.total_unidades_vendidas())

print("\nTicket médio:")
print(f"{analisador.ticket_medio():.2f} €")

print("\nProduto com maior faturação:")
print(analisador.produto_maior_faturacao())

print("\nValor do produto com maior faturação:")
print(f"{analisador.valor_produto_maior_faturacao():.2f} €")

print("\nProduto mais vendido:")
print(
    f"{analisador.produto_mais_vendido()} - "
    f"{analisador.quantidade_produto_mais_vendido()} unidades"
)

print("\nTop 5 produtos:")
print(analisador.top_5_produtos())

print("\nTop 5 produtos por faturação:")
print(analisador.top_5_produtos_por_faturacao())

print("\nFaturação por categoria:")
print(analisador.faturacao_por_categoria())

print("\nQuantidade por categoria:")
print(analisador.quantidade_por_categoria())

print("\nFaturação por data:")
print(analisador.faturacao_por_data())


print("\nA apresentar gráfico...")
analisador.grafico_top_5()

print("\nA apresentar Top 5 por faturação...")
analisador.grafico_top_5_faturacao()

print("\nA apresentar evolução da faturação...")
analisador.grafico_faturacao_por_data()