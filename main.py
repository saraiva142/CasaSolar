import streamlit as st

def CasaSolar():
    st.title("Casa Solar :sunrise_over_mountains:")
    st.divider()
    st.write("Simulador de Geração Solar Residencial :house_with_garden:")
    st.write("Aqui você pode calcular a geração de energia solar para sua casa usando os dados da :blue[Nasa] :rocket:.")
    st.header(":dart: Objetivo:")
    st.write("Permitir ao usuário estimar a produção mensal/anual de energia solar e o retorno financeiro de uma instalação em qualquer cidade do mundo.")
    
    st.divider()
    
    st.header(":page_with_curl: Como Funciona:")
    st.write("Na página :blue[Consulta] você pode inserir os dados de sua residência. O sistema irá calcular a produção de energia e o retorno financeiro com base nos dados fornecidos.")
    
    st.markdown(
        """
        <style>
        .footer {
            position: relative;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            font-size: 12px;
            color: gray;
            padding: 10px 0;
            margin-top: 50px;
        }
        </style>
        <div class="footer">
            Desenvolvido por João Saraiva 👨‍💻
        </div>
        """,
        unsafe_allow_html=True
    )
    

pg = st.navigation([CasaSolar, "Consulta.py"])
pg.run()