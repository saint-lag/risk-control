"""
Módulo de validação de dados e indicadores.
"""

import pandas as pd
import numpy as np


def validar_dados_brutos(df: pd.DataFrame) -> dict:
    """
    Valida qualidade dos dados brutos.
    
    Args:
        df (pd.DataFrame): DataFrame com dados históricos
    
    Returns:
        dict: Dicionário com resultados da validação
    """
    validacoes = {
        'total_registros': len(df),
        'valores_nulos': df.isnull().sum().sum(),
        'percentual_nulos': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100,
        'registros_validos': len(df.dropna()),
        'data_inicio': df.index[0] if len(df) > 0 else None,
        'data_fim': df.index[-1] if len(df) > 0 else None,
    }
    
    return validacoes


def validar_retornos(retornos: pd.Series) -> dict:
    """
    Valida série de retornos.
    
    Args:
        retornos (pd.Series): Série de retornos logarítmicos
    
    Returns:
        dict: Dicionário com resultados da validação
    """
    validacoes = {
        'retornos_nan': retornos.isna().sum(),
        'retornos_infinitos': np.isinf(retornos).sum(),
        'retornos_positivos_%': (retornos > 0).sum() / len(retornos) * 100,
        'retornos_negativos_%': (retornos < 0).sum() / len(retornos) * 100,
    }
    
    return validacoes


def gerar_relatorio_validacao(dados: dict) -> None:
    """
    Gera relatório de validação para todos os ativos.
    
    Args:
        dados (dict): Dicionário com DataFrames por ticker
    """
    print("\n" + "="*60)
    print("📋 RELATÓRIO DE VALIDAÇÃO DE DADOS")
    print("="*60)
    
    for ticker, df in dados.items():
        print(f"\n🔍 {ticker}")
        val = validar_dados_brutos(df)
        print(f"   Registros: {val['total_registros']}")
        print(f"   Valores nulos: {val['valores_nulos']} ({val['percentual_nulos']:.2f}%)")
        print(f"   Período: {val['data_inicio'].date()} a {val['data_fim'].date()}")


if __name__ == "__main__":
    pass
