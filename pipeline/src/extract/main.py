"""
Módulo de extração de dados financeiros usando yfinance.
Coleta dados históricos de ativos brasileiros.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path


def baixar_historico(tickers: list, periodo_meses: int = 6) -> dict:
    """
    Baixa dados históricos de ativos financeiros.
    
    Args:
        tickers (list): Lista de tickers (ex: ['PETR4.SA', 'VALE3.SA'])
        periodo_meses (int): Número de meses de histórico (padrão: 6)
    
    Returns:
        dict: Dicionário com DataFrames por ticker
              {ticker: DataFrame com OHLCV}
    """
    # Calcular período
    data_fim = datetime.now()
    data_inicio = data_fim - timedelta(days=periodo_meses * 30)
    
    print(f"📥 Baixando dados de {len(tickers)} ativos...")
    print(f"   Período: {data_inicio.date()} a {data_fim.date()}")
    
    dados = {}
    
    for ticker in tickers:
        try:
            print(f"   ⏳ Processando {ticker}...", end=" ", flush=True)
            df = yf.download(
                ticker, 
                start=data_inicio, 
                end=data_fim,
                progress=False
            )
            
            if df is None or df.empty:
                print(f"❌ Nenhum dado encontrado")
                continue
            
            # Adicionar coluna de ticker
            df['Ticker'] = ticker
            dados[ticker] = df
            print(f"✅ {len(df)} registros")
            
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            continue
    
    print(f"\n✓ Total de {len(dados)} ativos baixados com sucesso\n")
    return dados


def salvar_dados_brutos(dados: dict, caminho_saida: str = "pipeline/data/raw"):
    """
    Salva dados brutos em arquivos CSV.
    
    Args:
        dados (dict): Dicionário com DataFrames por ticker
        caminho_saida (str): Caminho da pasta de saída
    """
    Path(caminho_saida).mkdir(parents=True, exist_ok=True)
    
    for ticker, df in dados.items():
        nome_arquivo = f"{caminho_saida}/{ticker.replace('.', '_')}_raw.csv"
        df.to_csv(nome_arquivo)
        print(f"💾 Salvo: {nome_arquivo}")


if __name__ == "__main__":
    tickers = ["PETR4.SA", "VALE3.SA", "WEGE3.SA"]
    dados = baixar_historico(tickers)
    salvar_dados_brutos(dados)