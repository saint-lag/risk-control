import pandas as pd

import numpy as np    
from scipy.stats import norm

class RiskIndicators:
    @staticmethod
    def calcular_volatilidade_anualizada(retornos: pd.Series, dias_trading: int = 252) -> float:
        """
        Calcula a volatilidade anualizada a partir de uma série de retornos logarítmicos.

        Parâmetros:
        retornos (pd.Series): Série de retornos logarítmicos.
        dias_trading (int): Número de dias de trading por ano (padrão: 252).

        Retorna:
        float: Volatilidade anualizada em percentual.
        """
        volatilidade_diaria = retornos.std()
        volatilidade_anualizada = volatilidade_diaria * np.sqrt(dias_trading)
        return volatilidade_anualizada

    @staticmethod
    def var_parametrico(log_return_series, confidence_level):
        """
        Calcula o Value at Risk (VaR) paramétrico para uma série de retornos logarítmicos.

        Parâmetros:
        log_return_series (pd.Series): Série de retornos logarítmicos.
        confidence_level (float): Nível de confiança para o cálculo do VaR (ex: 0.95 para 95%).

        Retorna:
        float: O valor do VaR paramétrico.
        """

        # Calcular a média e o desvio padrão dos retornos logarítmicos
        mean = log_return_series.mean()
        std_dev = log_return_series.std()

        # Calcular o quantil correspondente ao nível de confiança
        quantile = norm.ppf(1 - confidence_level)

        # Calcular o VaR paramétrico
        var_parametric = -(mean + quantile * std_dev)

        return var_parametric
    
    @staticmethod
    def calculate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula a matriz de correlação entre os retornos logarítmicos dos ativos.

        Parâmetros:
        df (pd.DataFrame): DataFrame contendo os retornos logarítmicos dos ativos, onde cada coluna representa um ativo.

        Retorna:
        pd.DataFrame: Matriz de correlação entre os ativos.
        """
        return df.corr()

    @staticmethod
    def cvar_parametrico(log_return_series, confidence_level):
        """
        Calcula o Conditional Value at Risk (CVaR) paramétrico para uma série de retornos logarítmicos.

        Parâmetros:
        log_return_series (pd.Series): Série de retornos logarítmicos.
        confidence_level (float): Nível de confiança para o cálculo do CVaR (ex: 0.95 para 95%).

        Retorna:
        float: O valor do CVaR paramétrico.
        """

        # Calcular a média e o desvio padrão dos retornos logarítmicos
        mean = log_return_series.mean()
        std_dev = log_return_series.std()

        # Calcular o quantil correspondente ao nível de confiança
        quantile = norm.ppf(1 - confidence_level)

        # Calcular o CVaR paramétrico
        cvar_parametric = -(mean + (std_dev * norm.pdf(quantile)) / (1 - confidence_level))

        return cvar_parametric
    
    @staticmethod
    def calculate_historical_var(log_return_series, confidence_level):
        """
        Calcula o Value at Risk (VaR) histórico para uma série de retornos logarítmicos.

        Parâmetros:
        log_return_series (pd.Series): Série de retornos logarítmicos.
        confidence_level (float): Nível de confiança para o cálculo do VaR (ex: 0.95 para 95%).

        Retorna:
        float: O valor do VaR histórico.
        """
        var_historical = -np.percentile(log_return_series, (1 - confidence_level) * 100)
        return var_historical
    
    @staticmethod
    def calculate_sharpe_ratio(log_return_series, risk_free_rate=0.0):
        """
        Calcula o Sharpe Ratio para uma série de retornos logarítmicos.

        Parâmetros:
        log_return_series (pd.Series): Série de retornos logarítmicos.
        risk_free_rate (float): Taxa livre de risco (padrão: 0.0).

        Retorna:
        float: O valor do Sharpe Ratio.
        """
        excess_return = log_return_series.mean() - risk_free_rate
        volatility = log_return_series.std()
        
        if volatility == 0:
            return np.nan  # Evitar divisão por zero
        
        sharpe_ratio = excess_return / volatility
        return sharpe_ratio