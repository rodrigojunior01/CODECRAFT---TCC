import pygame
import random

class Porta:
    def __init__(self, rect):
        self.rect = rect
        self.aberta = False

    def desenhar(self, tela, sprite):
        if not self.aberta:
            tela.blit(sprite, self.rect)

    def abrir(self):
        self.aberta = True


def criar_portas(corredores, pos_inicial):
    quantidade = random.randint(3, 5)

    livres = [
        c for c in corredores
        if not c.collidepoint(pos_inicial)
        and abs(c.x - pos_inicial[0]) > 120
        and abs(c.y - pos_inicial[1]) > 120
    ]

    escolhidos = random.sample(livres, min(quantidade, len(livres)))

    portas = [Porta(rect) for rect in escolhidos]

    return portas