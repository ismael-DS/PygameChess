import pygame

pygame.init()
# Tabela de cores
preto = (0, 0, 0)
marrom = (150, 75, 0)
bege = (245, 245, 220)
azul = (0, 225, 255)

tamanho = 70  # tamanho de cada quadrado
linhas_colunas = 8

tela = pygame.display.set_mode(((linhas_colunas + 2) * tamanho, (linhas_colunas + 2) * tamanho))
nome = pygame.display.set_caption('Xadrez')

# adicionando sprites:
bispo_branco = pygame.transform.scale(pygame.image.load("assets/sprites/bispo_v2.png"), (tamanho - 2, tamanho - 2))
torre_branco = pygame.transform.scale(pygame.image.load("assets/sprites/torre_v2.png"), (tamanho - 2, tamanho - 2))
cavalo_branco = pygame.transform.scale(pygame.image.load("assets/sprites/cavalo_v2.png"), (tamanho - 2, tamanho - 2))
rainha_branco = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v2.png"), (tamanho - 2, tamanho - 2))
rei_branco = pygame.transform.scale(pygame.image.load("assets/sprites/rei_v2.png"), (tamanho - 2, tamanho - 2))
peao_branco = pygame.transform.scale(pygame.image.load("assets/sprites/peao_v2.png"), (tamanho - 2, tamanho - 2))
bispo_preto = pygame.transform.scale(pygame.image.load("assets/sprites/bispo_v1.png"), (tamanho - 2, tamanho - 2))
torre_preto = pygame.transform.scale(pygame.image.load("assets/sprites/torre_v1.png"), (tamanho - 2, tamanho - 2))
cavalo_preto = pygame.transform.scale(pygame.image.load("assets/sprites/cavalo_v1.png"), (tamanho - 2, tamanho - 2))
rainha_preto = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v1.png"), (tamanho - 2, tamanho - 2))
rei_preto = pygame.transform.scale(pygame.image.load("assets/sprites/rei_v1.png"), (tamanho - 2, tamanho - 2))
peao_preto = pygame.transform.scale(pygame.image.load("assets/sprites/peao_v1.png"), (tamanho - 2, tamanho - 2))


# Funcoes

def Start():
    tela.fill(preto)

    count = 0
    for i in range(1, linhas_colunas + 1):
        for j in range(1, linhas_colunas + 1):
            if count % 2 == 0:
                pygame.draw.rect(tela, bege, [tamanho * j, tamanho * i, tamanho, tamanho])
            else:
                pygame.draw.rect(tela, marrom, [tamanho * j, tamanho * i, tamanho, tamanho])
            count += 1
        count -= 1

    # pecas brancas:
    tela.blit(torre_branco, (tamanho * 1 + 1, tamanho * 8 + 1))
    tela.blit(torre_branco, (tamanho * 8 + 1, tamanho * 8 + 1))
    tela.blit(cavalo_branco, (tamanho * 2 + 1, tamanho * 8 + 1))
    tela.blit(cavalo_branco, (tamanho * 7 + 1, tamanho * 8 + 1))
    tela.blit(bispo_branco, (tamanho * 3 + 1, tamanho * 8 + 1))
    tela.blit(bispo_branco, (tamanho * 6 + 1, tamanho * 8 + 1))
    tela.blit(rainha_branco, (tamanho * 4 + 1, tamanho * 8 + 1))
    tela.blit(rei_branco, (tamanho * 5 + 1, tamanho * 8 + 1))

    for i in range(1, 9):
        tela.blit(peao_branco, (tamanho * i + 1, tamanho * 7 + 1))

    # pecas pretas:
    tela.blit(torre_preto, (tamanho * 1 + 1, tamanho * 1 + 1))
    tela.blit(torre_preto, (tamanho * 8 + 1, tamanho * 1 + 1))
    tela.blit(cavalo_preto, (tamanho * 2 + 1, tamanho * 1 + 1))
    tela.blit(cavalo_preto, (tamanho * 7 + 1, tamanho * 1 + 1))
    tela.blit(bispo_preto, (tamanho * 3 + 1, tamanho * 1 + 1))
    tela.blit(bispo_preto, (tamanho * 6 + 1, tamanho * 1 + 1))
    tela.blit(rainha_preto, (tamanho * 4 + 1, tamanho * 1 + 1))
    tela.blit(rei_preto, (tamanho * 5 + 1, tamanho * 1 + 1))
    for i in range(1, 9):
        tela.blit(peao_preto, (tamanho * i + 1, tamanho * 2 + 1))

    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('RECOMEÇAR', False, azul), (250, 15))

    pygame.display.update()

    # Guardando posições iniciais das peças no sistema
    posicoes_iniciais = {'\nPtorre_preto1': (1, 1), '\nPtorre_preto2': (1, 8), '\nPcavalo_preto1': (1, 2),
                         '\nPcavalo_preto2': (1, 7), '\nPbispo_preto1': (1, 3), '\nPbispo_preto2': (1, 6),
                         '\nPrainha_preto': (1, 4), '\nPrei_preto': (1, 5), '\nPpeao_preto1': (2, 1),
                         '\nPpeao_preto2': (2, 2), '\nPpeao_preto3': (2, 3), '\nPpeao_preto4': (2, 4),
                         '\nPpeao_preto5': (2, 5), '\nPpeao_preto6': (2, 6), '\nPpeao_preto7': (2, 7),
                         '\nPpeao_preto8': (2, 8), '\nPtorre_branco1': (8, 1), '\nPtorre_branco2': (8, 8),
                         '\nPcavalo_branco1': (8, 2), '\nPcavalo_branco2': (8, 7), '\nPbispo_branco1': (8, 3),
                         '\nPbispo_branco2': (8, 6), '\nPrainha_branco': (8, 4), '\nPrei_branco': (8, 5),
                         '\nPpeao_branco1': (7, 1), '\nPpeao_branco2': (7, 2), '\nPpeao_branco3': (7, 3),
                         '\nPpeao_branco4': (7, 4), '\nPpeao_branco5': (7, 5), '\nPpeao_branco6': (7, 6),
                         '\nPpeao_branco7': (7, 7), '\nPpeao_branco8': (7, 8)}

    return posicoes_iniciais


def quadrado(square, border):   # Pinta quadrado limpo novamente:
    if border == True:
        if ((((square[0]) % 2) == 0) and (((square[1]) % 2) != 0)) or (
                (((square[0]) % 2) != 0) and (((square[1]) % 2) == 0)):
            pygame.draw.rect(tela, marrom, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho], 5)
        else:
            pygame.draw.rect(tela, bege, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho], 5)
    elif border == False:
        if ((((square[0]) % 2) == 0) and (((square[1]) % 2) != 0)) or (
                (((square[0]) % 2) != 0) and (((square[1]) % 2) == 0)):
            pygame.draw.rect(tela, marrom, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho])
        else:
            pygame.draw.rect(tela, bege, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho])


def select(pos, possibilidades, turn):

    keys = list(posicoes.keys())
    values = list(posicoes.values())
    peca = ''
    for i in range(len(values)):  # mostrando qual peca foi selecionada
        if values[i] == pos:
            peca = keys[i]

    if possibilidades != []:  # Limpando selecoes
        for p in range(len(possibilidades)):
            quadrado(possibilidades[p], True)
        possibilidades = []

    if turn == 1:  # Turno das brancas
        if 'Ppeao_branco' in peca:  # movimento do peao
            if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
                for i in range(len(values)):
                    if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('preto' in keys[i]):
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] - 1), tamanho, tamanho],
                                         5)
                        possibilidades.append(((pos[0] - 1), (pos[1] + 1)))

            if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
                for i in range(len(values)):
                    if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('preto' in keys[i]):
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] - 1), tamanho, tamanho],
                                         5)
                        possibilidades.append(((pos[0] - 1), (pos[1] - 1)))

            if (((pos[0] - 1), pos[1]) not in values) and (pos[0] - 1) != 0 and (pos[1]) != 0:  # Movimento comum
                pygame.draw.rect(tela, azul, [tamanho * (pos[1]), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] - 1), (pos[1])))

            if pos[0] == 7 and (((pos[0] - 2), pos[1]) not in values) and (
                    ((pos[0] - 1), pos[1]) not in values):  # Primeiro movimento do peao
                pygame.draw.rect(tela, azul, [tamanho * (pos[1]), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] - 2), (pos[1])))

    if turn == -1:  # Turno das pretas
        if 'Ppeao_preto' in peca:  # movimento do peao preto
            if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na direita
                for i in range(len(values)):
                    if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('branco' in keys[i]):
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] + 1), tamanho, tamanho],
                                         5)
                        possibilidades.append(((pos[0] + 1), (pos[1] - 1)))

            if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na esquerda
                for i in range(len(values)):
                    if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('branco' in keys[i]):
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] + 1), tamanho, tamanho],
                                         5)
                        possibilidades.append(((pos[0] + 1), (pos[1] + 1)))

            if (((pos[0] + 1), pos[1]) not in values) and (pos[0] + 1) != 9 and (pos[1]) != 9:  # Movimento comum
                pygame.draw.rect(tela, azul, [tamanho * (pos[1]), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] + 1), (pos[1])))

            if pos[0] == 2 and (((pos[0] + 2), pos[1]) not in values) and (((pos[0] + 1), pos[1]) not in values):  # Primeiro movimento do peao
                pygame.draw.rect(tela, azul, [tamanho * (pos[1]), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] + 2), (pos[1])))

    return possibilidades, pos


def move(pos, Old_Pos, posicoes, turn, possibilidades):

    for p in range(len(possibilidades)):  # Limpando selecao
        quadrado(possibilidades[p], True)

    keys = list(posicoes.keys())
    values = list(posicoes.values())

    if pos not in possibilidades and pos != Old_Pos:  # Para que o jogador siga as regras
        pygame.mixer.music.load("assets/sounds/wrong.ogg")
        pygame.mixer.music.play(1)
        return posicoes, turn, possibilidades

    if pos in possibilidades and pos != Old_Pos:
        pygame.mixer.music.load("assets/sounds/move.ogg")
        pygame.mixer.music.play(1)

    if pos != Old_Pos:
        print('aqui')
        turn = -turn  # Mudando o turno

    if pos in values:
        for i in range(len(values)):  # Retirando a peça anterior da memoria em caso de comer
            if values[i] == pos:
                posicoes[keys[i]] = None
                quadrado(pos, False)

    peca = ''
    for j in range(len(values)):  # Mostrando qual peca vai ser movida
        if values[j] == Old_Pos:
            peca = keys[j]
            posicoes[peca] = pos  # Mudando a posicao

    quadrado(Old_Pos, False)  # limpando local anterior da peca

    # Colocando a peca na nova posicao

    if 'Ppeao_branco' in peca:
        tela.blit(peao_branco, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Ptorre_branco' in peca:
        tela.blit(torre_branco, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Pcavalo_branco' in peca:
        tela.blit(cavalo_branco, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Pbispo_branco' in peca:
        tela.blit(bispo_branco, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Prainha_branco' in peca:
        tela.blit(rainha_branco, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Prei_preto' in peca:
        tela.blit(rei_branco, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Ppeao_preto' in peca:
        tela.blit(peao_preto, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Ptorre_branco' in peca:
        tela.blit(torre_preto, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Pcavalo_preto' in peca:
        tela.blit(cavalo_preto, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Pbispo_preto' in peca:
        tela.blit(bispo_preto, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Prainha_preto' in peca:
        tela.blit(rainha_preto, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'Prei_preto' in peca:
        tela.blit(rei_preto, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))

    return posicoes, turn, possibilidades


posicoes = Start()  # Iniciando o Jogo
jogo = True
selecao = ()  # tupla para armazenar selecao do jogador
possibilidades = []
turno = 1
OldPos = 0
while jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False
   
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()  # (x, y) localização do mouse
            coluna = location[0] // tamanho
            linha = location[1] // tamanho
            if selecao == (linha, coluna):
                if selecao == (0, 3) or selecao == (0, 4) or selecao == (0, 5) or selecao == (0, 6):  # Recomeçar
                    posicoes = Start()
                    turno = 1
                else:  # Movendo
                    posicoes, turno, possibilidades = move(selecao, OldPos, posicoes, turno, possibilidades)
                selecao = ()  # tornar seleçao vazia

            else:
                selecao = (linha, coluna)
                print(selecao)
                if selecao in posicoes.values():  # Apenas se a peca selecionada for a de seu turno
                    for i in range(len(list(posicoes.values()))):
                        if (list(posicoes.values())[i] == selecao) and (
                                ((turno == 1) and ('branco' in list(posicoes.keys())[i])) or (
                                (turno == -1) and ('preto' in list(posicoes.keys())[i]))):
                            possibilidades, OldPos = select(selecao, possibilidades, turno)
            pygame.display.update()

pygame.quit()
