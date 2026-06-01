"""
Módulo de transformação e cálculo de indicadores de risco.
"""
import sys
from matplotlib.path import Path
import pandas as pd
import numpy as np
from typing import Tuple

from pipeline.src.utils.indicators import RiskIndicators


def calcular_retornos_logaritmicos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula retornos logarítmicos a partir dos preços de fechamento.
    
    Args:
        df (pd.DataFrame): DataFrame com coluna 'Close' (pode ser MultiIndex)
    
    Returns:
        pd.DataFrame: DataFrame com coluna 'log_return'
    """
    df = df.copy()
    
    # Flattening MultiIndex columns if they exist
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)
    
    # Garantir que 'Close' existe
    if 'Close' not in df.columns:
        raise KeyError(f"Coluna 'Close' não encontrada. Colunas: {df.columns.tolist()}")
    
    df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
    return df


def calcular_volatilidade_anualizada(retornos: pd.Series, dias_trading: int = 252) -> float:
    """
    Calcula volatilidade histórica anualizada.
    
    Args:
        retornos (pd.Series): Série de retornos logarítmicos
        dias_trading (int): Dias de trading por ano (padrão: 252)
    
    Returns:
        float: Volatilidade anualizada (em percentual)
    """
    volatilidade_diaria = retornos.std()
    volatilidade_anualizada = volatilidade_diaria * np.sqrt(dias_trading)
    return volatilidade_anualizada * 100


def calcular_indicadores(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Calcula todos os indicadores de risco para um ativo.
    
    Args:
        df (pd.DataFrame): DataFrame com dados históricos
    
    Returns:
        tuple[pd.DataFrame, dict]: DataFrame com indicadores e dicionário com métricas
    """
    df = df.copy()
    
    # Retornos logarítmicos
    df = calcular_retornos_logaritmicos(df)
    
    # Remover NaN gerado pelo shift
    df = df.dropna(subset=['log_return'])
    
    # Volatilidade
    vol = calcular_volatilidade_anualizada(df['log_return'])
    
    # VaR Paramétrico @ 95%
    var_95 = RiskIndicators.var_parametrico(df['log_return'], confidence_level=0.95) * 100
    
    # Estatísticas resumidas
    resumo = {
        'volatilidade_anualizada_%': vol,
        'var_parametrico_95_%': var_95,
        'retorno_medio_%': df['log_return'].mean() * 100,
        'retorno_acumulado_%': df['log_return'].sum() * 100,
        'skewness': df['log_return'].skew(),
        'kurtosis': df['log_return'].kurtosis()
    }
    
    return df, resumo


def calcular_correlacoes(dados: dict) -> pd.DataFrame:
    """
    Calcula matriz de correlação entre os ativos.
    
    Args:
        dados (dict): Dicionário com DataFrames por ticker
    
    Returns:
        pd.DataFrame: Matriz de correlação
    """
    retornos = {}
    
    for ticker, df in dados.items():
        df_temp = calcular_retornos_logaritmicos(df)
        retornos[ticker] = df_temp['log_return']
    
    df_retornos = pd.DataFrame(retornos)
    correlacao = df_retornos.corr()
    
    return correlacao


if __name__ == "__main__":
    # Exemplo será usado no pipeline principal
    pass
