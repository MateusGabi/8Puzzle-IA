# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = [1,2,5,10,46,76,106,154,304,444,1080,1426,2730,4264,5866,4104,2284,1302,946,1538]
c = [1,4,7,12,48,78,126,156,306,446,826,1182,2642,4440,6940,5966,2346,1368,1014,1582]


# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, b, 'k--', label='Posicoes Erradas')
ax.plot(a, c, 'k:', label='Distancia de Manhattan')

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()