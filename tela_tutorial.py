import pygame


def tela_tutorial(tela, clock):
    fonte = pygame.font.SysFont("arial", 20)
    fonte_titulo = pygame.font.SysFont("arial", 26, bold=True)

    pagina = 0

    paginas = [

        # ✅ PAGINA 1
        [
            "BEM-VINDO AO CODECRAFT",
            "",
            "Objetivo:",
            "Avançar pelos níveis resolvendo desafios de lógica",
            "",
            "Pressione ENTER para continuar"
        ],

        # ✅ PAGINA 2 - VARIÁVEIS
        [
            "VARIÁVEIS",
            "",
            "Uma variável guarda um valor",
            "",
            "Exemplo:",
            "x = 10",
            "",
            "Pressione ENTER"
        ],

        # ✅ PAGINA 3 - OPERADORES
        [
            "OPERADORES",
            "",
            "* (multiplicação) vem antes de +",
            "",
            "Exemplo:",
            "2 + 3 * 4 = 14",
            "",
            "Pressione ENTER"
        ],

        # ✅ PAGINA 4 - IF
        [
            "CONDICIONAIS (IF)",
            "",
            "Exemplo:",
            "x > 5",
            "",
            "Se for verdadeiro → SIM",
            "Se for falso → NÃO",
            "",
            "Usado nas PORTAS"
        ],

        # ✅ PAGINA 5 - AND / OR / XOR
        [
            "OPERADORES LÓGICOS",
            "",
            "AND → precisa de dois verdadeiros",
            "OR  → um verdadeiro basta",
            "XOR → apenas um verdadeiro",
            "",
            "Pressione ENTER"
        ],

        # ✅ PAGINA 6 - TABELA VERDADE
        [
            "TABELA VERDADE (SIMPLIFICADA)",
            "",
            "A   B   A AND B",
            "V   V   V",
            "V   F   F",
            "F   V   F",
            "F   F   F",
            "",
            "Pressione ENTER"
        ],

        # ✅ PAGINA 7 - JOGO
        [
            "MECÂNICAS DO JOGO",
            "",
            "Espinho → responda perguntas",
            "Porta → resolva condições (IF)",
            "Fogo → resolva loop",
            "Cordas → apagam o fogo",
            "",
            "Pressione ENTER"
        ],

        # ✅ PAGINA FINAL
        [
            "BOA SORTE!",
            "",
            "Use a lógica para vencer.",
            "",
            "Pressione ENTER para jogar"
        ],
    ]

    while True:
        clock.tick(60)
        tela.fill((30, 30, 50))

        conteudo = paginas[pagina]

        for i, linha in enumerate(conteudo):
            if i == 0:
                txt = fonte_titulo.render(linha, True, (255, 255, 255))
            else:
                txt = fonte.render(linha, True, (255, 255, 255))

            tela.blit(txt, (80, 100 + i * 30))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "SAIR"

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:

                    if pagina < len(paginas) - 1:
                        pagina += 1
                    else:
                        return "JOGAR"