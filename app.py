
import streamlit as st
from alavancagem import alavancagem_banca

st.set_page_config(page_title="Alavancagem de Banca", layout="centered")
st.title("🚀 Simulador de Alavancagem de Banca")

st.markdown("""
Este simulador aplica a estratégia de **10 apostas consecutivas** para alavancar sua banca.
- Primeira aposta: 10% da banca
- Apostas seguintes: valor anterior + 3% da banca inicial
- Odds fixas (ex: 2.0)
- Meta: aumentar em ~50% ou mais ao fim das 10 apostas
""")

banca = st.number_input("💰 Valor da banca inicial (R$):", min_value=10.0, value=100.0, step=10.0)
odd = st.number_input("🎯 Odd fixa de cada aposta:", min_value=1.01, value=2.0, step=0.01)

if st.button("Simular Alavancagem"):
    resultados = alavancagem_banca(banca, odd)
    st.subheader("📊 Resultado por Rodada:")
    for r in resultados:
        st.write(f"Rodada {r['rodada']}: Apostado R${r['apostado']:.2f} | Lucro R${r['ganho']:.2f} | Total R${r['lucro acumulado']:.2f}")

    st.success(f"✅ Lucro total ao fim da alavancagem: R$ {resultados[-1]['lucro acumulado']:.2f}")
