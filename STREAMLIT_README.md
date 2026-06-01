# 📊 Dashboard Streamlit - Análise de Risco Financeiro

Dashboard interativo para visualização de indicadores de risco de ativos financeiros brasileiros.

## 🚀 Como Executar

### Opção 1: Script Bash (Linux/Mac)
```bash
chmod +x run_dashboard.sh
./run_dashboard.sh
```

### Opção 2: Comando Direto
```bash
# Com virtual environment
.venv/bin/streamlit run app.py

# Sem virtual environment
streamlit run app.py
```

### Opção 3: Docker (em desenvolvimento)
```bash
docker build -t risk-control-app .
docker run -p 8501:8501 risk-control-app
```

## 📌 Acesso

O dashboard estará disponível em:
- **Local**: http://localhost:8501
- **Remoto**: `http://<seu-ip>:8501`

## 📊 Funcionalidades

### 1. 📈 Resumo (Tab 1)
- Cards com métricas principais por ativo
- Volatilidade anualizada
- Value at Risk (VaR) a 95%
- Retornos acumulados
- Estatísticas descritivas (Skewness, Kurtosis)

### 2. 📈 Série Histórica (Tab 2)
- Gráficos de preços de fechamento
- Série de retornos logarítmicos diários
- Análise temporal (últimos 6 meses)
- Zoom e interação com Plotly

### 3. 📉 Distribuição (Tab 3)
- Histogramas de retornos diários
- Estatísticas descritivas por ativo
- Min, máximo, mediana, desvio padrão

### 4. 🔗 Correlação (Tab 4)
- Heatmap da matriz de correlação
- Interpretação de valores
- Tabela detalhada de correlações
- Identificação de relações entre ativos

### 5. 🎯 Comparativo (Tab 5)
- Gráfico comparativo de métricas
- Ranking de ativos
- Resumo completo com todas as métricas

## ⚙️ Configurações (Barra Lateral)

- **Selecionar Ativos**: Escolha quais ativos analisar
- **Métrica de Comparação**: Volatilidade, VaR ou Retorno
- **Informações**: Descrição dos indicadores

## 📊 Indicadores Disponíveis

| Indicador | Descrição |
|-----------|-----------|
| **Volatilidade** | Desvio padrão anualizado dos retornos |
| **VaR 95%** | Perda máxima esperada com 95% confiança |
| **Retorno Acumulado** | Retorno total no período de 6 meses |
| **Correlação** | Relação linear entre retornos de ativos |
| **Skewness** | Assimetria da distribuição de retornos |
| **Kurtosis** | Caudas da distribuição de retornos |

## 🔄 Workflow

```
1. Executar pipeline:    python3 pipeline/main_pipeline.py
2. Gerar dados:          Baixa dados com yfinance
3. Calcular indicadores: Volatilidade, VaR, Correlação
4. Salvar resultados:    JSON, CSV
5. Executar dashboard:   streamlit run app.py
6. Visualizar:           Browser em localhost:8501
```

## 📁 Estrutura de Dados

O app lê dados de:
```
pipeline/data/processed/
├── PETR4_SA_processed.csv      # Preços e retornos
├── VALE3_SA_processed.csv
├── WEGE3_SA_processed.csv
├── indicadores_risco.json      # Métricas calculadas
└── matriz_correlacao.csv       # Correlações
```

## 🎨 Personalização

### Temas
Edite `app.py` para alterar o tema:
```python
# Temas disponíveis: light, dark
st.set_page_config(
    page_title="📊 Análise de Risco Financeiro",
    page_icon="📊",
    layout="wide"
)
```

### Cores e Estilos
Modifique a seção CSS:
```python
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        ...
    }
    </style>
""", unsafe_allow_html=True)
```

## 🐛 Troubleshooting

### Porta 8501 já está em uso
```bash
streamlit run app.py --server.port 8502
```

### Dados não aparecem
```bash
# Certifique-se que o pipeline foi executado
python3 pipeline/main_pipeline.py

# Verifique os arquivos
ls -la pipeline/data/processed/
```

### Módulos faltando
```bash
# Instale dependências
pip install -r requirements.txt

# Ou com venv
.venv/bin/pip install -r requirements.txt
```

## 📈 Performance

- **Carregamento**: ~2-3 segundos
- **Cálculos**: Utilizados `@st.cache_data` para otimização
- **Responsividade**: Interações em tempo real

## 🔒 Segurança

- Não há chaves de API expostas
- Dados locais no diretório `pipeline/data/`
- Cache local do Streamlit

## 📝 Próximas Melhorias

- [ ] Exportar relatórios em PDF
- [ ] Download de dados processados
- [ ] Análise de risco em carteira
- [ ] Simulação de cenários
- [ ] Integração com banco de dados
- [ ] Autenticação de usuários

## 👨‍💻 Desenvolvimento

Para editar o app:
```bash
# Modo watch automático
streamlit run app.py --logger.level=debug
```

Qualquer mudança em `app.py` será recarregada automaticamente.

## 📞 Suporte

Para problemas, verifique:
1. Logs do Streamlit: `streamlit logs`
2. Terminal de execução
3. Arquivos de dados em `pipeline/data/processed/`

---

**Desenvolvido com ❤️ usando Streamlit, Plotly e yfinance**
