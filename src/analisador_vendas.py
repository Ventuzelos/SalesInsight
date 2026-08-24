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
    
    def total_unidades_vendidas(self):
        return self.dados["Quantidade"].sum()
    
    def ticket_medio(self):
        self._calcular_faturacao()

        return self.dados["Faturacao"].sum() / len(self.dados)

    def produto_maior_faturacao(self):
        self._calcular_faturacao()

        faturacao_por_produto = (
                self.dados
                .groupby("Produto")["Faturacao"]
                .sum()
        )

        return faturacao_por_produto.idxmax()


    def valor_produto_maior_faturacao(self):
        self._calcular_faturacao()

        faturacao_por_produto = (
            self.dados
            .groupby("Produto")["Faturacao"]
            .sum()
        )

        return faturacao_por_produto.max()
    
    

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
        
    def top_5_produtos_por_faturacao(self):
        self._calcular_faturacao()

        return (
            self.dados
            .groupby("Produto")["Faturacao"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

    def grafico_top_5_faturacao(self):
        top_5 = self.top_5_produtos_por_faturacao()

        plt.figure(figsize=(10, 6))

        top_5.sort_values().plot(kind="barh")

        plt.title("Top 5 Produtos por Faturação")
        plt.xlabel("Faturação (€)")
        plt.ylabel("Produto")

        plt.tight_layout()

        plt.savefig(
            "outputs/graficos/top_5_produtos_faturacao.png",
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
        

    def categoria_maior_faturacao(self):
        faturacao = self.faturacao_por_categoria()

        return faturacao.idxmax()

    def percentagem_faturacao_categoria(self, categoria):
        faturacao = self.faturacao_por_categoria()

        total = faturacao.sum()

        return (faturacao[categoria] / total) * 100

    def categoria_maior_quantidade(self):
        quantidade = self.quantidade_por_categoria()

        return quantidade.idxmax()
    
    
    def gerar_insights(self):
        categoria_faturacao = self.categoria_maior_faturacao()
        percentagem_categoria = self.percentagem_faturacao_categoria(
            categoria_faturacao
        )

        categoria_quantidade = self.categoria_maior_quantidade()
        produto_faturacao = self.produto_maior_faturacao()
        valor_produto = self.valor_produto_maior_faturacao()

        return [
            (
                f"A categoria {categoria_faturacao} representa "
                f"{percentagem_categoria:.1f}% da faturação total."
            ),
            (
                f"A categoria {categoria_quantidade} apresenta "
                f"o maior volume de unidades vendidas."
            ),
            (
                f"O produto {produto_faturacao} apresenta a maior "
                f"faturação individual, com {valor_produto:.2f} €."
            )
        ]




