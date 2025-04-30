import streamlit as st
import plotly.express as px
from nasa_api import consultar_radiacao

st.title("Consulta Casa Solar :sunrise_over_mountains:")
st.divider()

with st.form("form"):
    cidade = st.text_input("Cidade", placeholder="Digite o nome da cidade")
    estado = st.text_input("Estado", placeholder="Digite o nome do estado")
    latitude = st.number_input("Latitude", format="%.6f", step=0.000001, value=0.0)
    longitude = st.number_input("Longitude", format="%.6f", step=0.000001, value=0.0)
    potencia = st.number_input("Potência do sistema (kWp)", format="%.2f", step=0.01, value=0.0)
    inclinacao = st.number_input("Inclinação dos painéis (graus)", format="%.2f", step=0.01, value=0.0)
    preco_distribuidora = st.number_input("Preço do kWh da distribuidora (R$)", format="%.2f", step=0.01, value=0.0)
    custo_instalacao = st.number_input("Custo estimado de instalação (R$)", format="%.2f", step=0.01, value=0.0)

    submit_button = st.form_submit_button("Enviar")

if submit_button:
    st.subheader("🔎 Resultados da Simulação")

    # Consulta à NASA
    insolacao_media = consultar_radiacao(latitude, longitude)

    if insolacao_media:
        # Cálculos
        rendimento_medio = 0.75  # eficiência média
        energia_diaria = potencia * insolacao_media * rendimento_medio
        energia_mensal = energia_diaria * 30
        energia_anual = energia_mensal * 12
        economia_mensal = energia_mensal * preco_distribuidora
        economia_anual = economia_mensal * 12
        co2_ano = energia_anual * 0.084  # 84g por kWh = 0.084 kg
        roi = (economia_anual / custo_instalacao) * 100 if custo_instalacao > 0 else 0
        area_painel_m2 = 2.54 * 1.134  # ≈ 2.882 m²
        numero_paineis = round(potencia / 0.55)  # Painéis de 500 W
        area_ocupada = numero_paineis * area_painel_m2

        # Exibição
        st.markdown(f"☀️ **Radiação solar média diária:** `{insolacao_media} kWh/m²/dia`")
        st.markdown(f"🔢 **Número estimado de painéis:** `{numero_paineis}`")
        st.markdown(f"🧱 **Área estimada ocupada:** `{area_ocupada:.2f} m²`")
        st.markdown(f"⚡ **Geração mensal estimada:** `{energia_mensal:.2f} kWh`")
        st.markdown(f"💰 **Economia mensal estimada:** `R$ {economia_mensal:.2f}`")
        st.markdown(f"📆 **Economia anual estimada:** `R$ {economia_anual:.2f}`")
        st.markdown(f"🌱 **CO₂ evitado por ano:** `{co2_ano:.2f} kg`")
        st.markdown(f"📈 **Retorno sobre investimento (ROI):** `{roi:.1f}%`")
        
        # Gráfico de economia acumulada
        anos = list(range(1, 11))
        economia_anos = [economia_anual * ano for ano in anos]
        co2_anos = [co2_ano * ano for ano in anos]

        fig1 = px.line(x=anos, y=economia_anos, labels={"x": "Ano", "y": "R$ acumulado"}, title="Economia acumulada (10 anos)")
        fig2 = px.line(x=anos, y=co2_anos, labels={"x": "Ano", "y": "CO₂ (kg)"}, title="CO₂ evitado acumulado (10 anos)")

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
    
    else:
        st.error("Erro ao consultar a API da NASA. Verifique as coordenadas.")
