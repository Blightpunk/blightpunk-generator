
import streamlit as st
import random
import io

from teste import (
    sorteio_idade, sorteio_fardo, distribuir_atributos, exibir_habilidades,
    sorteio_cortina, sortear_estigmas, etat_de_fortune_d10, ce_quil_reste,
    fardos_oficiais
)

st.set_page_config(page_title="Blightpunk – Gerador de Personagem", layout="wide")
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🕯️ Gerador de Personagem – Blightpunk")
st.markdown("*"O horror não está naquilo que é estranho demais, mas naquilo que se parece demais com a verdade."*  
— H.P. Lovecraft, adaptado por você")

st.markdown("---")

if st.button("📜 Revelar Personagem"):
    idade_d4, idade = sorteio_idade()
    fardo_id, (fardo_nome, arcano) = sorteio_fardo()
    atributos = distribuir_atributos()
    habilidades = exibir_habilidades(fardo_id)
    cortina_d4, cortina = sorteio_cortina(fardo_id)
    estigmas = sortear_estigmas()
    fortune_roll, fortune_etat, faixa = etat_de_fortune_d10()
    plaie_roll, plaie = ce_quil_reste()

    # Bloco superior: Fardo, Arcano, Idade
    st.subheader("Identidade");
    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.write(f"**Idade**: {idade} (D4: {idade_d4})")
    with col2:
        st.write(f"**Fardo**: {fardo_nome}")
    with col3:
        st.write(f"**Arcano**: *{arcano}*")

    st.markdown("---")

    # Atributos
    st.subheader("Atributos")
    col_a1, col_a2 = st.columns(2)
    atributos_items = list(atributos.items())
    half = len(atributos_items) // 2
    for k, v in atributos_items[:half]:
        col_a1.write(f"{k}: {v}")
    for k, v in atributos_items[half:]:
        col_a2.write(f"{k}: {v}")

    # Habilidades
    st.subheader("Habilidades")
    col_h1, col_h2 = st.columns(2)
    for i, (nome, valor) in enumerate(habilidades):
        (col_h1 if i % 2 == 0 else col_h2).write(f"{nome}: +{valor}%")


    st.subheader("Alinhamento (Cortina)")
    st.write(f"{cortina} (D4: {cortina_d4})")


    st.subheader("Estigmas")
    for est in estigmas:
        st.markdown(f"**[{est['Tipo']}] {est['Nome']} – Grau {est['Grau']}** (Rolagem: {est['Rolagem']})")
        st.markdown(f"→ {est['Descrição']}")

    # Fortuna e Ce qu'il reste
    colf1, colf2 = st.columns(2)
    with colf1:
        st.subheader("Estado de Fortuna")
        st.write(f"{fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}")

    with colf2:
        st.subheader("Ce qu’il reste de moi")
        st.write(f"{plaie} (D30: {plaie_roll})")


    st.success("Personagem Revelado!")

    # Exportação para .txt
    export_text = io.StringIO()
    export_text.write(f"FICHA DE PERSONAGEM – BLIGHTPUNK\n\n")
    export_text.write(f"Idade: {idade} (D4: {idade_d4})\n")
    export_text.write(f"Fardo: {fardo_nome}\nArcano: {arcano}\n\n")
    export_text.write("Atributos:\n")
    for k, v in atributos.items():
        export_text.write(f"- {k}: {v}\n")
    export_text.write("\nHabilidades:\n")
    for nome, valor in habilidades:
        export_text.write(f"- {nome}: +{valor}%\n")
    export_text.write(f"\nAlinhamento: {cortina} (D4: {cortina_d4})\n\n")
    export_text.write("Estigmas:\n")
    for est in estigmas:
        export_text.write(f"- [{est['Tipo']}] {est['Nome']} – Grau {est['Grau']} (Rolagem: {est['Rolagem']})\n  → {est['Descrição']}\n")
    export_text.write(f"\nEstado de Fortuna: {fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}\n")
    export_text.write(f"Ce qu’il reste de moi: {plaie} (D30: {plaie_roll})\n")


    st.download_button(
        label="💾 Baixar Ficha em .txt",
        data=export_text.getvalue(),
        file_name="ficha_blightpunk.txt",
        mime="text/plain"
    )

else:
    st.info("Clique no botão acima para gerar um novo personagem.")
