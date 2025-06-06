import random


estigmas_fisicos = {
    1: {
        "nome": "Visage Ingrat (Face Ingrata)",
        "graus": [
            "Cicatriz leve, notada em silêncio.",
            "Incomoda interações, perturba a escuta.",
            "Muda a cena com sua simples presença."
        ]
    },
    2: {
        "nome": "Flèche au Genou (Flecha no Joelho)",
        "graus": [
            "Manca levemente, atrasa o grupo.",
            "Movimentos custam, exige ajuda.",
            "Falha automática em ações físicas cruciais."
        ]
    },
    3: {
        "nome": "Souffle de Rouille (Sopro de Ferrugem)",
        "graus": [
            "Tosse discreta, corta o silêncio.",
            "Respiração audível, atrai atenção.",
            "Colapso físico, falha a ação."
        ]
    },
    4: {
        "nome": "Vue Fendue (Visão Rachada)",
        "graus": [
            "Visão embaçada sob pressão.",
            "Percepção falha em detalhes.",
            "Vê errado ou não vê o essencial."
        ]
    },
    5: {
        "nome": "Tremblement (Tremor)",
        "graus": [
            "Mão treme levemente.",
            "Erra por imprecisão.",
            "Deixa cair ou falha sem chance."
        ]
    },
    6: {
        "nome": "Voix Fendue (Voz Fendida)",
        "graus": [
            "Falas interrompidas.",
            "Tom muda ou falha.",
            "Fica sem voz ou fala distorcida."
        ]
    },
    7: {
        "nome": "Regard Fixe (Olhar Fixo)",
        "graus": [
            "Encarar demais cria tensão.",
            "Olha para o lugar errado.",
            "Trava o olhar e perde a ação."
        ]
    },
    8: {
        "nome": "Mâchoires Fermées (Mandíbula Fechada)",
        "graus": [
            "Tensão na mandíbula.",
            "Ranger evidente, altera fala.",
            "Trava completamente a fala."
        ]
    },
    9: {
        "nome": "Nausée Persistante (Náusea Persistente)",
        "graus": [
            "Náusea leve, reação física sutil.",
            "Afasta-se da cena.",
            "Vômito em momento chave da narrativa."
        ]
    },
    10: {
        "nome": "Bourdonnement (Zumbido)",
        "graus": [
            "Zumbido leve, distração auditiva.",
            "Confunde falas ou sons.",
            "Ouve errado, age de forma prejudicial."
        ]
    }
}
estigmas_mentais = {
    1: {
        "nome": "Deuil (Luto)",
        "graus": [
            "Confusão com a ausência — você fala como se alguém morto ainda estivesse vivo.",
            "Resposta fantasma — você reage como se ela estivesse ali.",
            "Presença da perda — você vê ou sente a pessoa, mesmo que ninguém mais veja."
        ]
    },
    2: {
        "nome": "Je n’étais pas là (Não Fui Eu)",
        "graus": [
            "Você nega ter feito algo, mas não tem certeza. Outros têm.",
            "Provas surgem. Um objeto, um cheiro, uma frase familiar.",
            "Você é acusado com força. E talvez comece a duvidar de si mesmo."
        ]
    },
    3: {
        "nome": "Étrange Obsession (Estranha Obsessão)",
        "graus": [
            "Objeto distrai. Você não consegue ignorar.",
            "Você reage com violência se alguém mexer.",
            "Você pega o objeto — mesmo que isso custe tudo."
        ]
    },
    4: {
        "nome": "Ce N’est Pas Lui (Esse Não É Ele)",
        "graus": [
            "Você hesita ao reconhecer alguém querido.",
            "Você acha que ele mente — sempre.",
            "Você age como se aquela pessoa tivesse sido trocada."
        ]
    },
    5: {
        "nome": "Ils ont dit que… (Eles Disseram Que...)",
        "graus": [
            "Uma frase surge. Sussurrada. E você a escuta.",
            "A frase volta. Vira instrução.",
            "A frase se torna verdade. E você age com base nela."
        ]
    },
    6: {
        "nome": "Vérité Insupportable (Verdade Insuportável)",
        "graus": [
            "Você tenta contar sua verdade. Ninguém acredita.",
            "Você insiste. Eles se afastam.",
            "Você age como se aquilo fosse fato — mesmo que perca tudo."
        ]
    },
    7: {
        "nome": "Marqué pour Mourir (Marcado para Morrer)",
        "graus": [
            "Coincidência demais. Algo te persegue.",
            "Ninguém reage aos seus alertas. Todos já aceitaram.",
            "O mundo coopera com sua morte. Você sente."
        ]
    },
    8: {
        "nome": "Mon Cher Bourreau (Meu Querido Algoz)",
        "graus": [
            "Rosto conhecido em corpo estranho.",
            "Frases, gestos, sinais — ele te observa. E guia.",
            "Ele aparece. E você o reconhece. Mesmo que não seja ele."
        ]
    },
    9: {
        "nome": "Tout Est Trop Fort (Tudo é Intenso Demais)",
        "graus": [
            "O mundo machuca. Sons, luzes, toques.",
            "Você reage sem pensar — com fuga, dor, enjoo.",
            "O corpo fecha. Você entra em colapso sensorial."
        ]
    },
    10: {
        "nome": "TOC – Théorème Obsessionnel du Corps (Teorema Obsessivo do Corpo)",
        "graus": [
            "Você precisa contar, alinhar, repetir.",
            "Você não sai enquanto o gesto não termina.",
            "Você prioriza o ritual — mesmo que o mundo quebre ao redor."
        ]
    }
}
estigmas_limiar = {
    1: {
        "nome": "I-1407b (Sim — é a sala do lado)",
        "graus": [
            "Você entra por último e algo está errado. O som, o ar, o tempo — nada encaixa. O grupo jura que você nunca se afastou.",
            "Você vive algo marcante, mas ninguém confirma. Um encontro, uma fala, um toque. Tudo existiu — só pra você.",
            "Portas respiram. Escadas esperam. Você é tragado para outra sala — e devolvido com marcas que ninguém entende."
        ]
    },
    2: {
        "nome": "Scène 2 (A Cena Recomeça)",
        "graus": [
            "Alguém aplaude, cochicha ou comenta sua fala. Você está sendo observado — como se atuasse sem saber.",
            "Você é corrigido no meio de uma frase. Um estranho dita o rumo da cena. Não há roteiro. Mas há direção.",
            "A cena para. Alguém comanda: “Ação.” Tudo recomeça, só para você. E só você sabe que recomeçou."
        ]
    },
    3: {
        "nome": "L’Enfant Est Mon Double (A criança é meu Duplo)",
        "graus": [
            "Desenhos infantis aparecem com cenas que você viveu — ou ainda vai viver.",
            "Reflexos mostram você... criança. Mas ela sangra, sorri ou chora em seu lugar.",
            "Ela está ali. Não é você. Mas todos confundem. E quando chamam seu nome... é ela quem responde."
        ]
    },
    4: {
        "nome": "Le Parfum de Rosie (O Perfume de Rosie)",
        "graus": [
            "Você sente um perfume familiar. Alguém que você amou. Ou que te amou demais.",
            "O cheiro invade sua roupa, sua cama, sua memória. Um nome antigo volta à tona.",
            "Ela está presente. A comida foi feita. O bilhete escrito. E tudo grita que você foi amado — ou assombrado."
        ]
    },
    5: {
        "nome": "Ne Peut Pas Entrer (Ele Não Pode Entrar)",
        "graus": [
            "Você vê alguém parado lá fora. Sem se mexer. Ele não entra. Mas espera.",
            "Ele chama seu nome. Só você ouve. E agora, você tem que decidir: abre ou ignora?",
            "Você recebe um bilhete. Um local. Uma hora. Um convite com sua letra. Se não for... ele virá assim mesmo."
        ]
    },
    6: {
        "nome": "Mercredi, à six heures (Quarta, às seis)",
        "graus": [
            "Toda vez que algo estranho acontece… é quarta. E são seis da tarde.",
            "O relógio marca 5h55. Você sente o corpo falhar. O mundo vai girar de novo.",
            "Quinta chegou. Mas não importa. Você ainda está preso na quarta-feira às seis. E algo ainda não acabou."
        ]
    },
    7: {
        "nome": "Ma Grâce Te Suffit (Minha graça te basta)",
        "graus": [
            "Você faz gestos estranhos. Cruz com sal. Vinho sobre cadáveres. E nem nota.",
            "Frases te escapam. Pessoas reagem como se você fosse um arauto. Você não tem fé — mas a fé age através de você.",
            "Ela aparece. Uma presença aponta. Você obedece — mesmo sabendo que está sendo manipulado. E aceita assim mesmo."
        ]
    },
    8: {
        "nome": "La Chute de l’Ange (A Queda do Anjo)",
        "graus": [
            "Você vê uma figura branca, angelical. Ninguém mais vê. Mas o mundo fica... estranho.",
            "Ele toca os telhados. As pessoas brigam. Você sente que o caos se aproxima.",
            "Ele toca o chão. E o mundo enlouquece. Só você sabe o motivo. Só você enxerga o Anjo. E talvez... você o siga."
        ]
    },
    9: {
        "nome": "Je n’oublie pas ce que j’ai oublié (Eu não esqueço o que esqueci)",
        "graus": [
            "Você faz gestos para alguém que não lembra. Serve um prato extra. Canta para o vazio. Mas faz com carinho.",
            "Objetos reagem. Bilhetes surgem. O mundo responde — como se também lembrasse de quem você esqueceu.",
            "Você encontra um endereço. Uma lembrança nítida — e então esquece. Mas precisa ir até lá. Algo foi dito. Algo foi selado."
        ]
    }
}
estigmas_sociais = {
    1: {
        "nome": "Péchés de Ton Père (Pecados de Teu Pai)",
        "graus": [
            "Olhares desviam quando seu sobrenome surge. Você carrega um passado que fede.",
            "Seu nome trava reuniões. Famílias te evitam. Propostas evaporam ao te reconhecerem.",
            "Você virou símbolo de um erro ancestral. E símbolos não são perdoados — são caçados."
        ]
    },
    2: {
        "nome": "Nom de Dette (Nome de Dívida)",
        "graus": [
            "Você é tratado como devedor, mesmo sem dever nada. Favores cobram silenciosamente.",
            "Seu nome surge em promessas que nunca fez. Recusar ajuda soa como traição.",
            "Você é cobrado por pactos antigos. Culpado por dívidas simbólicas que não reconhece."
        ]
    },
    3: {
        "nome": "Main Mise (Mão Manchada)",
        "graus": [
            "Sua presença pesa. Todos sentem o cheiro do sangue que você derramou.",
            "Seu nome é sussurrado como o de um assassino. Ninguém esqueceu o que você fez.",
            "Você é a encarnação do erro. Alguém precisa pagar. E você é o pagamento vivo."
        ]
    },
    4: {
        "nome": "Complice Silencieux (Cúmplice Silencioso)",
        "graus": [
            "Mesmo dizendo a verdade, sua voz soa falsa. O silêncio que você teve virou sentença.",
            "As pessoas lembram: você estava lá. E não fez nada. Agora, ninguém te ouve.",
            "Sua fala é ruído. Você foi julgado não pelo que disse, mas pelo que não disse."
        ]
    },
    5: {
        "nome": "Tache de Sang (Mancha de Sangue)",
        "graus": [
            "Você sobreviveu. E isso já basta para que te olhem com desprezo.",
            "Dizem que você fugiu. Ou traiu. Que salvou a si mesmo — às custas de outro.",
            "Você é o inimigo invisível. Sua existência é a afronta. E ela exige punição."
        ]
    },
    6: {
        "nome": "Terre Maudite (Terra Maldita)",
        "graus": [
            "Sua terra morreu. Mas você vive. E todos se lembram que você foi embora.",
            "Você não salvou ninguém. Você só saiu correndo. E isso te condena.",
            "Você é o covarde vivo. E toda dor coletiva recai sobre você como herança amarga."
        ]
    },
    7: {
        "nome": "Chassé des Saints (Expulso dos Santos)",
        "graus": [
            "Religiosos hesitam diante de você. A fé encolhe quando você entra.",
            "Rituais falham. Velas apagam. Você é o ruído na oração dos outros.",
            "Você é heresia viva. Há orações contra você. E algumas delas pedem seu fim."
        ]
    },
    8: {
        "nome": "Fissure Inhérente (Fissura Inerente)",
        "graus": [
            "As pessoas veem sua rachadura. Mesmo quando você tenta parecer inteiro.",
            "Ninguém quer estar por perto quando você quebrar de novo. E todos esperam que quebre.",
            "Você é isolado antes mesmo de surtar. O medo é suficiente para te empurrar pro canto."
        ]
    }
}


# === PASSO 1 – Idade ===
def sorteio_idade():
    idade_d4 = random.randint(1, 4)
    idades = {
        1: "18-25",
        2: "26–39",
        3: "40–55",
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
    13: ("Le Mort (O Morto)", "La Mort(A Morte)"),
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


# === PASSO 3 – Atributos (30 base + 80 distribuídos, máx. 80) ===
import random

def distribuir_atributos(idade_d4):
    nomes_atributos = {
        "Corps": "Corpo",              # Força física, resistência, ação
        "Clarté": "Clareza",           # Percepção, atenção, lucidez imediata
        "Sagacité": "Raciocínio",  # Lógica, cálculo, dedução
        "Présence": "Presença"         # Carisma, autoridade, impacto social
    }

    atributos = {k: 30 for k in nomes_atributos.keys()}
    pontos = 80

    while pontos > 0:
        escolha = random.choice(list(atributos.keys()))
        if atributos[escolha] < 80:
            atributos[escolha] += 1
            pontos -= 1

    modificadores = {
        1: {"Présence": 5, "Raisonnement": -5},     # 18–25
        2: {},                                      # 26–39
        3: {"Raisonnement": 5,"Corps": -5},         # 40–55
        4: {"Raisonnement": 10, "Corps": -10}       # 60+
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




# === PASSO 4 – Compétences (com traduções) ===
habilidades_por_fardo = {
    0: ["Improvisation (Improvisação)", "Furtivité (Furtividade)", "Athlétisme (Atletismo)", "Observation (Observação)", "Persuasion (Persuasão)"],
    1: ["Occultisme (Ocultismo)", "Langue Morte (Língua Morta)", "Réception (Recepção)", "Médecine (Medicina)", "Résidu (Resíduo)"],
    2: ["Cryptographie (Criptografia)", "Connaissance (Conhecimento)", "Observation (Observação)", "Langue Morte (Língua Morta)", "Réception (Recepção)"],
    3: ["Improvisation (Improvisação)", "Lancer (Arremesso)", "Persuasion (Persuasão)", "Athlétisme (Atletismo)", "Résidu (Resíduo)"],
    4: ["Corps-à-corps (Combate Corpo a Corpo)", "Tirer (Disparo)", "Athlétisme (Atletismo)", "Résistance (Resistência)", "Navigation (Navegação)"],
    5: ["Tirer (Disparo)", "Résidu (Resíduo)", "Réception (Recepção)", "Médecine (Medicina)", "Observation (Observação)"],
    6: ["Mensonge (Mentira)", "Navigation (Navegação)", "Observation (Observação)", "Persuasion (Persuasão)", "Improvisation (Improvisação)"],
    7: ["Connaissance (Conhecimento)", "Médecine (Medicina)", "Langue Morte (Língua Morta)", "Exorcisme (Exorcismo)", "Résistance (Resistência)"],
    8: ["Autorité (Autoridade)", "Comportement (Comportamento)", "Persuasion (Persuasão)", "Observation (Observação)", "Occultisme (Ocultismo)"],
    9: ["Survie (Sobrevivência)", "Navigation (Navegação)", "Observation (Observação)", "Résistance (Resistência)", "Athlétisme (Atletismo)"],
    10: ["Calcul (Cálculo)", "Connaissance (Conhecimento)", "Verrouillage (Arrombamento Técnico)", "Désamorçage (Desarme)", "Observation (Observação)"],
    11: ["Corps-à-corps (Combate Corpo a Corpo)", "Réception (Recepção)", "Résistance (Resistência)", "Improvisation (Improvisação)", "Symbiose (Simbiose)"],
    12: ["Corps-à-corps (Combate Corpo a Corpo)", "Survie (Sobrevivência)", "Médecine (Medicina)", "Résistance (Resistência)", "Observation (Observação)"],
    13: ["Furtivité (Furtividade)", "Résistance (Resistência)", "Navigation (Navegação)", "Improvisation (Improvisação)", "Observation (Observação)"],
    14: ["Médecine (Medicina)", "Résistance (Resistência)", "Observation (Observação)", "Connaissance (Conhecimento)", "Improvisation (Improvisação)"],
    15: ["Survie (Sobrevivência)", "Athlétisme (Atletismo)", "Observation (Observação)", "Résistance (Resistência)", "Corps-à-corps (Combate Corpo a Corpo)"],
    16: ["Furtivité (Furtividade)", "Mensonge (Mentira)", "Athlétisme (Atletismo)", "Observation (Observação)", "Improvisation (Improvisação)"],
    17: ["Navigation (Navegação)", "Observation (Observação)", "Improvisation (Improvisação)", "Athlétisme (Atletismo)", "Persuasion (Persuasão)"],
    18: ["Improvisation (Improvisação)", "Comportement (Comportamento)", "Médecine (Medicina)", "Observation (Observação)", "Navigation (Navegação)"],
    19: ["Marchandage (Negociação)", "Mensonge (Mentira)", "Navigation (Navegação)", "Observation (Observação)", "Connaissance (Conhecimento)"],
    20: ["Observation (Observação)", "Langue Morte (Língua Morta)", "Persuasion (Persuasão)", "Improvisation (Improvisação)", "Mensonge (Mentira)"],
    21: ["Improvisation (Improvisação)", "Calcul (Cálculo)", "Résistance (Resistência)", "Verrouillage (Arrombamento Técnico)", "Observation (Observação)"]
}



bonus_habilidades = [60, 50, 30, 25, 10]


def exibir_habilidades(fardo_id):
    if fardo_id in habilidades_por_fardo:
        return list(zip(habilidades_por_fardo[fardo_id], bonus_habilidades))
    return []


# === PASSO 5 – Cortina ===
cortinas_por_fardo = {
    0: ["Salon des Refusés (Salão dos Recusados)", "Absinthe Noir (Absinto Negro)", "Le Système Effondré (O Sistema Colapsado)", "Les Sans Serment (Sem Juramento)"],
    1: ["Ordo Nocturne", "Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Маршрутизаторы Незримого (Os que Caminham no Invisível)", "Les Sans Serment (Sem Juramento)"],
    2: ["Ordo Nocturne", "Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "Les Sans Serment (Sem Juramento)"],
    3: ["Enfants de Faust (Filhos de Fausto)", "Brûleurs de Carrelage (Queimadores de Azulejo)", "Absinthe Noir (Absinto Negro)", "Les Sans Serment (Sem Juramento)"],
    4: ["L’État Effondré (O Estado Colapsado)", "La Compagnie des Abandonnés (Companhia dos Abandonados)", "L’Ordre des Marcheurs Silencieux (Ordem dos Que Marcham em Silêncio)", "Les Sans Serment (Sem Juramento)"],
    5: ["Cathédrale du Triumvirat (Catedral do Triunvirato)", "Absinthe Noir (Absinto Negro)", "Les Saints de Paille (Santos de Palha)", "Les Sans Serment (Sem Juramento)"],
    6: ["Ordo Nocturne", "Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "L’État Effondré (O Estado Colapsado)", "Les Sans Serment (Sem Juramento)"],
    7: ["Archivum Obscura", "Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Ordo Nocturne", "Les Sans Serment (Sem Juramento)"],
    8: ["Cathédrale du Triumvirat (Catedral do Triunvirato)", "Absinthe Noir (Absinto Negro)", "Ordo Nocturne", "Les Sans Serment (Sem Juramento)"],
    9: ["Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Ordo Nocturne", "Le Système Effondré (O Sistema Colapsado)", "Les Sans Serment (Sem Juramento)"],
    10: ["Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Ordo Nocturne", "Archivum Obscura", "Les Sans Serment (Sem Juramento)"],
    11: ["Ordo Nocturne", "Absinthe Noir (Absinto Negro)", "Archivum Obscura", "Les Sans Serment (Sem Juramento)"],
    12: ["Cathédrale du Triumvirat (Catedral do Triunvirato)", "Absinthe Noir (Absinto Negro)", "Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "Les Sans Serment (Sem Juramento)"],
    13: ["Les Marcheurs de l’Inconnu (Os Que Marcham no Desconhecido)", "Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "Brûleurs de Carrelage (Queimadores de Azulejo)", "Les Sans Serment (Sem Juramento)"],
    14: ["Ordo Nocturne", "Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Archivum Obscura", "Les Sans Serment (Sem Juramento)"],
    15: ["Cathédrale du Triumvirat (Catedral do Triunvirato)", "Les Saints de Paille (Santos de Palha)", "Le Système Effondré (O Sistema Colapsado)", "Les Sans Serment (Sem Juramento)"],
    16: ["Les Rats de l’Étage (Os Ratos do Sótão)", "Absinthe Noir (Absinto Negro)", "Brûleurs de Carrelage (Queimadores de Azulejo)", "Les Sans Serment (Sem Juramento)"],
    17: ["Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "Absinthe Noir (Absinto Negro)", "Les Sans Serment (Sem Juramento)"],
    18: ["Société d’Éther et de Lumière (Sociedade do Éter e da Luz)", "Absinthe Noir (Absinto Negro)", "Salon des Refusés (Salão dos Recusados)", "Les Sans Serment (Sem Juramento)"],
    19: ["Absinthe Noir (Absinto Negro)", "Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "Les Bouches Pleines (As Bocas Cheias)", "Les Sans Serment (Sem Juramento)"],
    20: ["Bureau de la Mémoire Civile (Gabinete da Memória Civil)", "Le Journal du Juge (O Jornal do Juiz)", "Le Sino Trincado", "Les Sans Serment (Sem Juramento)"],
    21: ["Le Système Effondré (O Sistema Colapsado)", "Brûleurs de Carrelage (Queimadores de Azulejo)", "Absinthe Noir (Absinto Negro)", "Les Sans Serment (Sem Juramento)"]
}



def sorteio_cortina(fardo_id):
    cortinas = cortinas_por_fardo.get(fardo_id, ["Les Sans Serment (Sem Juramento)"])
    escolha = random.choice(cortinas)
    indice = cortinas.index(escolha) + 1
    return indice, escolha



# IMPORTANTE: certifique-se que as bibliotecas estigmas_fisicos, estigmas_mentais, estigmas_limiares e estigmas_sociais
# já foram declaradas antes deste trecho!

def tipo_por_d12(n):
    if n in [1, 2, 3]:
        return "Físico"
    elif n in [4, 5, 6]:
        return "Mental"
    elif n in [7, 8, 9]:
        return "Social"
    elif n in [10, 11, 12]:
        return "Limiar"

def sortear_estigmas():
    estigmas = []
    tipo_count = {"Físico": 0, "Mental": 0, "Social": 0, "Limiar": 0}

    while len(estigmas) < 3:
        tipo = tipo_por_d12(random.randint(1, 12))
        if tipo_count[tipo] >= 2:
            continue

        if tipo == "Físico":
            biblioteca = estigmas_fisicos
        elif tipo == "Mental":
            biblioteca = estigmas_mentais
        elif tipo == "Social":
            biblioteca = estigmas_sociais
        elif tipo == "Limiar":
            biblioteca = estigmas_limiar

        idx = random.randint(1, len(biblioteca))
        grau = random.randint(1, 3)

        nome = biblioteca[idx]["nome"]
        descricao = biblioteca[idx]["graus"][grau - 1]

        # Evita repetir estigma pelo nome
        if any(e["Nome"] == nome for e in estigmas):
            continue

        estigmas.append({
            "Tipo": tipo,
            "Nome": nome,
            "Grau": grau,
            "Rolagem": idx,
            "Descrição": descricao
        })

        tipo_count[tipo] += 1

    return estigmas



# === PASSO 8 – État de Fortune (Estado de Fortuna) ===
def etat_de_fortune_d10():
    roll = random.randint(1, 10)
    if 1 <= roll <= 3:
        return roll, "Misérable (Miserável)", "1 a 3"
    elif 4 <= roll <= 7:
        return roll, "Tant bien que mal (Paga as contas)", "1 a 6"
    else:
        return roll, "Aisé (Afortunado)", "1 a 8"


# === PASSO 9 – Ce qu’il reste de moi(O Que Restou de Mim) (D30) ===
plaies = {
    1: "Um lenço encardido com as iniciais “S.M.” bordadas em dourado.",
    2: "Um pedaço de espelho trincado, com uma inscrição apagada no verso.",
    3: "Um recibo antigo, escrito em tinta quase apagada.",
    4: "Um colar com um dente de leite pendurado por um fio de cobre.",
    5: "Uma carta escrita à mão, sem destinatário.",
    6: "Um retrato fotográfico antigo com três figuras.",
    7: "Uma pulseira hospitalar com nome borrado e número visível.",
    8: "Um botão metálico, ainda preso a um fragmento de tecido carbonizado.",
    9: "Um pedaço de corda com nós desfeitos.",
    10: "Um bilhete costurado por dentro do casaco.",
    11: "Uma aliança quebrada, com marcas de dente.",
    12: "Um laço de cabelo infantil, ressecado.",
    13: "Um papel com um poema, mas só metade está legível.",
    14: "Um número rabiscado repetidas vezes.",
    15: "Um pedaço de osso marcado com símbolos.",
    16: "Uma página de diário escrita de trás para frente.",
    17: "Uma etiqueta de mala com o nome riscado.",
    18: "Uma miniatura de barco ou trem, feito à mão.",
    19: "Um caco de vidro azul escuro.",
    20: "Uma pena embebida em algo seco que já foi vermelho.",
    21: "Um pedaço de vela com fio ainda queimado.",
    22: "Um cartão-postal nunca enviado.",
    23: "Um frasco vazio, mas com cheiro persistente.",
    24: "Uma partitura rasgada com anotações indecifráveis.",
    25: "Um brinco solitário, com pedra rachada.",
    26: "Um pedaço de uniforme ou farda, embolorado.",
    27: "Um envelope lacrado — mas ninguém consegue abrir.",
    28: "Um pente com fios de cabelo antigos.",
    29: "Um diário em branco, exceto pela última página.",
    30: "🕯️ O Inominado – Nada emerge agora. O Condutor te entrega algo durante a primeira sessão."
}


def ce_quil_reste():
    d30 = random.randint(1, 30)
    return d30, plaies[d30]

objetos_abandono = {
    0: {
        "nome": "Garrafa quebrada, ainda cheirando a álcool barato",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    1: {
        "nome": "Pé de cabra com símbolo maçônico",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    2: {
        "nome": "Cruz de madeira com uma lasca solta — já foi empunhada com fé",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    3: {
        "nome": "Tesoura escolar enferrujada",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    4: {
        "nome": "Pá de jardinagem com cabo de osso",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    5: {
        "nome": "Canivete de açougueiro, sem trava",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    6: {
        "nome": "Corrente de portão com gancho adaptado",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    7: {
        "nome": "Bastão de bengala com ponta de chumbo",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    8: {
        "nome": "Estaca de madeira rachada, esculpida às pressas",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    9: {
        "nome": "Revólver velho com apenas uma bala",
        "tipo": "Pistola e revólver",
        "dano": "1D8",
        "regra": "Rolar 1D6 para munição"
    },
    10: {
        "nome": "Machado de lenha com cabo rachado",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    11: {
        "nome": "Ripa de cama com dois pregos tortos",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    12: {
        "nome": "Espingarda de caça enferrujada, sem alça",
        "tipo": "Espingarda",
        "dano": "1D10",
        "regra": "Rolar 1D6 para munição"
    },
    13: {
        "nome": "Pedra amarrada num pano",
        "tipo": "Improvisada",
        "dano": "1D6",
        "regra": ""
    },
    14: {
        "nome": "Navalha de barbear com sangue seco",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    15: {
        "nome": "Faca de cozinha, sem ponta, mas afiada nas beiradas",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    16: {
        "nome": "Chave inglesa média com inscrição “Société Lumière”",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    17: {
        "nome": "Pistola pequena escondida num sapato feminino",
        "tipo": "Pistola e revólver",
        "dano": "1D8",
        "regra": "Rolar 1D6 para munição"
    },
    18: {
        "nome": "Torniquete de ferro usado em amputações",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    19: {
        "nome": "Cabo de guarda-chuva quebrado, com haste em aço pontiagudo",
        "tipo": "Perfurante improvisado",
        "dano": "1D4",
        "regra": ""
    },
    20: {
        "nome": "Pinça de açougue amassada, com pontas afiadas demais para conforto",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    21: {
        "nome": "Cabo de panela de ferro, solto de um fogão abandonado",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    22: {
        "nome": "Pé de cadeira com pregos na ponta",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    23: {
        "nome": "Tesoura de costureira, com ponta lascada",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    24: {
        "nome": "Cajado de madeira com entalhes religiosos — usado pra andar e castigar",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    25: {
        "nome": "Florete de treinamento, usado em academias teatrais",
        "tipo": "Perfurante leve",
        "dano": "1D4",
        "regra": ""
    },
    26: {
        "nome": "Bastão de comando com ponta de latão — símbolo de um soldado degradado",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    27: {
        "nome": "Par de algemas quebradas, uma argola pendurada",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    28: {
        "nome": "Alavanca curta de trem, retirada de uma locomotiva desativada",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    29: {
        "nome": "Facão agrícola com inscrição apagada",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    30: {
        "nome": "Martelo de açougueiro com cabeça dupla",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    31: {
        "nome": "Navalha dobrável com monograma do Professorado Nacional",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    32: {
        "nome": "Faca de trincheira feita com lima",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    33: {
        "nome": "Pistola compacta com brasão do exército imperial",
        "tipo": "Pistola e revólver",
        "dano": "1D8",
        "regra": "Rolar 1D6 para munição"
    },
    34: {
        "nome": "Caneta-tinteiro de cobre, com ponta afiada por uso indevido",
        "tipo": "Improvisada (perfurante)",
        "dano": "1D4",
        "regra": ""
    },
    35: {
        "nome": "Tesoura cirúrgica entortada",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    36: {
        "nome": "Parafuso gigante com rosca quebrada, encontrado em trilho abandonado",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    37: {
        "nome": "Punho de guarda-chuva com espeto oculto",
        "tipo": "Perfurante improvisado",
        "dano": "1D4",
        "regra": ""
    },
    38: {
        "nome": "Garfo de açougueiro de três pontas",
        "tipo": "Perfurante média",
        "dano": "1D6",
        "regra": ""
    },
    39: {
        "nome": "Porrete policial com marca da Cathédrale",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
        40: {
        "nome": "Pincel de artista com ponta enrijecida em resina seca",
        "tipo": "Improvisada (cortes leves)",
        "dano": "1D4",
        "regra": ""
    },
    41: {
        "nome": "Agulha de crochê grossa, torta na ponta",
        "tipo": "Perfurante leve",
        "dano": "1D4",
        "regra": ""
    },
    42: {
        "nome": "Copo de vidro grosso, quebrado num lado",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    43: {
        "nome": "Tampa de panela, usada como escudo e estilingue improvisado",
        "tipo": "Improvisada (defensiva)",
        "dano": "1D4",
        "regra": "Pode ser usada para aparar"
    },
    44: {
        "nome": "Tábua de passar roupa com marcas de queimadura",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    45: {
        "nome": "Candelabro de bronze com dois braços quebrados",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    46: {
        "nome": "Cinto com fivela de latão, enrolado na mão",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    47: {
        "nome": "Tesoura de poda com ferrugem nas engrenagens",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    48: {
        "nome": "Trinco de porta arrancado",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    49: {
        "nome": "Cabide de ferro dobrado",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    50: {
        "nome": "Garrafa de perfume com base reforçada",
        "tipo": "Improvisada",
        "dano": "1D4",
        "regra": ""
    },
    51: {
        "nome": "Estribo de cavalo com couro apodrecido",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    52: {
        "nome": "Quebra-nozes de ferro",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    53: {
        "nome": "Bastão de cortina com gancho na ponta",
        "tipo": "Improvisada perfurante",
        "dano": "1D4",
        "regra": ""
    },
    54: {
        "nome": "Sabre de treino infantil, pesado demais pro jogo e leve demais pra guerra",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    55: {
        "nome": "Régua de madeira longa com entalhe de professorado",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    56: {
        "nome": "Espeto de carne, ainda com marcas de carvão",
        "tipo": "Perfurante média",
        "dano": "1D6",
        "regra": ""
    },
    57: {
        "nome": "Corrimão de escada quebrado",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    58: {
        "nome": "Vela derretida com ponta dura como pedra",
        "tipo": "Improvisada leve",
        "dano": "1D4",
        "regra": ""
    },
    59: {
        "nome": "Par de sapatos com salto de madeira, um deles com prego solto",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    60: {
        "nome": "Caixa de música rachada — toca só uma nota quando acerta",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": "Efeito narrativo opcional ao toque"
    },
    61: {
        "nome": "Tábua de passar roupa com dobradiça solta",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    62: {
        "nome": "Vidro de compota estourado, com tampa presa",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    63: {
        "nome": "Gaiola de passarinho amassada, com uma das barras afiadas",
        "tipo": "Improvisada perfurante",
        "dano": "1D4",
        "regra": ""
    },
    64: {
        "nome": "Corrente de relógio com pingente de bronze cortante",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    65: {
        "nome": "Régua metálica escolar, entortada na ponta",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    66: {
        "nome": "Pistola com símbolo da Société d’Éther, ainda quente ao toque",
        "tipo": "Pistola e revólver",
        "dano": "1D8",
        "regra": "Rolar 1D6 para munição"
    },
    67: {
        "nome": "Bota de couro com salto de madeira estourado",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    68: {
        "nome": "Moldura de espelho rachada, com vidro estilhaçado preso",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    69: {
        "nome": "Espeto de ferreiro, usado para moldar brasas",
        "tipo": "Perfurante média",
        "dano": "1D6",
        "regra": ""
    },
    70: {
        "nome": "Haste de sombrinha com ponta de cobre",
        "tipo": "Improvisada perfurante",
        "dano": "1D4",
        "regra": ""
    },
    71: {
        "nome": "Corrente de bicicleta com graxa seca",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    72: {
        "nome": "Tridente de ferro pequeno, decorativo, arrancado de altar",
        "tipo": "Perfurante média",
        "dano": "1D6",
        "regra": ""
    },
    73: {
        "nome": "Gancho de açougueiro com resquícios orgânicos",
        "tipo": "Perfurante média",
        "dano": "1D6",
        "regra": ""
    },
    74: {
        "nome": "Cavilha de trilho de trem",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    75: {
        "nome": "Ponta de guarda-chuva afiada propositalmente",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    76: {
        "nome": "Candelabro de mesa partido ao meio",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    77: {
        "nome": "Tampa de bueiro em miniatura (decoração), usada como escudo e porrete",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    78: {
        "nome": "Soquete de lâmpada com cabo de pano",
        "tipo": "Improvisada com intenção",
        "dano": "1D6",
        "regra": ""
    },
    79: {
        "nome": "Pente de osso com dentes partidos",
        "tipo": "Improvisada leve",
        "dano": "1D4",
        "regra": ""
    },
        80: {
        "nome": "Foice de jardim infantil, já oxidada",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    81: {
        "nome": "Facão de mato com lâmina torta",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    82: {
        "nome": "Lança de cena teatral, usada em tragédias",
        "tipo": "Perfurante média",
        "dano": "1D6",
        "regra": ""
    },
    83: {
        "nome": "Martelo de pedreiro, com cabo curto",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    84: {
        "nome": "Tesoura de alfaiate com ponta dupla",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    85: {
        "nome": "Machado de talho, usado para cortar juntas",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    86: {
        "nome": "Ponta de flecha histórica, adaptada num cabo de colher",
        "tipo": "Perfurante leve",
        "dano": "1D4",
        "regra": ""
    },
    87: {
        "nome": "Espada de desfile, sem fio",
        "tipo": "Contundente leve",
        "dano": "1D4",
        "regra": ""
    },
    88: {
        "nome": "Pistola artesanal feita com peça de engate",
        "tipo": "Pistola improvisada",
        "dano": "1D8",
        "regra": "Rolar 1D6 para munição"
    },
    89: {
        "nome": "Mangueira metálica de irrigação, rígida de ferrugem",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    90: {
        "nome": "Lâmina de poda agrícola, com cabo serrado",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    91: {
        "nome": "Tridente de pescador com ponta reconstruída em ferro fundido",
        "tipo": "Perfurante pesada",
        "dano": "1D8",
        "regra": ""
    },
    92: {
        "nome": "Sabre de oficial com bainha rasgada",
        "tipo": "Cortes e lâminas médias",
        "dano": "1D6",
        "regra": ""
    },
    93: {
        "nome": "Cassetete com símbolo da Ordo Nocturne queimado a faca",
        "tipo": "Contundente média",
        "dano": "1D6",
        "regra": ""
    },
    94: {
        "nome": "Florete de combate real, cabo trincado",
        "tipo": "Perfurante leve",
        "dano": "1D4",
        "regra": ""
    },
    95: {
        "nome": "Faca de campo médico, usada para abrir roupas e carne",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    96: {
        "nome": "Espingarda serrada de caça, com cheiro de pólvora antiga",
        "tipo": "Espingarda curta",
        "dano": "1D10",
        "regra": "Rolar 1D6 para munição"
    },
    97: {
        "nome": "Marreta de trilho, mais arma do que ferramenta",
        "tipo": "Contundente pesada",
        "dano": "1D8",
        "regra": ""
    },
    98: {
        "nome": "Adaga de ritual da Cathédrale, sem símbolo visível",
        "tipo": "Cortes e lâminas pequenas",
        "dano": "1D4",
        "regra": ""
    },
    99: {
        "nome": "Pistola compacta com número raspado e sangue seco no gatilho",
        "tipo": "Pistola e revólver",
        "dano": "1D8",
        "regra": "Rolar 1D6 para munição"
    }
}
def sortear_objeto_d100():
    rolagem = random.randint(0, 99)
    item = objetos_abandono[rolagem]
    return rolagem, item["nome"], item["tipo"], item["dano"], item["regra"]    


# === EXECUÇÃO GERAL ===
idade_d4, idade = sorteio_idade()
fardo_id, (fardo_nome, arcano) = sorteio_fardo()
atributos = distribuir_atributos(idade_d4)
habilidades = exibir_habilidades(fardo_id)
cortina_d4, cortina = sorteio_cortina(fardo_id)
estigmas = sortear_estigmas()
fortune_roll, fortune_etat, faixa = etat_de_fortune_d10()
plaie_roll, plaie = ce_quil_reste()

# === EXIBIÇÃO FINAL ===
print(f"PASSO 1 – Âge(Idade): {idade} (D4: {idade_d4})")
print(f"PASSO 2 – Fardeau(Fardo): {fardo_nome} (Arcano: {arcano})")
print("PASSO 3 – Attributs:")
for k, data in atributos.items():
    val = data["final"]
    mod = data["mod"]
    bonus = f" (+{mod})" if mod > 0 else f" ({mod})" if mod < 0 else ""
    print(f"  {k}: {val}{bonus}")
print("PASSO 4 – Compétences:")
for nom, pct in habilidades:
    print(f"  {nom}: +{pct}%")
print(f"PASSO 5 – Alignement: {cortina} (D4: {cortina_d4})")
print("PASSO 6 – Stigmates:")
for e in estigmas:
    print(f"  [{e['Tipo']}] {e['Nome']} – Grau {e['Grau']} (Rolagem: {e['Rolagem']})")
    print(f"    → {e['Descrição']}")
print(f"PASSO 8 – État de Fortune(Estado de Fortuna): {fortune_etat} (D10: {fortune_roll}) → Sucesso: {faixa}")
print(f"PASSO 9 – Ce qu’il reste de moi(O Que Restou de Mim): {plaie} (D30: {plaie_roll})")
obj_roll, obj_nome, obj_tipo, obj_dano, obj_regra = sortear_objeto_d100()
print(f"PASSO 10 – O que a Mão Toca:")
print(f"  Objeto #{obj_roll:02d}: {obj_nome}")
print(f"    → Tipo: {obj_tipo} | Dano: {obj_dano}")
if obj_regra:
    print(f"    ⚠️ Regra Especial: {obj_regra}")

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Personagem Revelado!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
