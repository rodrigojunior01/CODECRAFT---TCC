import pygame
from personagem import Personagem
from labirinto import Labirinto
from colisao import verificar_colisao
from espinho import criar_espinhos
from tela_pergunta import tela_pergunta
from perguntas import gerar_perguntas_aritmetica
from niveis import Niveis
from portas import criar_portas
from tela_condicoes import tela_condicao
from fogo import Fogo
from corda import Corda




def game_tela(tela, clock, nome_jogador, niveis):
    fonte = pygame.font.SysFont("arial", 22)

    pontuacao = 0
    vidas = 3

    labirinto = Labirinto(800, 600)
    
    ix, iy = labirinto.posicao_inicial()
    robo = Personagem(ix, iy, 32, 44)

    
    saida_liberada = False
    saida_liberada_nivel2 = False
    saida = pygame.Rect(740, 56, 60, 500)  

    if niveis.get_nivel() == 1:
        espinhos = criar_espinhos(labirinto.corredores, (ix, iy))
        portas = []
        fogos = []
        cordas = []

    elif niveis.get_nivel() == 2:
        espinhos = []
        portas = criar_portas(labirinto.corredores, (ix, iy))
        fogos = []
        cordas = []

    elif niveis.get_nivel() == 3:
        espinhos = []
        portas = []
        
        fogos = []

        for c in labirinto.corredores:
            if abs(c.x - ix) > 120 and abs(c.y - iy) > 120:
                fogos.append(Fogo(c))

        fogos = fogos[:3]  # quantidade de fogos
        cordas = []

        cordas = []

        for fogo in fogos:
            cima = fogo.rect.move(0, -40)
            baixo = fogo.rect.move(0, 40)

            for pos in [cima, baixo]:
                if pos in labirinto.corredores:
                    cordas.append(Corda(pos, fogo))

    else:
        espinhos = []
        portas = []
        fogos = []
        cordas = []

        import random

        # ✅ aleatoriedade
        usar_espinhos = random.choice([True, False])
        usar_portas = random.choice([True, False])
        usar_fogos = random.choice([True, False])

        # garantir que pelo menos 1 existe
        if not (usar_espinhos or usar_portas or usar_fogos):
            usar_espinhos = True

        # ✅ ESPINHOS
        if usar_espinhos:
            espinhos = criar_espinhos(labirinto.corredores, (ix, iy))

        # ✅ PORTAS
        if usar_portas:
            portas = criar_portas(labirinto.corredores, (ix, iy))

        # ✅ FOGOS
        if usar_fogos:
            # mesmo filtro pra não nascer no player
            posicoes_validas = [
                c for c in labirinto.corredores
                if abs(c.x - ix) > 120 and abs(c.y - iy) > 120
            ]

            fogos = [Fogo(c) for c in posicoes_validas[:3]]

            cordas = []
            for fogo in fogos:
                cima = fogo.rect.move(0, -40)
                baixo = fogo.rect.move(0, 40)

                cordas.append(Corda(cima, fogo))
                cordas.append(Corda(baixo, fogo))
    banco_perguntas = gerar_perguntas_aritmetica()
    idx_pergunta = 0

    coracao = pygame.image.load("assets/coracao.png").convert_alpha()
    coracao = pygame.transform.scale(coracao, (24, 24))
    sprite_porta = pygame.image.load("assets/porta.png").convert_alpha()
    sprite_porta = pygame.transform.scale(sprite_porta, (40, 40))

    sprite_fogo = pygame.image.load("assets/fogo.png").convert_alpha()
    sprite_fogo = pygame.transform.scale(sprite_fogo, (40, 40))

    


    
    esperando_resposta = False
    dano_timer = 0

    while True:
        clock.tick(60)
        tela.fill((200, 220, 240))
        dano_timer += 1
        
        obstaculos = list(labirinto.paredes)

        # adiciona portas fechadas
        for porta in portas:
            if not porta.aberta:
                obstaculos.append(porta.rect)

        for fogo in fogos:
            if fogo.queimar(robo):
                if dano_timer > 30:   # ✅ controla dano
                    vidas -= 1
                    dano_timer = 0

 
        # Movimento com colisão
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            verificar_colisao(robo, obstaculos, "cima", robo.velocidade)
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            verificar_colisao(robo, obstaculos, "baixo", robo.velocidade)
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            verificar_colisao(robo, obstaculos, "esquerda", robo.velocidade)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            verificar_colisao(robo, obstaculos, "direita", robo.velocidade)

            
        

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "SAIR"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "MENU"
                
                if evento.key == pygame.K_y:

                    # ✅ NIVEL 1 - espinhos
                    for e in espinhos:
                        e.desativar()

                    # ✅ NIVEL 2 - portas
                    for porta in portas:
                        porta.abrir()

                    # ✅ NIVEL 3 - fogo
                    for fogo in fogos:
                        fogo.apagar()

                    # ✅ libera saída nível 2
                    if niveis.get_nivel() == 2:
                        saida_liberada_nivel2 = True

                        saida_area = pygame.Rect(720, 56, 80, 500)

                        labirinto.paredes = [
                            p for p in labirinto.paredes
                            if not p.colliderect(saida_area)
                        ]

                    # ✅ libera saída nível 3
                    if niveis.get_nivel() >= 3:
                        saida_liberada = True

                        saida_area = pygame.Rect(720, 56, 80, 500)

                        labirinto.paredes = [
                            p for p in labirinto.paredes
                            if not p.colliderect(saida_area)
                        ]


        # ✅ INTERAÇÃO COM PORTA (NOVO SISTEMA)
        
        teclas = pygame.key.get_pressed()

        for porta in portas:
            if not porta.aberta:

                zona_interacao = porta.rect.inflate(10, 10)

                if robo.rect.colliderect(zona_interacao) and not esperando_resposta:

                    esperando_resposta = True

                    acertou = tela_condicao(tela, clock)

                    if acertou:
                        porta.abrir()
                        pontuacao += 20   # ✅ GANHA PONTO

                    else:
                        vidas -= 1        # ✅ PERDE VIDA

                        if vidas <= 0:    # ✅ MORTE
                            return "MENU"

                    esperando_resposta = False

        from tela_loop import tela_loop

        for corda in cordas:
            zona = corda.rect.inflate(10, 10)

            if robo.rect.colliderect(zona) and not esperando_resposta:

                if teclas[pygame.K_e] or teclas[pygame.K_RETURN]:

                    esperando_resposta = True

                    acertou = tela_loop(tela, clock)

                    if acertou:
                        corda.fogo.apagar()
                        pontuacao += 30
                    else:
                        vidas -= 1

                        if vidas <= 0:
                            return "MENU"

                    esperando_resposta = False

        # Desenha labirinto e personagem
        labirinto.desenhar(tela)
        
        

        for porta in portas:
            porta.desenhar(tela, sprite_porta)

        for fogo in fogos:
            fogo.desenhar(tela, sprite_fogo)

        for corda in cordas:
            # base da corda
            pygame.draw.rect(tela, (139, 69, 19), corda.rect)  # marrom

            # linha em cima (corda mesmo)
            pygame.draw.line(
                tela,
                (255, 255, 0),
                (corda.rect.centerx, corda.rect.top),
                (corda.rect.centerx, corda.rect.bottom),
                3
            )

        #    dica na porta
        for porta in portas:
            zona_interacao = porta.rect.inflate(10, 10)

            if not porta.aberta and robo.rect.colliderect(zona_interacao):
                fonte_dica = pygame.font.SysFont("arial", 18)
                dica = fonte_dica.render("Pressione E ou ENTER para abrir", True, (255, 255, 100))
                tela.blit(dica, dica.get_rect(center=(400, 560)))

        for corda in cordas:
            zona = corda.rect.inflate(10, 10)

            if robo.rect.colliderect(zona):
                fonte_dica = pygame.font.SysFont("arial", 18)
                dica = fonte_dica.render("E para apagar fogo", True, (255, 255, 100))
                tela.blit(dica, dica.get_rect(center=(400, 560)))
       
                    
        
        

        # Espinhos
        for e in espinhos:
            e.atualizar()

            # Verifica se personagem está no botão
            em_cima_botao = e.verificar_botao(robo.rect)
            e.mostrar_botao = em_cima_botao

            e.desenhar(tela)

            # Personagem tocou o botão → abre pergunta
            if em_cima_botao:
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_e] or teclas[pygame.K_RETURN]:
                    pergunta = banco_perguntas[idx_pergunta % len(banco_perguntas)]
                    acertou = tela_pergunta(tela, clock, pergunta)
                    if acertou:
                        e.desativar()
                        pontuacao += 10
                        idx_pergunta += 1
                    else:
                        # Erra: próxima pergunta diferente na próxima tentativa
                        idx_pergunta += 1

            # Colisão com espinho ativo
            if e.esta_ativo() and robo.rect.colliderect(e.rect):
                vidas -= 1
                robo.x, robo.y = ix, iy
                robo.rect.topleft = (robo.x + 6, robo.y + 6)
                if vidas <= 0:
                    return "MENU"

        
        # ✅ NIVEL 1 (espinhos)
        if niveis.get_nivel() == 1:
            if all(not e.ativo for e in espinhos) and not saida_liberada:
                saida_liberada = True

                saida_area = pygame.Rect(720, 56, 80, 500)

                labirinto.paredes = [
                    p for p in labirinto.paredes
                    if not p.colliderect(saida_area)
                ]


        
        # ✅ NIVEL 2 (portas)
        if niveis.get_nivel() == 2:
            if len(portas) > 0 and all(p.aberta for p in portas) and not saida_liberada_nivel2:

                saida_liberada_nivel2 = True

                saida_area = pygame.Rect(720, 56, 80, 500)

                labirinto.paredes = [
                    p for p in labirinto.paredes
                    if not p.colliderect(saida_area)
                ]

        #  NIVEL 3 (fogo)
        if niveis.get_nivel() == 3:
            if len(fogos) > 0 and all(not f.ativo for f in fogos):

                saida_liberada = True

                saida_area = pygame.Rect(720, 56, 80, 500)

                labirinto.paredes = [
                    p for p in labirinto.paredes
                    if not p.colliderect(saida_area)
                ]

        robo.desenhar(tela)

        # Dica do botão
        for e in espinhos:
            if e.ativo and e.verificar_botao(robo.rect):
                fonte_dica = pygame.font.SysFont("arial", 18)
                dica_btn = fonte_dica.render("Pressione E ou Enter para responder", True, (255, 255, 100))
                tela.blit(dica_btn, dica_btn.get_rect(center=(400, 560)))

        # HUD — faixa escura no topo
        pygame.draw.rect(tela, (0, 0, 0, 180), pygame.Rect(0, 0, 800, 56))

        # Nome do jogador
        texto_nome = fonte.render(f"Jogador: {nome_jogador}", True, (255, 255, 255))
        tela.blit(texto_nome, (10, 8))

        # Pontuação
        texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
        tela.blit(texto_pontos, (300, 8))

        
        # NÍVEL
        texto_nivel = fonte.render(f"Nível: {niveis.get_nivel()}", True, (255, 255, 255))
        tela.blit(texto_nivel, (550, 8))


        # Corações alinhados à direita
        for i in range(vidas):
            tela.blit(coracao, (800 - (vidas - i) * 30, 14))

        
        if saida_liberada or saida_liberada_nivel2:
            pygame.draw.rect(tela, (0, 200, 0), saida)


        # Dica ESC
        dica = fonte.render("ESC: Menu", True, (180, 180, 180))
        tela.blit(dica, (680, 36))

        
        # ✅ NIVEL 1 → usa saída
        if niveis.get_nivel() == 1:
            if saida_liberada and robo.rect.colliderect(saida):
                return "PROXIMO_NIVEL"

        # ✅ NIVEL 2 → portas
        elif niveis.get_nivel() == 2:
            if saida_liberada_nivel2 and robo.rect.colliderect(saida):
                return "PROXIMO_NIVEL"
            
        
        # ✅ NIVEL 3+ → fogo / modo aleatório
        elif niveis.get_nivel() >= 3:
            if saida_liberada and robo.rect.colliderect(saida):
                return "PROXIMO_NIVEL"

        
        

        pygame.display.flip()