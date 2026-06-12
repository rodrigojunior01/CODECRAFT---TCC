import pygame
import random

TAMANHO_BLOCO = 40
OFFSET_Y = 56  # altura da barra HUD


class Labirinto:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho = TAMANHO_BLOCO

        area_jogo = altura_tela - OFFSET_Y
        # Grade em células (cada célula = 2 blocos: parede + corredor)
        self.cols = (largura_tela // TAMANHO_BLOCO - 1) // 2
        self.rows = (area_jogo // TAMANHO_BLOCO - 1) // 2

        self.paredes = []
        self.gerar_labirinto()

    def gerar_labirinto(self):
        cols = self.cols
        rows = self.rows
        t = self.tamanho

        # Grade: True = parede, False = corredor
        grid = [[True] * (cols * 2 + 1) for _ in range(rows * 2 + 1)]

        visitado = [[False] * cols for _ in range(rows)]

        def vizinhos(r, c):
            viz = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visitado[nr][nc]:
                    viz.append((nr, nc, dr, dc))
            return viz

        # DFS iterativo — célula (0,0) é sempre o ponto de partida (grid[1][1])
        stack = [(0, 0)]
        visitado[0][0] = True
        grid[1][1] = False
        # Posição pixel da célula inicial (col=1, row=1 na grade)
        self._inicio_x = 1 * t
        self._inicio_y = 1 * t + OFFSET_Y

        while stack:
            r, c = stack[-1]
            viz = vizinhos(r, c)
            if viz:
                nr, nc, dr, dc = random.choice(viz)
                visitado[nr][nc] = True
                # Abre célula destino
                grid[nr * 2 + 1][nc * 2 + 1] = False
                # Abre parede entre as duas células
                grid[r * 2 + 1 + dr][c * 2 + 1 + dc] = False
                stack.append((nr, nc))
            else:
                stack.pop()

        # Converte grade para rects pygame (com offset do HUD)
        self.paredes = []
        self.corredores = []  # células livres para posicionar espinhos
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    self.paredes.append(
                        pygame.Rect(col * t, row * t + OFFSET_Y, t, t)
                    )
                else:
                    self.corredores.append(
                        pygame.Rect(col * t, row * t + OFFSET_Y, t, t)
                    )

    def desenhar(self, tela):
        for parede in self.paredes:
            pygame.draw.rect(tela, (40, 40, 40), parede)

    def posicao_inicial(self):
        """Retorna a posição garantidamente livre onde o jogador começa"""
        t = self.tamanho
        # Centraliza o personagem dentro da célula (32x44 px)
        return (self._inicio_x + (t - 32) // 2, self._inicio_y + (t - 44) // 2)