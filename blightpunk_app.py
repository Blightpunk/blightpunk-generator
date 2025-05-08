
import streamlit as st
import random
import io

from teste import (
    sorteio_idade, sorteio_fardo, distribuir_atributos,
    exibir_habilidades, sorteio_cortina, sortear_estigmas,
    etat_de_fortune_d10, ce_quil_reste, fardos_oficiais
)

st.set_page_config(page_title="Blightpunk – Gerador de Personagem", layout="wide")
st.title("🕯️ Gerador de Personagem – Blightpunk")
st.markdown("---")

if "gerado" not in st.session_state:
    st.session_state.gerado = False

def gerar_personagem():
    st.session_state.gerado = True

st.button("📜 Revelar Personagem", on_click=gerar_personagem)

if st.session_state.gerado:
    idade_d4, idade = sorteio_idade()
    fardo_id, (fardo_nome, arcano) = sorteio_fardo()
    atributos = distribuir_atributos(idade_d4)
    habilidades = exibir_habilidades(fardo_id)
    cortina_d4, cortina = sorteio_cortina(fardo_id)
    estigmas = sortear_estigmas()
    fortune_roll, fortune_etat, faixa = etat_de_fortune_d10()
    plaie_roll, plaie = ce_quil_reste()

    st.image(f"images/arcano_{fardo_id}.png", caption=arcano)

    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.subheader("1. Idade")
        st.write(f"{idade} (D4: {idade_d4})")
    with col2:
        st.subheader("2. Fardo")
        st.write(f"{fardo_nome}")
    with col3:
        st.subheader("3. Arcano")
        st.write(f"{arcano}")

    st.markdown("---")
    st.subheader("Atributos")
    col4, col5 = st.columns(2)
    atributos_items = list(atributos.items())
    half = len(atributos_items) // 2
    for k, v in atributos_items[:half]:
        val = v["final"]
        mod = v["mod"]
        bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
        col4.write(f"{k}: {val}{bonus}")
    for k, v in atributos_items[half:]:
        val = v["final"]
        mod = v["mod"]
        bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
        col5.write(f"{k}: {val}{bonus}")

    st.subheader("Habilidades")
    col6, col7 = st.columns(2)
    for i, (nome, valor) in enumerate(habilidades):
        (col6 if i % 2 == 0 else col7).write(f"{nome}: +{valor}%")

    st.subheader("Alinhamento (Cortina)")
    st.write(f"{cortina} (D4: {cortina_d4})")

    st.subheader("Estigmas")
    for est in estigmas:
        st.markdown(f"**[{est['Tipo']}] {est['Nome']} – Grau {est['Grau']}** (Rolagem: {est['Rolagem']})")
        st.markdown(f"→ {est['Descrição']}")

    col8, col9 = st.columns(2)
    with col8:
        st.subheader("Estado de Fortuna")
        st.write(f"{fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}")
    with col9:
        st.subheader("Ce qu’il reste de moi")
        st.write(f"{plaie} (D30: {plaie_roll})")

    st.success("Personagem Revelado!")

    export_text = io.StringIO()
    export_text.write("FICHA DE PERSONAGEM – BLIGHTPUNK\n\n")
    export_text.write(f"Idade: {idade} (D4: {idade_d4})\n")
    export_text.write(f"Fardo: {fardo_nome}\nArcano: {arcano}\n\n")
    export_text.write("Atributos:\n")
    for k, v in atributos.items():
        val = v["final"]
        mod = v["mod"]
        bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
        export_text.write(f"- {k}: {val}{bonus}\n")
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
