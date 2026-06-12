import pygame
import random


def tela_loop(tela, clock):
    fonte = pygame.font.SysFont("arial", 22)
    fonte_grande = pygame.font.SysFont("arial", 28, bold=True)

    # ✅ DESAFIOS DE LOOP (melhorados)
    desafios = [
        {
            "texto": "x começa em 0\nRepita: x = x + 1\nQuando chega em 5?\nQuantas repetições?",
            "resposta": "5"
        },
        {
            "texto": "x começa em 1\nRepita: x = x * 2\nQuando chega em 8?\nQuantas repetições?",
            "resposta": "3"
        },
        {
            "texto": "x começa em 2\nRepita: x = x + 2\nQuando chega em 10?\nQuantas repetições?",
            "resposta": "4"
        },
        {
            "texto": "x começa em 10\nRepita: x = x - 1\nQuando chega em 5?\nQuantas repetições?",
            "resposta": "5"
        }
    ]

    desafio = random.choice(desafios)

    opcoes = ["2", "3", "4", "5"]
    random.shuffle(opcoes)

    while True:
        clock.tick(60)
        tela.fill((20, 20, 40))

        # ✅ título
        titulo = fonte_grande.render("LOOP (REPETIÇÃO)", True, (255, 255, 255))
        tela.blit(titulo, titulo.get_rect(center=(400, 60)))

        # ✅ texto do desafio
        linhas = desafio["texto"].split("\n")
        for i, linha in enumerate(linhas):
            txt = fonte.render(linha, True, (255, 255, 255))
            tela.blit(txt, (100, 150 + i * 30))

        # ✅ desenho estilo loop
        pygame.draw.rect(tela, (200, 200, 0), (300, 260, 200, 80), 3)
        txt_loop = fonte.render("LOOP", True, (255, 255, 255))
        tela.blit(txt_loop, txt_loop.get_rect(center=(400, 300)))

        # ✅ botões resposta
        botoes = []

        for i, opcao in enumerate(opcoes):
            btn = pygame.Rect(250, 380 + i * 60, 120, 50)

            pygame.draw.rect(tela, (70, 70, 200), btn)

            txt = fonte.render(opcao, True, (255, 255, 255))
            tela.blit(txt, txt.get_rect(center=btn.center))

            botoes.append((btn, opcao))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                for btn, opcao in botoes:
                    if btn.collidepoint(evento.pos):
                        return opcao == desafio["resposta"]