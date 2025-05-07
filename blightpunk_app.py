
import streamlit as st
import random

# ==== Importar tudo que já funciona no seu código base ====
from teste import (
    sorteio_idade, sorteio_fardo, distribuir_atributos, exibir_habilidades,
    sorteio_cortina, sortear_estigmas, etat_de_fortune_d10, ce_quil_reste,
    fardos_oficiais
)

st.set_page_config(page_title="Gerador de Personagem – Blightpunk", layout="centered")
st.title("🕯️ Gerador de Personagem – Blightpunk")

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

    st.subheader("1. Idade")
    st.write(f"{idade} (D4: {idade_d4})")

    st.subheader("2. Fardo e Arcano")
    st.write(f"**{fardo_nome}**  ")
    st.write(f"Arcano: *{arcano}*")

    st.subheader("3. Atributos")
    for k, v in atributos.items():
        st.write(f"{k}: {v}")

    st.subheader("4. Habilidades")
    for nome, valor in habilidades:
        st.write(f"{nome}: +{valor}%")

    st.subheader("5. Alinhamento (Cortina)")
    st.write(f"{cortina} (D4: {cortina_d4})")

    st.subheader("6. Estigmas")
    for est in estigmas:
        st.markdown(f"**[{est['Tipo']}] {est['Nome']} – Grau {est['Grau']}** (Rolagem: {est['Rolagem']})")
        st.markdown(f"→ {est['Descrição']}")

    st.subheader("8. Estado de Fortuna")
    st.write(f"{fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}")

    st.subheader("9. Ce qu’il reste de moi")
    st.write(f"{plaie} (D30: {plaie_roll})")

    st.success("Personagem Revelado!")

else:
    st.info("Clique no botão acima para gerar um novo personagem.")
