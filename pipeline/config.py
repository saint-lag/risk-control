"""
Configurações do pipeline de análise de risco.
"""

# Ativos para análise
TICKERS_DEFAULT = [
    "PETR4.SA",  # Petrobras
    "VALE3.SA",  # Vale
    "WEGE3.SA",  # WEG
    "BBAS3.SA",  # Banco do Brasil
    "ITUB4.SA",  # Itaú 
]

# Período de análise
PERIODO_MESES = 6
DIAS_TRADING_ANO = 252

# Nível de confiança para VaR
VAR_CONFIDENCE_LEVEL = 0.95

# Caminhos de dados
CAMINHO_DADOS_BRUTOS = "pipeline/data/raw"
CAMINHO_DADOS_PROCESSADOS = "pipeline/data/processed"

# Configurações de visualização
PLOTLY_TEMPLATE = "plotly_white"
