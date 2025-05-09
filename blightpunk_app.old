import streamlit as st
import random
import io
import base64
import teste
import streamlit.components.v1 as components
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('EBGaramond', 'fonts/EBGaramond-Regular.ttf'))

def gerar_pdf_com_fundo(texto, imagem_fundo_path, imagem_fardo_path):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    fundo = ImageReader(imagem_fundo_path)
    fardo = ImageReader(imagem_fardo_path)
    c.drawImage(fundo, 0, 0, width=A4[0], height=A4[1])
    c.drawImage(fardo, 13.5*cm, 26.5*cm, width=4.5*cm, height=6.5*cm, preserveAspectRatio=True, mask='auto')
    c.setFont("EBGaramond", 13)
    x, y = 2.5 * cm, 27 * cm

    for linha in texto.split('\n'):
        if y < 2 * cm:
            c.showPage()
            c.drawImage(fundo, 0, 0, width=A4[0], height=A4[1])
            c.setFont("EBGaramond", 13)
            y = 27 * cm
        c.drawString(x, y, linha)
        y -= 0.7 * cm

    c.save()
    buffer.seek(0)
    return buffer

def img_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(page_title="Blightpunk – Revelação de Fardo", layout="wide")
st.markdown(
    """
    <style>
    .botao-flutuante {
        position: fixed;
        bottom: 40px;
        right: 40px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True
)

if "gerado" not in st.session_state:
    st.session_state.gerado = False

st.title("🔯 Revelação de Fardo – Blightpunk")
st.markdown("---")

if st.button("📜 Revelar Fardo", key="botao_gerar", help="Clique para revelar seu personagem"):
    st.session_state.gerado = True

if st.session_state.gerado:
    idade_d4, idade = teste.sorteio_idade()
    fardo_id, (fardo_nome, arcano) = teste.sorteio_fardo()
    img_path = f"images/arcano_{fardo_id}.png"
    atributos = teste.distribuir_atributos(idade_d4)
    habilidades = teste.exibir_habilidades(fardo_id)
    cortina_d4, cortina = teste.sorteio_cortina(fardo_id)
    estigmas = teste.sortear_estigmas()
    fortune_roll, fortune_etat, faixa = teste.etat_de_fortune_d10()
    plaie_roll, plaie = teste.ce_quil_reste()
    obj_roll, obj_nome, obj_tipo, obj_dano, obj_regra = teste.sortear_objeto_d100()

    st.image(img_path, caption=arcano, width=300)

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
    for k, v in atributos_items[:len(atributos_items)//2]:
        mod = f" (+{v['mod']})" if v['mod'] > 0 else f" ({v['mod']})" if v['mod'] < 0 else ""
        col4.write(f"{k}: {v['final']}{mod}")
    for k, v in atributos_items[len(atributos_items)//2:]:
        mod = f" (+{v['mod']})" if v['mod'] > 0 else f" ({v['mod']})" if v['mod'] < 0 else ""
        col5.write(f"{k}: {v['final']}{mod}")

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
        st.subheader("Ce que ma main a trouvé (O que a mão achou)")
        st.write(f"Objeto #{obj_roll:02d}: {obj_nome}")
        st.write(f"→ Tipo: {obj_tipo} | Dano: {obj_dano}")
        if obj_regra:
            st.warning(f"⚠️ Regra Especial: {obj_regra}")

    st.success("Personagem Revelado!")

    conteudo = io.StringIO()
    conteudo.write("████████████████████████████████████████████\n")
    conteudo.write("           FICHA DE FARDO – BLIGHTPUNK\n")
    conteudo.write("████████████████████████████████████████████\n\n")
    conteudo.write(f"→ Âge: {idade} (D4: {idade_d4})\n→ Fardeau: {fardo_nome}\n→ Arcane: {arcano}\n\n")
    conteudo.write("ATTRIBUTS:\n")
    for k, v in atributos.items():
        mod = v["mod"]
        bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
        conteudo.write(f"{k}: {v['final']}{bonus}\n")
    conteudo.write("\nCOMPÉTENCES:\n")
    for nome, valor in habilidades:
        conteudo.write(f"- {nome}: +{valor}%\n")
    conteudo.write(f"\nALIGNEMENT: {cortina} (D4: {cortina_d4})\n\n")
    conteudo.write("STIGMATES:\n")
    for est in estigmas:
        conteudo.write(f"[{est['Tipo']}] {est['Nome']} — Grau {est['Grau']}\n→ {est['Descrição']}\n")
    conteudo.write(f"\nÉTAT DE FORTUNE: {fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}\n")
    conteudo.write(f"CE QU’IL RESTE DE MOI: {plaie} (D30: {plaie_roll})\n\n")
    conteudo.write(f"OBJET: {obj_nome} (#{obj_roll:02d})\n→ Tipo: {obj_tipo} | Dano: {obj_dano}\n")
    if obj_regra:
        conteudo.write(f"⚠️ Regra Especial: {obj_regra}\n")
    conteudo.write("\nARCHIVE DU FARD — PARIS, 1919\n")

    buffer = io.BytesIO()
    buffer.write(conteudo.getvalue().encode("utf-8"))
    buffer.seek(0)
    pdf_file = gerar_pdf_com_fundo(conteudo.getvalue(), "images/papel_velho.jpg", img_path)

    col_txt, col_pdf = st.columns(2)
    with col_txt:
        st.download_button("📜 Baixar Ficha .txt", data=buffer, file_name="ficha_blightpunk.txt", mime="text/plain")
    with col_pdf:
        st.download_button("📄 Baixar PDF", data=pdf_file, file_name="ficha_blightpunk.pdf", mime="application/pdf")
