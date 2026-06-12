import pygame
from button import Button
from banco import inserir_jogador

def tela_nome_jogador(tela, clock):
    fonte = pygame.font.SysFont("arial", 32)
    texto_nome = ""
    cursor_visivel = True
    tempo_cursor = 0

    botao_jogar = Button("JOGAR", 300, 350, 200, 50, fonte)

    while True:
        clock.tick(60)
        tela.fill((173, 216, 230))

        # Título
        titulo = fonte.render("Digite seu nome:", True, (0, 0, 0))
        tela.blit(titulo, (300, 200))

        # Caixa de texto
        caixa = pygame.Rect(250, 260, 300, 50)
        pygame.draw.rect(tela, (255, 255, 255), caixa, border_radius=6)
        pygame.draw.rect(tela, (0, 0, 0), caixa, 2, border_radius=6)

        # Texto digitado
        texto_render = fonte.render(texto_nome, True, (0, 0, 0))
        tela.blit(texto_render, (caixa.x + 10, caixa.y + 10))

        # Cursor piscando
        tempo_cursor += 1
        if tempo_cursor % 30 == 0:
            cursor_visivel = not cursor_visivel

        if cursor_visivel:
            cursor_x = caixa.x + 10 + texto_render.get_width() + 2
            pygame.draw.line(
                tela, (0, 0, 0),
                (cursor_x, caixa.y + 10),
                (cursor_x, caixa.y + 40), 2
            )

        # Botão Jogar
        botao_jogar.desenhar(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and texto_nome.strip():
                    inserir_jogador(texto_nome)
                    return texto_nome

                if evento.key == pygame.K_BACKSPACE:
                    texto_nome = texto_nome[:-1]
                elif len(texto_nome) < 15:
                    texto_nome += evento.unicode

            if botao_jogar.foi_clicado(evento) and texto_nome.strip():
                inserir_jogador(texto_nome)
                return texto_nome

        pygame.display.flip()