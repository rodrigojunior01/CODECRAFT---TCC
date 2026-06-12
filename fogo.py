import pygame

class Fogo:
    def __init__(self, rect):
        self.rect = rect
        self.ativo = True

    def desenhar(self, tela, sprite):
        if self.ativo:
            tela.blit(sprite, self.rect)

        elif hasattr(self, "apagando") and self.timer > 0:
            # desenha "água" azul
            pygame.draw.rect(tela, (0, 150, 255), self.rect)
            self.timer -= 1

    def queimar(self, robo):
        return self.ativo and robo.rect.colliderect(self.rect)

    def apagar(self):
        self.ativo = False
        self.apagando = True
        self.timer = 20