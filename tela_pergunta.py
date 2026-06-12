import pygame


COR_FUNDO      = (20, 20, 40)
COR_PAINEL     = (35, 35, 60)
COR_BORDA      = (80, 80, 140)
COR_CODIGO     = (30, 30, 30)
COR_TEXTO_COD  = (180, 255, 180)   # verde terminal
COR_TEXTO      = (240, 240, 240)
COR_BOTAO      = (60, 60, 100)
COR_HOVER      = (90, 90, 150)
COR_CERTO      = (40, 160, 80)
COR_ERRADO     = (180, 40, 40)


def tela_pergunta(tela, clock, pergunta):
    """
    Exibe uma pergunta de lógica com 4 opções.
    Retorna True se acertou, False se errou.
    """
    fonte_titulo = pygame.font.SysFont("arial", 22, bold=True)
    fonte_codigo = pygame.font.SysFont("couriernew", 20)
    fonte_opcao  = pygame.font.SysFont("arial", 20)
    fonte_feed   = pygame.font.SysFont("arial", 26, bold=True)

    largura, altura = tela.get_size()

    # Painel central
    painel_w, painel_h = 620, 420
    painel_x = (largura - painel_w) // 2
    painel_y = (altura - painel_h) // 2

    opcoes = pergunta["opcoes"]
    resposta_correta = pergunta["resposta"]
    linhas_codigo = pergunta["codigo"].split("\n")

    # Botões das opções
    btn_w, btn_h = 240, 48
    gap = 16
    btn_inicio_y = painel_y + 230

    botoes = []
    for i, op in enumerate(opcoes):
        col = i % 2
        lin = i // 2
        bx = painel_x + 30 + col * (btn_w + gap)
        by = btn_inicio_y + lin * (btn_h + gap)
        botoes.append(pygame.Rect(bx, by, btn_w, btn_h))

    feedback = None       # None | "certo" | "errado"
    tempo_feedback = 0

    rodando = True
    acertou = False

    while rodando:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()

        # Fundo escurecido
        overlay = pygame.Surface((largura, altura), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        tela.blit(overlay, (0, 0))

        # Painel
        pygame.draw.rect(tela, COR_PAINEL, (painel_x, painel_y, painel_w, painel_h), border_radius=12)
        pygame.draw.rect(tela, COR_BORDA,  (painel_x, painel_y, painel_w, painel_h), 2, border_radius=12)

        # Título
        titulo = fonte_titulo.render("⚙  Resolva o código para liberar a passagem!", True, COR_TEXTO)
        tela.blit(titulo, (painel_x + 20, painel_y + 16))

        # Bloco de código
        cod_x = painel_x + 20
        cod_y = painel_y + 55
        cod_w = painel_w - 40
        cod_h = 20 + len(linhas_codigo) * 28
        pygame.draw.rect(tela, COR_CODIGO, (cod_x, cod_y, cod_w, cod_h), border_radius=6)
        pygame.draw.rect(tela, COR_BORDA,  (cod_x, cod_y, cod_w, cod_h), 1, border_radius=6)

        for j, linha in enumerate(linhas_codigo):
            txt = fonte_codigo.render(linha, True, COR_TEXTO_COD)
            tela.blit(txt, (cod_x + 14, cod_y + 10 + j * 28))

        # Pergunta
        perg = fonte_opcao.render(pergunta["pergunta"], True, COR_TEXTO)
        tela.blit(perg, (painel_x + 20, btn_inicio_y - 36))

        # Botões de opção
        for i, (op, rect) in enumerate(zip(opcoes, botoes)):
            hover = rect.collidepoint(mouse) and feedback is None
            cor = COR_HOVER if hover else COR_BOTAO

            if feedback == "certo" and op == resposta_correta:
                cor = COR_CERTO
            elif feedback == "errado" and op == resposta_correta:
                cor = COR_CERTO   # mostra a certa em verde

            pygame.draw.rect(tela, cor, rect, border_radius=8)
            pygame.draw.rect(tela, COR_BORDA, rect, 1, border_radius=8)

            label = fonte_opcao.render(str(op), True, COR_TEXTO)
            tela.blit(label, label.get_rect(center=rect.center))

        # Feedback
        if feedback:
            tempo_feedback += 1
            msg = "✔  Correto! Passagem liberada!" if feedback == "certo" else "✘  Errado! Tente novamente..."
            cor_feed = COR_CERTO if feedback == "certo" else COR_ERRADO
            feed_txt = fonte_feed.render(msg, True, cor_feed)
            tela.blit(feed_txt, feed_txt.get_rect(center=(largura // 2, painel_y + painel_h - 30)))

            if tempo_feedback > 80:   # ~1.3s
                rodando = False

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.MOUSEBUTTONDOWN and feedback is None:
                for i, (op, rect) in enumerate(zip(opcoes, botoes)):
                    if rect.collidepoint(evento.pos):
                        if op == resposta_correta:
                            feedback = "certo"
                            acertou = True
                        else:
                            feedback = "errado"
                            acertou = False

    return acertou