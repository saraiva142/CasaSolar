# ☀️ Simulador de Instalação Fotovoltaica com Dados da NASA POWER

Este projeto é um **simulador interativo** de geração de energia solar para residências, desenvolvido em **Python** com **Streamlit**, utilizando dados reais da **NASA POWER API**.

## 🚀 Funcionalidades

- Consulta automática da **radiação solar média diária** para qualquer localização
- Cálculo da **geração mensal/anual de energia (kWh)**
- Estimativa da **economia financeira** e **ROI**
- Cálculo do **CO₂ evitado** com uso da energia solar
- Estimativa da **área ocupada pelos painéis** no telhado
- **Gráficos interativos** com Plotly (economia e CO₂ acumulado)

## 📦 Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- NASA POWER API
- Plotly

## 📊 Como Funciona

O usuário informa:

- Cidade e estado **&** latitude/longitude
- Potência do sistema (em kWp)
- Preço do kWh da distribuidora
- Custo estimado da instalação
- Inclinação dos painéis (opcional)

O simulador então:

1. Consulta a radiação solar da NASA para a localização informada
2. Calcula a energia gerada, economia, ROI e impacto ambiental
3. Exibe gráficos e resultados claros e interativos

## 📁 Organização

- `main.py`: Página inicial
- `Consulta.py`: Tela principal de simulação
- `nasa_api.py`: Função de integração com a API da NASA

## 🛰️ Fonte de Dados

Este projeto utiliza dados da [NASA POWER Project](https://power.larc.nasa.gov), que fornece informações geoespaciais para aplicações em energia renovável e clima.

## 💻 Deploy
[CasaSolar](https://casasolar.streamlit.app/)

## 📄 Licença

MIT © João Saraiva
