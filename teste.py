
import random
import pandas as pd

# === PASSO 1 – Idade ===
def sorteio_idade():
    idade_d4 = random.randint(1, 4)
    idades = {
        1: "18-20",
        2: "21–40",
        3: "41–60",
        4: "60+"
    }
    return idade_d4, idades[idade_d4]

# === PASSO 2 – Fardo ===
fardos_oficiais = {
    0: ("L’Artiste (O Artista)", "Le Mat (O Louco)"),
    1: ("L’Occultiste (O Ocultista)", "Le Bateleur (O Mago)"),
    2: ("Le Cryptographe (O Criptógrafo)", "La Papesse (A Papisa)"),
    3: ("L’Enflammé (O Inflamado)", "L’Impératrice (A Imperatriz)"),
    4: ("Le Soldat (O Soldado)", "L’Empereur (O Imperador)"),
    5: ("Le Pestifeur (O Pestífero)", "Le Pape (O Papa)"),
    6: ("L’Agent (O Agente)", "L’Amoureux (Os Amantes)"),
    7: ("Le Professeur (O Professor)", "Le Chariot (O Carro)"),
    8: ("Le Vicaire (O Vigário)", "La Justice (A Justiça)"),
    9: ("Le Marin (O Marinheiro)", "L’Hermite (O Eremita)"),
    10: ("Le Savant (O Cientista)", "La Roue de Fortune (A Roda da Fortuna)"),
    11: ("L’Ombresang (A Sombra Sangrenta)", "La Force (A Força)"),
    12: ("Le Fossoyeur (O Coveiro)", "Le Pendu (O Enforcado)"),
    13: ("Le Mort (O Morto)", "L’Arcane Sans Nom (O Arcano Sem Nome)"),
    14: ("Le Docteur (O Médico)", "Tempérance (A Temperança)"),
    15: ("Le Paysan (O Camponês)", "Le Diable (O Diabo)"),
    16: ("Le Truand (O Malandro)", "La Maison Dieu (A Torre)"),
    17: ("Le Messager (O Mensageiro)", "L’Étoile (A Estrela)"),
    18: ("La Costurière (A Costureira)", "La Lune (A Lua)"),
    19: ("Le Marchand (O Mercador)", "Le Soleil (O Sol)"),
    20: ("Le Journaliste (O Jornalista)", "Le Jugement (O Julgamento)"),
    21: ("Le Machiniste (O Maquinista)", "Le Monde (O Mundo)")
}

def sorteio_fardo():
    fardo_id = random.randint(0, 21)
    return fardo_id, fardos_oficiais[fardo_id]

# === PASSO 3 – Atributos com Modificadores Aplicados ===
def distribuir_atributos(idade_d4):
    nomes_atributos = {
        "Corps": "Corpo",
        "Clarté": "Clareza",
        "Raisonnement": "Raciocínio",
        "Présence": "Presença"
    }

    atributos = {k: 30 for k in nomes_atributos.keys()}
    pontos = 80

    while pontos > 0:
        escolha = random.choice(list(atributos.keys()))
        if atributos[escolha] < 80:
            atributos[escolha] += 1
            pontos -= 1

    modificadores = {
        1: {"Présence": 5, "Raisonnement": -5},
        2: {},
        3: {},
        4: {"Raisonnement": 5, "Corps": -5}
    }.get(idade_d4, {})

    atributos_modificados = {}
    for k in atributos:
        mod = modificadores.get(k, 0)
        valor_final = atributos[k] + mod
        atributos_modificados[f"{k} ({nomes_atributos[k]})"] = {
            "final": valor_final,
            "mod": mod
        }

    return atributos_modificados
