# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = [
    0.0579357147217,
    0.114917755127,
    0.231027603149,
    0.361204147339,
    1.37901306152,
    2.27093696594,
    3.38101387024,
    4.76813316345,
    9.74297523499,
    16.263961792,
    49.3049621582,
    71.9468593597,
    187.988996506,
    437.371015549,
    682.032823563,
    373.097896576,
    162.008047104,
    63.2200241089,
    40.1258468628,
    78.8869857788
]


c = [
    0.0989437103271,
    0.288009643555,
    0.431776046753,
    0.550985336304,
    1.80697441101,
    2.73180007935,
    4.42600250244,
    5.41305541992,
    11.1930370331,
    17.1389579773,
    37.4789237976,
    58.1150054932,
    189.996004105,
    473.384141922,
    926.525831223,
    775.340795517,
    185.796022415,
    71.9640254974,
    46.450138092,
    86.6129398346
]


# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, b, 'k--', label='Posicoes Erradas')
ax.plot(a, c, 'k:', label='Distancia de Manhattan')

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()