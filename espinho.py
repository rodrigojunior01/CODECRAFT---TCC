import pygame
import random

TAMANHO_BLOCO = 40


class Espinho:
    def __init__(self, x, y):
        self.x = x
        self.base_y = y + TAMANHO_BLOCO
        self.largura = 30
        self.altura_max = 20

        # Animação
        self.altura_atual = 0
        self.velocidade_anim = 0.5
        self.subindo = True

        # Estado
        self.ativo = True
        self.mostrar_botao = False

        # Zona de proximidade: 60px ao redor do espinho
        self.zona_rect = pygame.Rect(x - 20, y - 20, TAMANHO_BLOCO + 40, TAMANHO_BLOCO + 40)

        # Hitbox espinho
        self.rect = pygame.Rect(self.x + 5, self.base_y, self.largura, 0)

    def atualizar(self):
        if not self.ativo:
            return

        if self.subindo:
            self.altura_atual += self.velocidade_anim
            if self.altura_atual >= self.altura_max:
                self.altura_atual = self.altura_max
                self.subindo = False
        else:
            self.altura_atual -= self.velocidade_anim
            if self.altura_atual <= 0:
                self.altura_atual = 0
                self.subindo = True

        topo = self.base_y - int(self.altura_atual)
        self.rect = pygame.Rect(
            self.x + 5, topo,
            self.largura, int(self.altura_atual)
        )

    def desenhar(self, tela):
        if not self.ativo:
            return

        # Espinhos
        if self.altura_atual >= 1:
            h = int(self.altura_atual)
            topo = self.base_y - h
            num = 3
            largura_pico = self.largura // num
            cor = (80, 80, 80)
            cor_ponta = (200, 200, 200)
            for i in range(num):
                bx = self.x + 5 + i * largura_pico
                p1 = (bx, self.base_y)
                p2 = (bx + largura_pico, self.base_y)
                p3 = (bx + largura_pico // 2, topo)
                pygame.draw.polygon(tela, cor, [p1, p2, p3])
                pygame.draw.polygon(tela, cor_ponta, [
                    p3,
                    (bx + largura_pico // 2 - 2, topo + 4),
                    (bx + largura_pico // 2 + 2, topo + 4)
                ])

        # Indicador "!" flutuante acima do espinho quando jogador está perto
        if self.mostrar_botao:
            fonte = pygame.font.SysFont("arial", 20, bold=True)
            indicador = pygame.Surface((26, 26), pygame.SRCALPHA)
            pygame.draw.rect(indicador, (255, 200, 0, 220), (0, 0, 26, 26), border_radius=4)
            txt = fonte.render("!", True, (0, 0, 0))
            indicador.blit(txt, txt.get_rect(center=(13, 13)))
            tela.blit(indicador, (self.x + 8, self.base_y - self.altura_max - 32))

    def verificar_botao(self, personagem_rect):
        """Retorna True se o personagem está na zona de proximidade do espinho"""
        return self.ativo and personagem_rect.colliderect(self.zona_rect)

    def esta_ativo(self):
        return self.ativo and self.altura_atual > 2

    def desativar(self):
        self.ativo = False
        self.altura_atual = 0


def criar_espinhos(corredores, posicao_inicial, quantidade=None):
    ix, iy = posicao_inicial
    celula_inicial = pygame.Rect(
        (ix // TAMANHO_BLOCO) * TAMANHO_BLOCO,
        (iy // TAMANHO_BLOCO) * TAMANHO_BLOCO,
        TAMANHO_BLOCO, TAMANHO_BLOCO
    )

    candidatos = [
        c for c in corredores
        if abs(c.x - celula_inicial.x) > TAMANHO_BLOCO * 2
        or abs(c.y - celula_inicial.y) > TAMANHO_BLOCO * 2
    ]

    if quantidade is None:
        quantidade = random.randint(5, 12)

    escolhidos = random.sample(candidatos, min(quantidade, len(candidatos)))

    espinhos = []
    for cel in escolhidos:
        e = Espinho(cel.x + 5, cel.y)
        e.altura_atual = random.uniform(0, e.altura_max)
        e.subindo = random.choice([True, False])
        espinhos.append(e)

    return espinhos