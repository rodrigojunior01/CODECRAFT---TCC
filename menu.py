import pygame
from tela import Tela
from button import Button


def desenhar_titulo(tela):
    fonte_titulo = pygame.font.SysFont("arial", 48, bold=True)
    fonte_subtitulo = pygame.font.SysFont("arial", 24)

    titulo = fonte_titulo.render("CODECRAFT", True, (0, 0, 0))
    subtitulo = fonte_subtitulo.render("APRENDENDO A LÓGICA", True, (60, 60, 60))

    tela.blit(titulo, titulo.get_rect(center=(400, 80)))
    tela.blit(subtitulo, subtitulo.get_rect(center=(400, 120)))


def menu_principal(tela, clock):
    fonte = pygame.font.SysFont("arial", 28)

    menu = Tela(
        titulo="Menu Principal",
        desenhar_extra=desenhar_titulo
    )

    menu.adicionar_botao(Button("JOGAR", 340, 180, 220, 50, fonte))
    menu.adicionar_botao(Button("PONTUAÇÃO", 340, 250, 220, 50, fonte))
    menu.adicionar_botao(Button("NÍVEIS", 340, 320, 220, 50, fonte))
    menu.adicionar_botao(Button("CONFIGURAÇÕES", 340, 390, 220, 50, fonte))

    return menu.executar(tela, clock)