import pygame


class Personagem:
    def __init__(self, x, y, largura, altura, velocidade=4):
        # Posição
        self.x = x
        self.y = y

        # Tamanho
        self.largura = largura
        self.altura = altura

        # Movimento
        self.velocidade = velocidade

        # ✅ Sprite inicial: robô de frente
        self.imagem = pygame.image.load(
            "assets/robo_frente.png"
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem, (self.largura, self.altura)
        )

        # Hitbox menor que o sprite para evitar travamento nas bordas
        margem = 6
        self.rect = pygame.Rect(
            self.x + margem,
            self.y + margem,
            self.largura - margem * 2,
            self.altura - margem * 2
        )

    def mover(self, direcao):
        if direcao == "cima":
            self.y -= self.velocidade
        elif direcao == "baixo":
            self.y += self.velocidade
        elif direcao == "esquerda":
            self.x -= self.velocidade
        elif direcao == "direita":
            self.x += self.velocidade

        # Atualiza hitbox com margem
        margem = 6
        self.rect.topleft = (self.x + margem, self.y + margem)

    def atualizar(self):
        pass  # reservado para animação/lógica futura

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))