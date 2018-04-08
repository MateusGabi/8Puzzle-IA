# -*- coding: utf-8 -*-
import copy

RESPONSE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def main():
    board = [1, 2, 3, 4, 5, 6, 7, 0, 8]


    buscaHeuristicaNumeroErrados(board)
    buscaHeuristicaManhattan(board)

# TODO:
def buscaHeuristicaNumeroErrados(estado):
    g = geraFilhos(estado)

    if g != 0:
        zero_pos,filhos = g
        hErradoAgora = heuristicaNumeroErrados(estado)
        print "hErradoAgora = " + str(hErradoAgora)

        encontrado = False

        for filho in filhos:
            if not encontrado:
                novoEstado = copy.deepcopy(estado)
                print "ANTES DO FILHO ("+ str(filho) +") => (" + str(zero_pos) + ")" + str(novoEstado)
                i_posZero = zero_pos[1]*3 + zero_pos[0]
                i_posTroca = filho[1]*3 + filho[0]

                temp = novoEstado[i_posZero]
                novoEstado[i_posZero] = novoEstado[i_posTroca]
                novoEstado[i_posTroca] = temp
                print  "DEPOIS DO FILHO ("+ str(filho) +") => (" + str(zero_pos) + ")" + str(novoEstado)

                hNovoEstado = heuristicaNumeroErrados(novoEstado)
                if hNovoEstado == 0:
                    print "Achou"
                    encontrado = True



# TODO
def buscaHeuristicaManhattan(estado):

    hManhattan = heuristicaManhattan(estado)

    print hManhattan

def heuristicaNumeroErrados(estado):
    """
    para sabe o número de itens que estão na posição errada, basta andar pelo
    vetor de resposta e pelo estado ao mesmo tempo e vendo quais eram iguias
    """
    errado = 0
    for i,j in zip(RESPONSE, estado):
        if i != j:
            errado = errado + 1
    return errado

def heuristicaManhattan(estado):
    # a posição certa é valor - 1
    i = 0
    dist = 0
    for value in estado:
        """
        se não esta na posição certa, temos que calcular o menor numero de
        passos até a posição certa.

        % anda pela linha
        // anda pela coluna
        """
        y = abs((value - 1) % 3 - i % 3) + abs((value - 1)//3 - i // 3)
        i = i + 1

        dist = dist + y

    return dist

def geraFilhos(estado):

    zero_pos = posicaoZero(estado)
    print "zeropos => " + str(zero_pos)

    if zero_pos != -1:

        x,y = zero_pos

        filhos = []

        # CASE 1 ESPAÇO EM BRANCO VAI PARA CIMA
        if not y - 1 < 0:
            print 'da para ir para cima'
            filhos.append([x, y - 1])

        # CASE 2 ESPAÇO EM BRANCO VAI DIREITA
        if not x + 1 > 2:
            print 'da para ir para direita'
            filhos.append([x + 1, y])

        # CASE 3 ESPAÇO EM BRANCO VAI PARA BAIXO
        if not y + 1 > 2:
            print 'da para ir para baixo'
            filhos.append([x, y + 1])

        # CASE 4 ESPAÇO EM BRANCO VAI PARA ESQUERDA
        if not x - 1 < 0:
            print 'da para ir para esquerda'
            filhos.append([x - 1, y])

        return zero_pos,filhos
    return 0

def posicaoZero(estado):
    i = 0
    while i < 9:
        if estado[i] == 0:
            print "0 em " + str(i)
            x = i % 3
            y = i // 3
            return x,y
        i = i + 1
    return -1


if __name__ == '__main__':
    main()
