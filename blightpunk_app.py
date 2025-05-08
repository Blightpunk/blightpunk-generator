import streamlit as st
import random
import io
import importlib
import teste  # importa o módulo inteiro
importlib.reload(teste)  # força recarregamento sempre que o app roda
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('EBGaramond', 'fonts/EBGaramond-Regular.ttf'))
def gerar_pdf_com_fundo(texto, imagem_fundo_path):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    fundo = ImageReader(imagem_fundo_path)
    c.drawImage(fundo, 0, 0, width=A4[0], height=A4[1])
    c.setFont("EBGaramond", 11)
    x = 2.5 * cm
    y = 27 * cm

    for linha in texto.split('\n'):
        if y < 2 * cm:
            c.showPage()
            c.drawImage(fundo, 0, 0, width=A4[0], height=A4[1])
            c.setFont("EBGaramond", 11)
            y = 27 * cm
        c.drawString(x, y, linha)
        y -= 0.55 * cm

    c.save()
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="Blightpunk – Revelação de Fardo", layout="wide")
st.title("🕯️ Revelação de Fardo – Blightpunk")
st.markdown("---")

if "gerado" not in st.session_state:
    st.session_state.gerado = False

def gerar_personagem():
    st.session_state.gerado = True

st.button("📜 Revelar Fardo", on_click=gerar_personagem)

if st.session_state.gerado:
    idade_d4, idade = teste.sorteio_idade()
    fardo_id, (fardo_nome, arcano) = teste.sorteio_fardo()
    atributos = teste.distribuir_atributos(idade_d4)
    habilidades = teste.exibir_habilidades(fardo_id)
    cortina_d4, cortina = teste.sorteio_cortina(fardo_id)
    estigmas = teste.sortear_estigmas()
    fortune_roll, fortune_etat, faixa = teste.etat_de_fortune_d10()
    plaie_roll, plaie = teste.ce_quil_reste()
    obj_roll, obj_nome, obj_tipo, obj_dano, obj_regra = teste.sortear_objeto_d100()
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
        st.subheader("Ce qu’il reste de moi (O que restou de mim)")
        st.write(f"{plaie} (D30: {plaie_roll})")
        st.subheader("Objet trouvé au commencement")
    st.success("Personagem Revelado!")
    export_text = io.BytesIO()
    conteudo = ""
    conteudo += "████████████████████████████████████████████\n"
    conteudo += "           FICHA DE FARDO – BLIGHTPUNK\n"
    conteudo += "████████████████████████████████████████████\n\n"

    conteudo += "ID DA REVELAÇÃO\n"
    conteudo += f"→ Âge (Idade): {idade} (D4: {idade_d4})\n"
    conteudo += f"→ Fardeau (Fardo): {fardo_nome}\n"
    conteudo += f"→ Arcane (Arcano): {arcano}\n\n"

    conteudo += "────────────────────────────────────────────\n"
    conteudo += "ATTRIBUTS (ATRIBUTOS)\n"
    conteudo += "────────────────────────────────────────────\n"
    for k, v in atributos.items():
        val = v["final"]
        mod = v["mod"]
        bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
        conteudo += f"{k}: {val}{bonus}\n"

    conteudo += "\n────────────────────────────────────────────\n"
    conteudo += "COMPÉTENCES (HABILIDADES)\n"
    conteudo += "────────────────────────────────────────────\n"
    for nome, valor in habilidades:
        conteudo += f"- {nome}: +{valor}%\n"

    conteudo += "\n────────────────────────────────────────────\n"
    conteudo += "ALIGNEMENT (CORTINA)\n"
    conteudo += "────────────────────────────────────────────\n"
    conteudo += f"{cortina} (D4: {cortina_d4})\n"

    conteudo += "\n────────────────────────────────────────────\n"
    conteudo += "STIGMATES (ESTIGMAS)\n"
    conteudo += "────────────────────────────────────────────\n"
    for est in estigmas:
        conteudo += f"[{est['Tipo']}] {est['Nome']} — Grau {est['Grau']} (Rolagem: {est['Rolagem']})\n"
        conteudo += f"→ {est['Descrição']}\n"

    conteudo += "\n────────────────────────────────────────────\n"
    conteudo += "ÉTAT DE FORTUNE (ESTADO DE FORTUNA)\n"
    conteudo += "────────────────────────────────────────────\n"
    conteudo += f"{fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}\n"

    conteudo += "\n────────────────────────────────────────────\n"
    conteudo += "CE QU’IL RESTE DE MOI (O QUE RESTOU DE MIM)\n"
    conteudo += "────────────────────────────────────────────\n"
    conteudo += f"{plaie} (D30: {plaie_roll})\n\n"

    conteudo += "────────────────────────────────────────────\n"
    conteudo += "OBJET TROUVÉ AU COMMENCEMENT (OBJETO ENCONTRADO)\n"
    conteudo += "────────────────────────────────────────────\n"
    conteudo += f"{obj_nome} (#{obj_roll:02d})\n"
    conteudo += f"→ Tipo: {obj_tipo} | Dano: {obj_dano}\n"
    if obj_regra:
        conteudo += f"⚠️ Regra Especial: {obj_regra}\n"
    conteudo += "\n"

    conteudo += "────────────────────────────────────────────\n"
    conteudo += "ARCHIVE DU FARD — PARIS, 1919\n"

    export_text.write(conteudo.encode('utf-8'))
    pdf_arquivo = gerar_pdf_com_fundo(conteudo, "images/papel_velho.jpg")
    col_txt, col_pdf = st.columns(2)

    with col_txt:
        st.download_button(
            label="📜 Baixar Ficha em .txt",
            data=export_text.getvalue(),
            file_name="ficha_blightpunk.txt",
            mime="text/plain"
        )

    with col_pdf:
        st.download_button(
            label="📄 Baixar Ficha em PDF",
            data=pdf_arquivo,
            file_name="ficha_blightpunk.pdf",
            mime="application/pdf"
        )

