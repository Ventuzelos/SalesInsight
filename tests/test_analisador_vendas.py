import pandas as pd

from src.analisador_vendas import AnalisadorVendas


def criar_dados_teste():
    return pd.DataFrame({
        "Data": [
            "2026-05-01",
            "2026-05-01",
            "2026-05-02"
        ],
        "Produto": [
            "Produto A",
            "Produto B",
            "Produto A"
        ],
        "Categoria": [
            "Categoria 1",
            "Categoria 2",
            "Categoria 1"
        ],
        "Quantidade": [
            10,
            5,
            7
        ],
        "Preco": [
            10.0,
            20.0,
            10.0
        ]
    })


def criar_analisador():
    dados = criar_dados_teste()

    analisador = AnalisadorVendas(dados)
    analisador.limpar_dados()

    return analisador


def test_total_faturado():
    analisador = criar_analisador()

    resultado = analisador.total_faturado()

    assert resultado == 270.0


def test_produto_mais_vendido():
    analisador = criar_analisador()

    resultado = analisador.produto_mais_vendido()

    assert resultado == "Produto A"


def test_top_5_produtos():
    analisador = criar_analisador()

    resultado = analisador.top_5_produtos()

    assert resultado["Produto A"] == 17
    assert resultado["Produto B"] == 5


def test_faturacao_por_categoria():
    analisador = criar_analisador()

    resultado = analisador.faturacao_por_categoria()

    assert resultado["Categoria 1"] == 170.0
    assert resultado["Categoria 2"] == 100.0


def test_limpeza_remove_dados_invalidos():
    dados = pd.DataFrame({
        "Data": [
            "2026-05-01",
            "2026-05-02",
            "2026-05-03"
        ],
        "Produto": [
            "Produto A",
            "Produto B",
            "Produto C"
        ],
        "Categoria": [
            "Categoria 1",
            "Categoria 1",
            "Categoria 2"
        ],
        "Quantidade": [
            10,
            -5,
            8
        ],
        "Preco": [
            10.0,
            20.0,
            0.0
        ]
    })

    analisador = AnalisadorVendas(dados)

    resultado = analisador.limpar_dados()

    assert len(resultado) == 1
    assert resultado.iloc[0]["Produto"] == "Produto A"
    
    
def test_quantidade_produto_mais_vendido():
    analisador = criar_analisador()

    resultado = analisador.quantidade_produto_mais_vendido()

    assert resultado == 17
    
    
def test_top_5_produtos_por_faturacao():
    analisador = criar_analisador()

    resultado = analisador.top_5_produtos_por_faturacao()

    assert resultado["Produto A"] == 170.0
    assert resultado["Produto B"] == 100.0
    
def test_quantidade_por_categoria():
    analisador = criar_analisador()

    resultado = analisador.quantidade_por_categoria()

    assert resultado["Categoria 1"] == 17
    assert resultado["Categoria 2"] == 5
    

def test_faturacao_por_data():
    analisador = criar_analisador()

    resultado = analisador.faturacao_por_data()

    assert resultado[pd.Timestamp("2026-05-01")] == 200.0
    assert resultado[pd.Timestamp("2026-05-02")] == 70.0
    

def test_total_unidades_vendidas():
    analisador = criar_analisador()

    assert analisador.total_unidades_vendidas() == 22
    
def test_ticket_medio():
    analisador = criar_analisador()

    assert analisador.ticket_medio() == 90.0
    
def test_produto_maior_faturacao():
    analisador = criar_analisador()

    assert analisador.produto_maior_faturacao() == "Produto A"
    
def test_valor_produto_maior_faturacao():
    analisador = criar_analisador()

    assert analisador.valor_produto_maior_faturacao() == 170.0
    
def test_categoria_maior_faturacao():
    analisador = criar_analisador()

    resultado = analisador.categoria_maior_faturacao()

    assert resultado == "Categoria 1"
    

def test_percentagem_faturacao_categoria():
    analisador = criar_analisador()

    resultado = analisador.percentagem_faturacao_categoria("Categoria 1")

    assert resultado == (170 / 270) * 100
    
def test_categoria_maior_quantidade():
    analisador = criar_analisador()

    resultado = analisador.categoria_maior_quantidade()

    assert resultado == "Categoria 1"
    
def test_gerar_insights():
    analisador = criar_analisador()

    insights = analisador.gerar_insights()

    assert len(insights) == 3
    assert "Categoria 1" in insights[0]
    assert "Categoria 1" in insights[1]
    assert "Produto A" in insights[2]
