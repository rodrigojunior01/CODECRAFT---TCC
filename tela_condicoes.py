import pygame
import random


def tela_condicao(tela, clock):
    fonte = pygame.font.SysFont("arial", 22)
    fonte_grande = pygame.font.SysFont("arial", 28, bold=True)

    # ✅ BANCO DE PERGUNTAS AVANÇADO
    perguntas = [
        {
            "texto": "João é filho de José.\nAna é filha de João.\nJoão e Ana são irmãos?",
            "resposta": False,
            "condicao": "Relação familiar"
        },
        {
            "texto": "João é pai de Maria.\nMaria é mãe de Pedro.\nJoão é avô de Pedro?",
            "resposta": True,
            "condicao": "Hierarquia"
        },
        {
            "texto": "x = 10\nx > 5 AND x < 20",
            "resposta": True,
            "condicao": "AND"
        },
        {
            "texto": "x = 10\nx > 5 AND x < 8",
            "resposta": False,
            "condicao": "AND"
        },
        {
            "texto": "x = 3\nx > 5 OR x == 3",
            "resposta": True,
            "condicao": "OR"
        },
        {
            "texto": "x = 7\nx < 5 OR x == 6",
            "resposta": False,
            "condicao": "OR"
        },
        {
            "texto": "x = 5\ny = 10\n(x == 5) XOR (y == 10)",
            "resposta": False,
            "condicao": "XOR"
        },
        {
            "texto": "x = 5\ny = 9\n(x == 5) XOR (y == 10)",
            "resposta": True,
            "condicao": "XOR"
        },
        {
            "texto": "Tabela:\nA = True, B = False\nA AND B",
            "resposta": False,
            "condicao": "Tabela Verdade"
        },
        {
            "texto": "Tabela:\nA = True, B = False\nA OR B",
            "resposta": True,
            "condicao": "Tabela Verdade"
        }
    ]

    pergunta = random.choice(perguntas)

    while True:
        clock.tick(60)
        tela.fill((30, 30, 50))

        # ✅ título
        titulo = fonte_grande.render("Lógica Condicional", True, (255, 255, 255))
        tela.blit(titulo, titulo.get_rect(center=(400, 60)))

        # ✅ tipo da lógica
        tipo = fonte.render(f"Tipo: {pergunta['condicao']}", True, (200, 200, 200))
        tela.blit(tipo, tipo.get_rect(center=(400, 100)))

        # ✅ texto da pergunta (quebrado em linhas)
        linhas = pergunta["texto"].split("\n")
        for i, linha in enumerate(linhas):
            txt = fonte.render(linha, True, (255, 255, 255))
            tela.blit(txt, (100, 150 + i * 30))

        # ✅ LOSANGO
        pygame.draw.polygon(
            tela,
            (200, 200, 0),
            [(400, 260), (480, 320), (400, 380), (320, 320)],
            3
        )

        txt_if = fonte.render("VERDADEIRO?", True, (255, 255, 255))
        tela.blit(txt_if, txt_if.get_rect(center=(400, 320)))

        # ✅ BOTÕES
        btn_sim = pygame.Rect(250, 420, 120, 50)
        btn_nao = pygame.Rect(430, 420, 120, 50)

        pygame.draw.rect(tela, (0, 150, 0), btn_sim)
        pygame.draw.rect(tela, (150, 0, 0), btn_nao)

        tela.blit(fonte.render("VERDADEIRO", True, (255,255,255)), btn_sim.move(5, 15))
        tela.blit(fonte.render("FALSO", True, (255,255,255)), btn_nao.move(25, 15))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if btn_sim.collidepoint(evento.pos):
                    return pergunta["resposta"] == True

                if btn_nao.collidepoint(evento.pos):
                    return pergunta["resposta"] == False