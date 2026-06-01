# risk-control
Pequeno pipeline de análise de risco de mercado utilizando dados de ativos financeiros negociados no Brasil.

## Coleta de Dados
Dados históricos de pelo menos dois ativos financeiros brasileiros
(ações, índices, fundos, etc.) com cotações diárias dos últimos 6 meses.

Fontes permitidas (gratuitas):
- B3 – Bolsa do Brasil via API do Yahoo Finance
- Brasil API (https://brasilapi.com.br/)
- Alpha Vantage (https://www.alphavantage.co/)
- Investing.com via Web Scraping com investpy

Dica: Para ações da B3 no Yahoo Finance, o ticker precisa ser seguido de .SA, ex:
PETR4.SA.

## Cálculo de Indicadores de Risco
Com os dados coletados, implemente os seguintes indicadores:
- Volatilidade histórica anualizada (com base em retornos diários)
- Valor em Risco (VaR) paramétrico a 95% (pressuponha distribuição
normal)
- Correlação entre os ativos

Fórmulas devem ser corretamente implementadas. Pode-se usar bibliotecas
como pandas, numpy, scipy e ou similares.

## Apresentação e Visualização
Crie uma visualização interativa ou um relatório claro com:
-  Série histórica dos preços
-  Retornos diários
-  Indicadores calculados
-  Gráficos comparativos entre os ativos

Sugestões:
- Biblioteca Python: Plotly, Matplotlib, Seaborn, Streamlit
- Alternativa: Exportar relatório em PDF ou HTML com gráficos, como
C3/D3js. Jupyter Notebook com Markdown + gráficos é permitido.
