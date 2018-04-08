# 8Puzzle-IA

![Exemplo](https://sandipanweb.files.wordpress.com/2017/03/sol_a0.gif?w=676)

Dado um estado, encontrar a solução usando busca em largura e heurística (Manhattan e Número de Errados).

### Heurísticas

**Estado Inicial**

A|A| A 
-|-|-
7|8|4
5|0|3
2|6|1

**Estado Final**

A|A| A 
-|-|-
1|2|3
4|5|6
7|8|0
#### Manhattan

O Valor da Distância de Manhattan é de: `2 + 3 + 3 + 1 + 2 + 1 + 3 + 2 + 4 = 21`

#### Posições Erradas

O Valor das Posições Erradas é de: `1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 9`
