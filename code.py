# -*- coding: utf-8 -*-

RESPONSE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def main():
    board = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    hErrado = heuristicaNumeroErrados(board)
    hManhattan = heuristicaManhattan(board)

    print hErrado
    print hManhattan

def heuristicaNumeroErrados(estado):
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
        passos até a posição certa
        """
        y = abs((value - 1) % 3 - i % 3) + abs((value - 1)//3 - i // 3)
        i = i + 1

        dist = dist + y

    return dist

if __name__ == '__main__':
    main()
