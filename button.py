import pygame


class Button:
    def __init__(self, texto, x, y, largura, altura, fonte):
        self.texto = texto
        self.rect = pygame.Rect(x, y, largura, altura)
        self.fonte = fonte

        self.cor_normal = (180, 180, 180)
        self.cor_hover = (150, 150, 150)
        self.cor_texto = (0, 0, 0)

    def desenhar(self, tela):
        mouse = pygame.mouse.get_pos()
        cor = self.cor_hover if self.rect.collidepoint(mouse) else self.cor_normal

        pygame.draw.rect(tela, cor, self.rect, border_radius=8)

        tamanho_fonte = self.fonte.get_height()
        fonte_atual = self.fonte

        texto_render = fonte_atual.render(self.texto, True, self.cor_texto)

        while texto_render.get_width() > self.rect.width - 10:
            tamanho_fonte -= 1
            fonte_atual = pygame.font.SysFont("arial", tamanho_fonte)
            texto_render = fonte_atual.render(self.texto, True, self.cor_texto)

        texto_rect = texto_render.get_rect(center=self.rect.center)
        tela.blit(texto_render, texto_rect)

    def foi_clicado(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                return True
        return False