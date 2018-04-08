# -*- coding: utf-8 -*-
import sys
import copy


RESPONSE = [1, 2, 3, 4, 5, 6, 7, 8, 0]
USE_NUMEROS_ERRADOS = 0
USE_MANHATTAN = 1



def main():
    board = [1, 2, 3, 4, 5, 6, 7, 0, 8]

    bfs(board, USE_NUMEROS_ERRADOS)
    bfs(board, USE_MANHATTAN)

def hash(array):
    return ''.join(str(i) for i in array)


# TODO:
def bfs(estado, heuristica):

    if heuristica == USE_MANHATTAN or heuristica == USE_NUMEROS_ERRADOS:

        if heuristica == USE_MANHATTAN:
            print "Manhattan não disponível"
            return

    else:
        print "Use heuristica"
        return


    passos = 1

    if estado == RESPONSE:
        encontrado = True
        print "Passo " + str(passos)
        return

    lista = [estado]
    visitados = []

    encontrado = False
    while len(lista) > 0 and not encontrado:
        pai = lista[0]
        del lista[0]

        if hash(pai) not in visitados:
            visitados.append(hash(pai))
            filhos = geraFilhos(pai, heuristica)
            for filho in filhos:
                chave_filho = hash(filho)
                if chave_filho not in lista or chave_filho not in visitados:
                    lista.append(filho)
                    if filho == RESPONSE:
                        encontrado = True
                        print "Encontrado em " + str(passos) + " passos."
                        break         

        passos = passos + 1     


def heuristicaNumeroErrados(estado):
    """
    para sabe o número de itens que estão na posição errada, basta andar pelo
    vetor de resposta e pelo estado ao mesmo tempo e vendo quais eram iguias
    """
    print "recebido : " + str(estado)
    errado = 0
    for i,j in zip(RESPONSE, estado):
        if i != j:
            errado = errado + 1
    print "retorno : " + str(errado)
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

def geraFilhos(estado, heuristica):

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

        retorno = []

        """cria filhos"""
        for filho in filhos:
            novoEstado = copy.deepcopy(estado)
            print "ANTES DO FILHO ("+ str(filho) +") => (" + str(zero_pos) + ")" + str(novoEstado)
            i_posZero = zero_pos[1]*3 + zero_pos[0]
            i_posTroca = filho[1]*3 + filho[0]

            temp = novoEstado[i_posZero]
            novoEstado[i_posZero] = novoEstado[i_posTroca]
            novoEstado[i_posTroca] = temp
            print  "DEPOIS DO FILHO ("+ str(filho) +") => (" + str(zero_pos) + ")" + str(novoEstado)

            retorno.append(novoEstado)


        """ordena filhos por heuristica"""
        i = 0
        heuristizado = []
        while i < len(filhos):
            if heuristica == USE_NUMEROS_ERRADOS:
                heuristizado.append(heuristicaNumeroErrados(retorno[i]))
            elif heuristica ==USE_MANHATTAN:
                heuristizado.append(heuristicaManhattan(retorno[i]))
            else:
                print "heuristica não esperada"
                sys.exit(1)
            i = i + 1  

        print heuristizado
        return retorno
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
