import pygame
from personagem import Personagem


class Tela:
    
    def __init__(self, titulo=None, desenhar_extra=None):
        self.titulo = titulo
        self.desenhar_extra = desenhar_extra
        self.botoes = []

        self.largura = 800
        self.altura = 600
        self.cor_fundo = (173, 216, 230)

        self.fonte = pygame.font.SysFont("arial", 28)

        self.robo = Personagem(x=80, y=220, largura=80, altura=120)

    def adicionar_botao(self, botao):
        self.botoes.append(botao)

    def executar(self, tela, clock):
        rodando = True

        while rodando:
            clock.tick(60)
            tela.fill(self.cor_fundo)

            
            if self.desenhar_extra:
                self.desenhar_extra(tela)


            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "SAIR"

                for botao in self.botoes:
                    if botao.foi_clicado(evento):
                        return botao.texto

            self.robo.desenhar(tela)

            for botao in self.botoes:
                botao.desenhar(tela)

            pygame.display.flip()
