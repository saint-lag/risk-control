"""
Módulo de carregamento e persistência de dados processados.
"""

import pandas as pd
from pathlib import Path
import json


def salvar_dados_processados(dados: dict, caminho_saida: str = "pipeline/data/processed"):
    """
    Salva dados processados em CSV.
    
    Args:
        dados (dict): Dicionário com DataFrames por ticker
        caminho_saida (str): Caminho da pasta de saída
    """
    Path(caminho_saida).mkdir(parents=True, exist_ok=True)
    
    for ticker, df in dados.items():
        nome_arquivo = f"{caminho_saida}/{ticker.replace('.', '_')}_processed.csv"
        df.to_csv(nome_arquivo)
        print(f"💾 Salvo: {nome_arquivo}")


def salvar_indicadores(indicadores: dict, caminho_saida: str = "pipeline/data/processed"):
    """
    Salva indicadores calculados em JSON.
    
    Args:
        indicadores (dict): Dicionário com indicadores por ticker
        caminho_saida (str): Caminho da pasta de saída
    """
    Path(caminho_saida).mkdir(parents=True, exist_ok=True)
    
    # Converter valores para formatos serializáveis
    indicadores_serializados = {}
    for ticker, ind in indicadores.items():
        indicadores_serializados[ticker] = {
            k: float(v) if isinstance(v, (int, float)) else str(v)
            for k, v in ind.items()
        }
    
    arquivo = f"{caminho_saida}/indicadores_risco.json"
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(indicadores_serializados, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Salvo: {arquivo}")


def salvar_correlacoes(correlacao: pd.DataFrame, caminho_saida: str = "pipeline/data/processed"):
    """
    Salva matriz de correlação.
    
    Args:
        correlacao (pd.DataFrame): Matriz de correlação
        caminho_saida (str): Caminho da pasta de saída
    """
    Path(caminho_saida).mkdir(parents=True, exist_ok=True)
    
    arquivo = f"{caminho_saida}/matriz_correlacao.csv"
    correlacao.to_csv(arquivo)
    print(f"💾 Salvo: {arquivo}")


def carregar_dados_processados(ticker: str, caminho: str = "pipeline/data/processed") -> pd.DataFrame:
    """
    Carrega dados processados.
    
    Args:
        ticker (str): Ticker do ativo
        caminho (str): Caminho da pasta
    
    Returns:
        pd.DataFrame: Dados processados
    """
    arquivo = f"{caminho}/{ticker.replace('.', '_')}_processed.csv"
    return pd.read_csv(arquivo, index_col=0)


if __name__ == "__main__":
    pass
