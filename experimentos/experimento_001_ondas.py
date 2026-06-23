import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

y = np.sin(x)

plt.plot(x, y)

plt.title("Primeira Onda")

plt.xlabel("Tempo")

plt.ylabel("Amplitude")

plt.grid(True)

plt.show()