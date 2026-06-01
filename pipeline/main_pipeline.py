"""
Pipeline principal de análise de risco financeiro.
Orquestra todas as etapas: Extract → Transform → Validate → Load
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pipeline.src.extract.main import baixar_historico, salvar_dados_brutos
from pipeline.src.transform.main import calcular_indicadores, calcular_correlacoes
from pipeline.src.validation.main import gerar_relatorio_validacao
from pipeline.src.load.main import salvar_dados_processados, salvar_indicadores, salvar_correlacoes


def executar_pipeline(tickers: list, periodo_meses: int = 6):
    """
    Executa o pipeline completo de análise de risco.
    
    Args:
        tickers (list): Lista de tickers (ex: ['PETR4.SA', 'VALE3.SA'])
        periodo_meses (int): Período em meses
    """
    
    print("\n" + "="*70)
    print("INICIANDO PIPELINE DE ANÁLISE DE RISCO")
    print("="*70)
    
    # ===== ETAPA 1: EXTRACT (Coleta) =====
    print("\n[1/4] EXTRACT - Coleta de Dados")
    print("-" * 70)
    dados_brutos = baixar_historico(tickers, periodo_meses)
    
    if not dados_brutos:
        print("Erro: Nenhum dado foi coletado!")
        return
    
    salvar_dados_brutos(dados_brutos)
    
    # ===== ETAPA 2: VALIDATION (Validação) =====
    print("\n[2/4] VALIDATION - Verificação de Qualidade")
    print("-" * 70)
    gerar_relatorio_validacao(dados_brutos)
    
    # ===== ETAPA 3: TRANSFORM (Transformação) =====
    print("\n[3/4] TRANSFORM - Cálculo de Indicadores")
    print("-" * 70)
    
    dados_processados = {}
    indicadores_risco = {}
    
    for ticker, df in dados_brutos.items():
        print(f"\n Processando {ticker}...")
        df_proc, indicadores = calcular_indicadores(df)
        
        dados_processados[ticker] = df_proc
        indicadores_risco[ticker] = indicadores
        
        # Exibir indicadores
        print(f"      • Volatilidade Anualizada: {indicadores['volatilidade_anualizada_%']:.2f}%")
        print(f"      • VaR (95%): {indicadores['var_parametrico_95_%']:.2f}%")
        print(f"      • Retorno Acumulado: {indicadores['retorno_acumulado_%']:.2f}%")
    
    # Correlações
    print(f"\n Calculando matriz de correlação...")
    correlacao = calcular_correlacoes(dados_brutos)
    
    # ===== ETAPA 4: LOAD (Persistência) =====
    print("\n[4/4] LOAD - Armazenamento de Resultados")
    print("-" * 70)
    
    salvar_dados_processados(dados_processados)
    salvar_indicadores(indicadores_risco)
    salvar_correlacoes(correlacao)
    
    # ===== RESUMO FINAL =====
    print("\n" + "="*70)
    print("PIPELINE CONCLUÍDO COM SUCESSO!")
    print("="*70)
    print(f"\n Resumo:")
    print(f"   • Ativos processados: {len(dados_processados)}")
    print(f"   • Dados brutos: pipeline/data/raw/")
    print(f"   • Dados processados: pipeline/data/processed/")
    print(f"   • Indicadores: pipeline/data/processed/indicadores_risco.json")
    print(f"   • Correlações: pipeline/data/processed/matriz_correlacao.csv")
    print()


if __name__ == "__main__":
    # Configuração de ativos para análise
    import config
    tickers = config.TICKERS_DEFAULT
    periodo_meses = 6
    
    executar_pipeline(tickers, periodo_meses)
