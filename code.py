# -*- coding: utf-8 -*-
import sys
import copy
import time
import random

RESPONSE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

""" SEM_HEURISTICA é usado APENAS para gerar filhos """
SEM_HEURISTICA = -1


USE_NUMEROS_ERRADOS = 0
USE_MANHATTAN = 1



def main():

    # CASOS_DE_TESTE = 2

    # board = copy.deepcopy(RESPONSE)
    # i = 1
    # estado = board
    # while i <= CASOS_DE_TESTE:
    #     print "==> "+ str(i) +" MOVIMENTO:"
    #     mutacoes = geraFilhos(estado, SEM_HEURISTICA)
    #     mutacao = random.randint(0, len(mutacoes) - 1)

    #     print mutacoes[mutacao]

    #     estado = copy.deepcopy(mutacoes[mutacao])

    #     bfs(mutacoes[mutacao], USE_NUMEROS_ERRADOS)
    #     bfs(mutacoes[mutacao], USE_MANHATTAN)

    #     i = i + 
    

    print "==> 1 MOVIMENTO"
    
    bfs([1, 2, 3, 4, 5, 6, 7, 0, 8], USE_MANHATTAN)
    bfs([1, 2, 3, 4, 5, 6, 7, 0, 8], USE_NUMEROS_ERRADOS)

    

    print "==> 2 MOVIMENTO"
    
    bfs([1, 2, 3, 4, 0, 6, 7, 5, 8], USE_MANHATTAN)
    bfs([1, 2, 3, 4, 0, 6, 7, 5, 8], USE_NUMEROS_ERRADOS)


    print "==> 3 MOVIMENTO"
    
    bfs([1, 2, 3, 0, 4, 6, 7, 5, 8], USE_MANHATTAN)
    bfs([1, 2, 3, 0, 4, 6, 7, 5, 8], USE_NUMEROS_ERRADOS)

    

    print "==> 4 MOVIMENTO"
    
    bfs([1, 2, 3, 7, 4, 6, 0, 5, 8], USE_MANHATTAN)
    bfs([1, 2, 3, 7, 4, 6, 0, 5, 8], USE_NUMEROS_ERRADOS)

    

    print "==> 5 MOVIMENTO"
    
    bfs([1, 2, 3, 7, 4, 6, 5, 0, 8], USE_MANHATTAN)
    bfs([1, 2, 3, 7, 4, 6, 5, 0, 8], USE_NUMEROS_ERRADOS)

    

    print "==> 6 MOVIMENTO"
    
    bfs([1, 2, 3, 7, 4, 6, 5, 8, 0], USE_MANHATTAN)
    bfs([1, 2, 3, 7, 4, 6, 5, 8, 0], USE_NUMEROS_ERRADOS)

    

    print "==> 7 MOVIMENTO"
    
    bfs([1, 2, 3, 7, 4, 0, 5, 8, 6], USE_MANHATTAN)
    bfs([1, 2, 3, 7, 4, 0, 5, 8, 6], USE_NUMEROS_ERRADOS)


    print "==> 8 MOVIMENTO"
    
    bfs([1, 2, 0, 7, 4, 3, 5, 8, 6], USE_MANHATTAN)
    bfs([1, 2, 0, 7, 4, 3, 5, 8, 6], USE_NUMEROS_ERRADOS)

    

    print "==> 9 MOVIMENTO"
    
    bfs([1, 0, 2, 7, 4, 3, 5, 8, 6], USE_MANHATTAN)
    bfs([1, 0, 2, 7, 4, 3, 5, 8, 6], USE_NUMEROS_ERRADOS)

    

    print "==> 10 MOVIMENTO"
    
    bfs([0, 1, 2, 7, 4, 3, 5, 8, 6], USE_MANHATTAN)
    bfs([0, 1, 2, 7, 4, 3, 5, 8, 6], USE_NUMEROS_ERRADOS)

    

    print "==> 11 MOVIMENTO"
    
    bfs([7, 1, 2, 0, 4, 3, 5, 8, 6], USE_MANHATTAN)
    bfs([7, 1, 2, 0, 4, 3, 5, 8, 6], USE_NUMEROS_ERRADOS)

    

    print "==> 12 MOVIMENTO"
    
    bfs([7, 1, 2, 5, 4, 3, 0, 8, 6], USE_MANHATTAN)
    bfs([7, 1, 2, 5, 4, 3, 0, 8, 6], USE_NUMEROS_ERRADOS)

    

    print "==> 13 MOVIMENTO"
    
    bfs([7, 1, 2, 5, 4, 3, 8, 0, 6], USE_MANHATTAN)
    bfs([7, 1, 2, 5, 4, 3, 8, 0, 6], USE_NUMEROS_ERRADOS)

    

    print "==> 14 MOVIMENTO"
    
    bfs([7, 1, 2, 5, 4, 3, 8, 6, 0], USE_MANHATTAN)
    bfs([7, 1, 2, 5, 4, 3, 8, 6, 0], USE_NUMEROS_ERRADOS)

    

    print "==> 15 MOVIMENTO"
    
    bfs([7, 1, 2, 5, 4, 0, 8, 6, 3], USE_MANHATTAN)
    bfs([7, 1, 2, 5, 4, 0, 8, 6, 3], USE_NUMEROS_ERRADOS)

    

    print "==> 16 MOVIMENTO"
    
    bfs([7, 1, 2, 5, 0, 4, 8, 6, 3], USE_MANHATTAN)
    bfs([7, 1, 2, 5, 0, 4, 8, 6, 3], USE_NUMEROS_ERRADOS)

    

    print "==> 17 MOVIMENTO"
    
    bfs([7, 1, 2, 0, 5, 4, 8, 6, 3], USE_MANHATTAN)
    bfs([7, 1, 2, 0, 5, 4, 8, 6, 3], USE_NUMEROS_ERRADOS)

    

    print "==> 18 MOVIMENTO"
    
    bfs([0, 1, 2, 7, 5, 4, 8, 6, 3], USE_MANHATTAN)
    bfs([0, 1, 2, 7, 5, 4, 8, 6, 3], USE_NUMEROS_ERRADOS)

    

    print "==> 19 MOVIMENTO"
    
    bfs([1, 0, 2, 7, 5, 4, 8, 6, 3], USE_MANHATTAN)
    bfs([1, 0, 2, 7, 5, 4, 8, 6, 3], USE_NUMEROS_ERRADOS)

    

    print "==> 20 MOVIMENTO"
    
    bfs([1, 2, 0, 7, 5, 4, 8, 6, 3], USE_MANHATTAN)
    bfs([1, 2, 0, 7, 5, 4, 8, 6, 3], USE_NUMEROS_ERRADOS)


def hash(array):
    return ''.join(str(i) for i in array)


# TODO:
def bfs(estado, heuristica):
    
    """ tempo de ínicio """
    start_time = time.time()
    if heuristica == USE_MANHATTAN or heuristica == USE_NUMEROS_ERRADOS:

        if heuristica == USE_MANHATTAN:
            print "Usando MANHATTAN"
        else:
            print "Usando NUMEROS_ERRADOS"

    else:
        print "Use heuristica"
        return


    passos = 1

    if estado == RESPONSE:
        encontrado = True
        tempo_execucao = (time.time() - start_time) * 1000
        print "Encontrado em " + str(passos) + " passos. Em " + str(tempo_execucao) + " ms."
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
                        tempo_execucao = (time.time() - start_time) * 1000
                        print "Encontrado em " + str(passos) + " passos. Em " + str(tempo_execucao) + " ms."
                        break         

        passos = passos + 1     


def heuristicaNumeroErrados(estado):
    """
    para sabe o número de itens que estão na posição errada, basta andar pelo
    vetor de resposta e pelo estado ao mesmo tempo e vendo quais eram iguias
    """
    # print "recebido : " + str(estado)
    errado = 0
    for i,j in zip(RESPONSE, estado):
        if i != j:
            errado = errado + 1
    # print "retorno : " + str(errado)
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

"""
gera filhos dado um estado e um heuristica. os filhos criados são ordenados
pelos menores valres de cada heurística.

Exemplo: há 3 possíveis filhos. Com h* de 3, 0 e 4, então o retorno será:
0, 3 e 4 
"""
def geraFilhos(estado, heuristica):

    zero_pos = posicaoZero(estado)
    # print "zeropos => " + str(zero_pos)

    if zero_pos != -1:

        x,y = zero_pos

        filhos = []

        # CASE 1 ESPAÇO EM BRANCO VAI PARA CIMA
        if not y - 1 < 0:
            # print 'da para ir para cima'
            filhos.append([x, y - 1])

        # CASE 2 ESPAÇO EM BRANCO VAI DIREITA
        if not x + 1 > 2:
            # print 'da para ir para direita'
            filhos.append([x + 1, y])

        # CASE 3 ESPAÇO EM BRANCO VAI PARA BAIXO
        if not y + 1 > 2:
            # print 'da para ir para baixo'
            filhos.append([x, y + 1])

        # CASE 4 ESPAÇO EM BRANCO VAI PARA ESQUERDA
        if not x - 1 < 0:
            # print 'da para ir para esquerda'
            filhos.append([x - 1, y])

        retorno = []

        """cria filhos"""
        for filho in filhos:
            novoEstado = copy.deepcopy(estado)
            # print "ANTES DO FILHO ("+ str(filho) +") => (" + str(zero_pos) + ")" + str(novoEstado)
            i_posZero = zero_pos[1]*3 + zero_pos[0]
            i_posTroca = filho[1]*3 + filho[0]

            temp = novoEstado[i_posZero]
            novoEstado[i_posZero] = novoEstado[i_posTroca]
            novoEstado[i_posTroca] = temp
            # print  "DEPOIS DO FILHO ("+ str(filho) +") => (" + str(zero_pos) + ")" + str(novoEstado)

            retorno.append(novoEstado)


        """ordena filhos por heuristica"""
        i = 0
        heuristizado = []
        while i < len(filhos):
            if heuristica == USE_NUMEROS_ERRADOS:
                heuristizado.append(heuristicaNumeroErrados(retorno[i]))
            elif heuristica == USE_MANHATTAN:
                heuristizado.append(heuristicaManhattan(retorno[i]))
            elif heuristica == SEM_HEURISTICA:
                heuristizado.append(1)
            else:
                print "heuristica não esperada"
                sys.exit(1)
            i = i + 1  

        # print heuristizado
        heuristizado, retorno = bubbleSort(heuristizado, retorno)
        return retorno
    return 0

def bubbleSort(heuristizado, retorno):
    for passnum in range(len(heuristizado)-1,0,-1):
        for i in range(passnum):
            if heuristizado[i]>heuristizado[i+1]:
                temp = heuristizado[i]
                heuristizado[i] = heuristizado[i+1]
                heuristizado[i+1] = temp

                temp = retorno[i]
                retorno[i] = retorno[i + 1]
                retorno[i+1] = temp

    return heuristizado, retorno

def posicaoZero(estado):
    i = 0
    while i < 9:
        if estado[i] == 0:
            # print "0 na posição " + str(i) + " do array."
            x = i % 3
            y = i // 3
            return x,y
        i = i + 1
    return -1


if __name__ == '__main__':
    main()
