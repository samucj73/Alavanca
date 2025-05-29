import streamlit as st
from alavancagem import alavancagem_banca

st.set_page_config(page_title="Alavancagem de Banca", layout="centered")

# Centralizar título com HTML
st.markdown("<h1 style='text-align: center;'>🚀 Simulador de Alavancagem de Banca</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center'>
<p>Este simulador aplica a estratégia de <strong>10 apostas consecutivas</strong> para alavancar sua banca.</p>

<h4>💡 Estratégia:</h4>
<ul style='list-style-position: inside; display: inline-block; text-align: left;'>
  <li>Aposta 1: 10% da banca inicial</li>
  <li>Apostas seguintes: <strong>10% da banca inicial + lucro acumulado</strong></li>
  <li>Odds fixas (ex: 2.0)</li>
  <li>Meta: aumentar significativamente ao final da sequência</li>
</ul>
<p>⚠️ Se perder qualquer aposta, a sequência é interrompida.</p>
</div>
""", unsafe_allow_html=True)

banca = st.number_input("💰 Valor da banca inicial (R$):", min_value=10.0, value=100.0, step=10.0)
odd = st.number_input("🎯 Odd fixa de cada aposta:", min_value=1.01, value=2.0, step=0.01)

if st.button("Simular Alavancagem"):
    resultados = alavancagem_banca(banca, odd)
    st.markdown("<h3 style='text-align: center;'>📊 Resultado por Rodada:</h3>", unsafe_allow_html=True)
    for r in resultados:
        st.write(f"Rodada {r['rodada']}: Apostado R${r['apostado']:.2f} | Lucro R${r['ganho']:.2f} | Total R${r['lucro acumulado']:.2f}")
    
    st.success(f"✅ Lucro total ao fim da alavancagem: R$ {resultados[-1]['lucro acumulado']:.2f}")

# Rodapé personalizado
st.markdown("""
<hr>
<p style='text-align: center; font-size: 14px;'>
Desenvolvido por <strong>Grupo Alfa</strong> 🔥 | Todos os direitos reservados © 2025
</p>
""", unsafe_allow_html=True)
