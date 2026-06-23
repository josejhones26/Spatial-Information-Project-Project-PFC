import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

onda1 = np.sin(x)

onda2 = np.sin(x)

resultado = onda1 + onda2

plt.plot(x, onda1, label="Onda 1")
plt.plot(x, onda2, label="Onda 2")
plt.plot(x, resultado, label="Resultado")

plt.legend()
plt.grid(True)

plt.show()
