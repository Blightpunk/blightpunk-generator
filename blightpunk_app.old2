
import streamlit as st
import random
import io
import base64
import teste
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
    c.drawImage(fardo, 15*cm, 20*cm, width=4.5*cm, height=6.5*cm, preserveAspectRatio=True, mask='auto')
    c.setFont("EBGaramond", 13)
    from reportlab.pdfgen.textobject import PDFTextObject

text_obj = c.beginText(x, y)
text_obj.setFont("EBGaramond", 13)

max_width = A4[0] - (x + 2.5*cm)  # margem direita de 2.5cm

for linha in texto.split('\n'):
    if y < 2 * cm:
        c.drawText(text_obj)
        c.showPage()
        c.drawImage(fundo, 0, 0, width=A4[0], height=A4[1])
        c.setFont("EBGaramond", 13)
        text_obj = c.beginText(x, 27 * cm)
        text_obj.setFont("EBGaramond", 13)
        y = 27 * cm

    while linha:
        for i in range(len(linha), 0, -1):
            if c.stringWidth(linha[:i], "EBGaramond", 13) < max_width:
                break
        text_obj.textLine(linha[:i])
        linha = linha[i:]
        y -= 0.7 * cm

c.drawText(text_obj)
    c.save()
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="Blightpunk – Revelação de Fardo", layout="wide")
st.title("🔯 Revelação de Fardo – Blightpunk")
st.markdown("---")

if "personagem" not in st.session_state:
    if st.button("📜 Revelar Fardo"):
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
        st.session_state.personagem = {
            "idade_d4": idade_d4, "idade": idade,
            "fardo_id": fardo_id, "fardo_nome": fardo_nome, "arcano": arcano,
            "img_path": img_path, "atributos": atributos,
            "habilidades": habilidades, "cortina_d4": cortina_d4, "cortina": cortina,
            "estigmas": estigmas, "fortune_roll": fortune_roll,
            "fortune_etat": fortune_etat, "faixa": faixa,
            "plaie_roll": plaie_roll, "plaie": plaie,
            "obj_roll": obj_roll, "obj_nome": obj_nome, "obj_tipo": obj_tipo,
            "obj_dano": obj_dano, "obj_regra": obj_regra
        }

if "personagem" in st.session_state:
    p = st.session_state.personagem
    st.image(p["img_path"], caption=p["arcano"], width=300)

    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.subheader("1. Idade")
        st.write(f"{p['idade']} (D4: {p['idade_d4']})")
    with col2:
        st.subheader("2. Fardo")
        st.write(f"{p['fardo_nome']}")
    with col3:
        st.subheader("3. Arcano")
        st.write(f"{p['arcano']}")

    st.markdown("---")
    st.subheader("Atributos")
    col4, col5 = st.columns(2)
    atributos_items = list(p["atributos"].items())
    for k, v in atributos_items[:len(atributos_items)//2]:
        mod = f" (+{v['mod']})" if v['mod'] > 0 else f" ({v['mod']})" if v['mod'] < 0 else ""
        col4.write(f"{k}: {v['final']}{mod}")
    for k, v in atributos_items[len(atributos_items)//2:]:
        mod = f" (+{v['mod']})" if v['mod'] > 0 else f" ({v['mod']})" if v['mod'] < 0 else ""
        col5.write(f"{k}: {v['final']}{mod}")

    st.subheader("Habilidades")
    col6, col7 = st.columns(2)
    for i, (nome, valor) in enumerate(p["habilidades"]):
        (col6 if i % 2 == 0 else col7).write(f"{nome}: +{valor}%")

    st.subheader("Alinhamento (Cortina)")
    st.write(f"{p['cortina']} (D4: {p['cortina_d4']})")

    st.subheader("Estigmas")
    for est in p["estigmas"]:
        st.markdown(f"**[{est['Tipo']}] {est['Nome']} – Grau {est['Grau']}** (Rolagem: {est['Rolagem']})")
        st.markdown(f"→ {est['Descrição']}")

    col8, col9 = st.columns(2)
    with col8:
        st.subheader("Estado de Fortuna")
        st.write(f"{p['fortune_etat']} (D10: {p['fortune_roll']}) → Sucesso: {p['faixa']}")
    with col9:
        st.subheader("Ce qu’il reste de moi (O que restou de mim)")
        st.write(f"{p['plaie']} (D30: {p['plaie_roll']})")
        st.subheader("Ce que ma main a trouvé (O que a mão achou)")
        st.write(f"Objeto #{p['obj_roll']:02d}: {p['obj_nome']}")
        st.write(f"→ Tipo: {p['obj_tipo']} | Dano: {p['obj_dano']}")
        if p['obj_regra']:
            st.warning(f"⚠️ Regra Especial: {p['obj_regra']}")

    conteudo = io.StringIO()
    conteudo.write("████████████████████████████████████████████\n")
    conteudo.write("           FICHA DE FARDO – BLIGHTPUNK\n")
    conteudo.write("████████████████████████████████████████████\n\n")
    conteudo.write(f"→ Âge: {p['idade']} (D4: {p['idade_d4']})\n→ Fardeau: {p['fardo_nome']}\n→ Arcane: {p['arcano']}\n\n")
    conteudo.write("ATTRIBUTS:\n")
    for k, v in p["atributos"].items():
        mod = v["mod"]
        bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
        conteudo.write(f"{k}: {v['final']}{bonus}\n")
    conteudo.write("\nCOMPÉTENCES:\n")
    for nome, valor in p["habilidades"]:
        conteudo.write(f"- {nome}: +{valor}%\n")
    conteudo.write(f"\nALIGNEMENT: {p['cortina']} (D4: {p['cortina_d4']})\n\n")
    conteudo.write("STIGMATES:\n")
    for est in p["estigmas"]:
        conteudo.write(f"[{est['Tipo']}] {est['Nome']} — Grau {est['Grau']}\n→ {est['Descrição']}\n")
    conteudo.write(f"\nÉTAT DE FORTUNE: {p['fortune_etat']} (D10: {p['fortune_roll']}) → Sucesso: {p['faixa']}\n")
    conteudo.write(f"CE QU’IL RESTE DE MOI: {p['plaie']} (D30: {p['plaie_roll']})\n\n")
    conteudo.write(f"OBJET: {p['obj_nome']} (#{p['obj_roll']:02d})\n→ Tipo: {p['obj_tipo']} | Dano: {p['obj_dano']}\n")
    if p['obj_regra']:
        conteudo.write(f"⚠️ Regra Especial: {p['obj_regra']}\n")
    conteudo.write("\nARCHIVE DU FARD — PARIS, 1919\n")

    buffer = io.BytesIO()
    buffer.write(conteudo.getvalue().encode("utf-8"))
    buffer.seek(0)

    pdf_file = gerar_pdf_com_fundo(conteudo.getvalue(), "images/papel_velho.jpg", p["img_path"])

    col_txt, col_pdf = st.columns(2)
    with col_txt:
        st.download_button("📜 Baixar Ficha .txt", data=buffer, file_name="ficha_blightpunk.txt", mime="text/plain")
    with col_pdf:
        st.download_button("📄 Baixar PDF", data=pdf_file, file_name="ficha_blightpunk.pdf", mime="application/pdf")
