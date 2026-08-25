# SalesInsight

Aplicação em Python para exploração, análise e visualização de dados de vendas, utilizando Pandas, Matplotlib e Programação Orientada a Objetos.

## Sobre o projeto

O SalesInsight é um projeto de análise de dados de vendas desenvolvido no âmbito do projeto final da Unidade de Competência 00618 – Criar aplicações em linguagem de programação Python.

A aplicação processa um conjunto de dados de vendas em formato CSV, realiza o tratamento e limpeza dos dados e calcula diferentes indicadores de desempenho comercial.

Para além das funcionalidades principais propostas no projeto, foram desenvolvidas análises adicionais, indicadores-chave de desempenho (KPIs), visualizações gráficas, geração automática de insights de negócio e testes automatizados.

O projeto foi desenvolvido com o objetivo de aplicar, de forma prática, conhecimentos de Python, Programação Orientada a Objetos, manipulação de dados, visualização de dados e controlo de versões.

## Objetivos

Os principais objetivos do projeto são:

- Carregar e explorar dados de vendas utilizando Pandas
- Identificar e remover registos de vendas inválidos
- Calcular a faturação total
- Identificar o produto mais vendido
- Calcular o total de unidades vendidas
- Calcular o ticket médio
- Identificar o produto com maior faturação
- Analisar os 5 produtos mais vendidos
- Analisar os 5 produtos com maior faturação
- Analisar a faturação por categoria
- Analisar a quantidade vendida por categoria
- Analisar a evolução da faturação ao longo do tempo
- Gerar insights de negócio automaticamente
- Criar visualizações gráficas utilizando Matplotlib
- Aplicar princípios de Programação Orientada a Objetos
- Guardar automaticamente os gráficos em formato PNG
- Validar as principais funcionalidades através de testes automatizados

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Pytest
- Git
- GitHub

## Estrutura do projeto

```text
SalesInsight/
│
├── data/
│   ├── vendas.csv
│   └── produtos.csv
│
├── outputs/
│   └── graficos/
│       ├── top_5_produtos.png
│       ├── top_5_produtos_faturacao.png
│       ├── faturacao_por_data.png
│       └── faturacao_por_categoria.png
│
├── src/
│   ├── analisador_vendas.py
│   ├── exploracao_vendas.py
│   └── teste_analisador.py
│
├── tests/
│   └── test_analisador_vendas.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Tratamento e limpeza dos dados

Antes da realização da análise, os dados são verificados e os registos inválidos são removidos.

O programa ignora registos onde:

- A quantidade seja negativa
- O preço seja igual ou inferior a zero

A coluna `Data` é também convertida para o formato de data, permitindo realizar análises relacionadas com a evolução das vendas ao longo do tempo.

Esta etapa permite garantir que os cálculos realizados posteriormente utilizam apenas registos considerados válidos.

## Classe `AnalisadorVendas`

A principal lógica de análise encontra-se organizada na classe `AnalisadorVendas`.

A classe recebe os dados através do seu construtor:

```python
def __init__(self, dados):
```

Através dos seus métodos são realizadas as principais operações de análise, incluindo:

- Limpeza dos dados
- Cálculo da faturação
- Identificação do produto mais vendido
- Cálculo do total de unidades vendidas
- Cálculo do ticket médio
- Identificação do produto com maior faturação
- Análise dos produtos mais vendidos
- Análise dos produtos com maior faturação
- Análise por categoria
- Análise temporal da faturação
- Geração de insights de negócio
- Geração de gráficos

## Principais funcionalidades

### Análise de vendas

O SalesInsight permite calcular:

- Faturação total
- Total de unidades vendidas
- Ticket médio
- Produto mais vendido
- Quantidade do produto mais vendido
- Produto com maior faturação
- Valor do produto com maior faturação
- Top 5 produtos por quantidade vendida
- Top 5 produtos por faturação
- Faturação por categoria
- Quantidade por categoria
- Faturação por data

### Indicadores-chave de desempenho

Foram acrescentados indicadores que permitem obter uma visão mais rápida do desempenho das vendas:

- Faturação total
- Unidades vendidas
- Ticket médio
- Produto com maior faturação
- Valor gerado pelo produto com maior faturação

## Insights de negócio

Para além da apresentação dos valores calculados, o projeto inclui uma camada de interpretação dos resultados.

O programa gera automaticamente insights relacionados com:

- A categoria responsável pela maior percentagem da faturação
- A categoria com maior volume de unidades vendidas
- O produto responsável pela maior faturação individual

Com os dados utilizados no projeto, foram identificados os seguintes insights:

- A categoria **Eletronica** representa aproximadamente **88,3% da faturação total**.
- A categoria **Papelaria** apresenta o maior volume de unidades vendidas.
- O produto **Portatil X** apresenta a maior faturação individual, com **5 100,00 €**.

## Visualizações

O projeto utiliza Matplotlib para gerar automaticamente quatro visualizações:

1. Top 5 produtos mais vendidos
2. Top 5 produtos por faturação
3. Evolução da faturação ao longo do tempo
4. Faturação por categoria

Os gráficos são guardados automaticamente na pasta:

```text
outputs/graficos/
```

Os ficheiros são gerados em formato PNG.

## Resultados obtidos

Com o conjunto de dados utilizado no projeto, foram obtidos os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Faturação total | 8 324,60 € |
| Unidades vendidas | 327 |
| Ticket médio | 224,99 € |
| Produto mais vendido | Caneta Azul |
| Quantidade do produto mais vendido | 90 unidades |
| Produto com maior faturação | Portatil X |
| Faturação do produto líder | 5 100,00 € |
| Categoria com maior faturação | Eletronica |
| Percentagem da faturação da Eletronica | 88,3% |

### Faturação por categoria

A distribuição da faturação por categoria é:

| Categoria | Faturação |
|---|---:|
| Eletronica | 7 352,50 € |
| Acessorios | 650,00 € |
| Papelaria | 322,10 € |

### Quantidade vendida por categoria

A distribuição da quantidade vendida por categoria é:

| Categoria | Unidades |
|---|---:|
| Papelaria | 234 |
| Eletronica | 56 |
| Acessorios | 37 |

## Instalação

Para executar o projeto, é necessário ter o Python instalado.

Depois de clonar o repositório, abrir o terminal na pasta do projeto e instalar as dependências:

```bash
python -m pip install -r requirements.txt
```

As principais bibliotecas utilizadas são:

```text
pandas
matplotlib
pytest
```

## Execução do programa

Para executar a análise completa:

```bash
python src/teste_analisador.py
```

O programa apresenta no terminal os principais resultados da análise e gera automaticamente os gráficos na pasta:

```text
outputs/graficos/
```

Entre os resultados apresentados encontram-se:

- Faturação total
- Total de unidades vendidas
- Ticket médio
- Produto mais vendido
- Top 5 produtos
- Top 5 produtos por faturação
- Faturação por categoria
- Quantidade por categoria
- Faturação por data
- Produto com maior faturação
- Insights de negócio

## Execução dos testes

O projeto inclui uma suite de testes automatizados utilizando Pytest.

Para executar os testes:

```bash
python -m pytest
```

Os testes validam as principais funcionalidades da classe `AnalisadorVendas`, incluindo:

- Limpeza dos dados
- Cálculo da faturação
- Identificação do produto mais vendido
- Cálculo das quantidades
- Top 5 produtos
- Top 5 produtos por faturação
- Análise por categoria
- Análise temporal
- Cálculo dos KPIs
- Geração dos insights de negócio

## Controlo de versões

O desenvolvimento do projeto foi realizado utilizando Git e GitHub.

O histórico de commits permite acompanhar a evolução do projeto desde a implementação inicial até à adição das funcionalidades de análise, testes, KPIs, insights e visualizações.

## Conclusão

O SalesInsight demonstra a aplicação prática dos conhecimentos adquiridos na Unidade de Competência 00618, integrando:

- Programação em Python
- Programação Orientada a Objetos
- Manipulação de dados com Pandas
- Visualização de dados com Matplotlib
- Limpeza e validação de dados
- Análise de indicadores de vendas
- Geração de insights
- Testes automatizados
- Controlo de versões com Git e GitHub
