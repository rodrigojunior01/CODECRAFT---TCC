import pygame
from menu import menu_principal
from tela_nome import tela_nome_jogador
from banco import criar_tabela
from game_tela import game_tela
from niveis import Niveis
from tela_tutorial import tela_tutorial

niveis = Niveis()
pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CodeCraft")

clock = pygame.time.Clock()

criar_tabela()

rodando = True
while rodando:
    escolha = menu_principal(tela, clock)

    if escolha == "JOGAR":
        
        resp = tela_tutorial(tela, clock)

        if resp == "JOGAR":
            

            nome = tela_nome_jogador(tela, clock)
            

            if nome:
                jogando = True

                while jogando:
                    resultado = game_tela(tela, clock, nome, niveis)

                    if resultado == "SAIR":
                        rodando = False
                        jogando = False

                    elif resultado == "MENU":
                        jogando = False

                    elif resultado == "PROXIMO_NIVEL":
                        niveis.proximo_nivel()
                        print(f"Nível atual: {niveis.get_nivel()}")

                    

    elif escolha == "PONTUAÇÃO":
        print("Tela de pontuação")

    elif escolha == "NÍVEIS":
        print("Tela de níveis")

    elif escolha == "CONFIGURAÇÕES":
        print("Tela de configurações")

    elif escolha == "SAIR":
        rodando = False

    
   

pygame.quit()