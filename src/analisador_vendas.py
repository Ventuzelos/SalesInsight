import pandas as pd
import matplotlib.pyplot as plt


class AnalisadorVendas:

    def __init__(self, dados):
        self.dados = dados

    def limpar_dados(self):
        self.dados = self.dados[
        (self.dados["Quantidade"] >= 0) &
        (self.dados["Preco"] > 0)
        ].copy()

        self.dados["Data"] = pd.to_datetime(self.dados["Data"])

        return self.dados

    def _calcular_faturacao(self):
        self.dados["Faturacao"] = (
            self.dados["Quantidade"] * self.dados["Preco"]
        )

    def total_faturado(self):
        self._calcular_faturacao()
        return self.dados["Faturacao"].sum()

    def produto_mais_vendido(self):
        vendas_por_produto = (
            self.dados.groupby("Produto")["Quantidade"].sum()
        )

        return vendas_por_produto.idxmax()

    def quantidade_produto_mais_vendido(self):
        vendas_por_produto = (
            self.dados.groupby("Produto")["Quantidade"].sum()
        )

        return vendas_por_produto.max()

    def top_5_produtos(self):
        return (
            self.dados
            .groupby("Produto")["Quantidade"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

    def faturacao_por_categoria(self):
        self._calcular_faturacao()

        return (
            self.dados
            .groupby("Categoria")["Faturacao"]
            .sum()
            .sort_values(ascending=False)
        )

    def quantidade_por_categoria(self):
        return (
            self.dados
            .groupby("Categoria")["Quantidade"]
            .sum()
            .sort_values(ascending=False)
        )

    def grafico_top_5(self):
        top_5 = self.top_5_produtos()

        plt.figure(figsize=(10, 6))

        top_5.plot(kind="bar")

        plt.title("Top 5 Produtos Mais Vendidos")
        plt.xlabel("Produto")
        plt.ylabel("Unidades Vendidas")

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig(
            "outputs/graficos/top_5_produtos.png",
            dpi=300
        )

        plt.show()
        plt.close()
        
        
    def faturacao_por_data(self):
        self._calcular_faturacao()

        return (
            self.dados
            .groupby("Data")["Faturacao"]
            .sum()
            .sort_index()
    )
        
    def grafico_faturacao_por_data(self):
        faturacao = self.faturacao_por_data()

        plt.figure(figsize=(10, 6))

        faturacao.plot(
            kind="line",
            marker="o"
        )

        plt.title("Evolução da Faturação")
        plt.xlabel("Data")
        plt.ylabel("Faturação (€)")

        plt.xticks(rotation=45, ha="right")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        plt.savefig(
            "outputs/graficos/faturacao_por_data.png",
            dpi=300
        )

        plt.show()
        plt.close()