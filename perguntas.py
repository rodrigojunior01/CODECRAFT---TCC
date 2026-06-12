import random


def gerar_perguntas_aritmetica():
    """Gera lista de perguntas de aritmética no estilo código Python"""
    perguntas = []

    # Soma
    for _ in range(6):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        resposta = a + b
        perguntas.append({
            "codigo": f"x = {a} + {b}\nprint(x)",
            "pergunta": "O que será impresso?",
            "resposta": resposta,
            "opcoes": _gerar_opcoes(resposta)
        })

    # Subtração
    for _ in range(6):
        a = random.randint(10, 30)
        b = random.randint(1, a)
        resposta = a - b
        perguntas.append({
            "codigo": f"x = {a} - {b}\nprint(x)",
            "pergunta": "O que será impresso?",
            "resposta": resposta,
            "opcoes": _gerar_opcoes(resposta)
        })

    # Multiplicação
    for _ in range(6):
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        resposta = a * b
        perguntas.append({
            "codigo": f"x = {a} * {b}\nprint(x)",
            "pergunta": "O que será impresso?",
            "resposta": resposta,
            "opcoes": _gerar_opcoes(resposta)
        })

    # Divisão inteira
    for _ in range(6):
        b = random.randint(2, 8)
        a = b * random.randint(2, 8)
        resposta = a // b
        perguntas.append({
            "codigo": f"x = {a} // {b}\nprint(x)",
            "pergunta": "O que será impresso?",
            "resposta": resposta,
            "opcoes": _gerar_opcoes(resposta)
        })

    # Expressão composta
    for _ in range(6):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 5)
        resposta = a + b * c
        perguntas.append({
            "codigo": f"x = {a} + {b} * {c}\nprint(x)",
            "pergunta": "O que será impresso?",
            "resposta": resposta,
            "opcoes": _gerar_opcoes(resposta)
        })

    # Variável reatribuída
    for _ in range(6):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        resposta = a + b
        perguntas.append({
            "codigo": f"x = {a}\nx = x + {b}\nprint(x)",
            "pergunta": "O que será impresso?",
            "resposta": resposta,
            "opcoes": _gerar_opcoes(resposta)
        })

    random.shuffle(perguntas)
    return perguntas


def _gerar_opcoes(resposta):
    """Gera 4 opções sendo 1 correta e 3 distratores plausíveis"""
    opcoes = {resposta}
    tentativas = 0
    while len(opcoes) < 4 and tentativas < 50:
        delta = random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
        distrator = resposta + delta
        if distrator >= 0:
            opcoes.add(distrator)
        tentativas += 1

    # Garante 4 opções mesmo em casos extremos
    i = 1
    while len(opcoes) < 4:
        opcoes.add(resposta + i)
        i += 1

    lista = list(opcoes)
    random.shuffle(lista)
    return lista
