import pygame


def verificar_colisao(personagem, paredes, direcao, velocidade):
    """
    Tenta mover o personagem na direção dada.
    Se colidir com alguma parede, desfaz o movimento.
    """
    # Move o personagem
    if direcao == "cima":
        personagem.y -= velocidade
    elif direcao == "baixo":
        personagem.y += velocidade
    elif direcao == "esquerda":
        personagem.x -= velocidade
    elif direcao == "direita":
        personagem.x += velocidade

    # Atualiza hitbox com margem
    margem = 6
    personagem.rect.topleft = (personagem.x + margem, personagem.y + margem)

    # Checa colisão com cada parede
    for parede in paredes:
        if personagem.rect.colliderect(parede):
            # Desfaz o movimento
            if direcao == "cima":
                personagem.y += velocidade
            elif direcao == "baixo":
                personagem.y -= velocidade
            elif direcao == "esquerda":
                personagem.x += velocidade
            elif direcao == "direita":
                personagem.x -= velocidade

            # Atualiza hitbox de volta com margem
            personagem.rect.topleft = (personagem.x + margem, personagem.y + margem)
            break