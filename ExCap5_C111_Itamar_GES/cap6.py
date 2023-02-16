# Capitulo 6 - Matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# CRIANDO UM NP ARRAY
x = np.array ([1,2,3,4])
y = x*2
y2 = x*x

# PLOTANDO DOIS GRAFICOS LADO A LADO

plt.subplot(1,2,1)
plt.title('Funcao Linear')
plt.plot(x,y,'r-')

# COLOCANDO NOME NOS EIXOS
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.subplot(1,2,2)
plt.title('Funcao Exponencial')
plt.plot(x,y2,'b--')


# COLOCANDO NOME NOS EIXOS
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# CUSTOMIZANDO NOSSO GRAFICO
formato = 's--g'

# PLOTANDO 2 GRAFICOS NO MESMO PLANO
#plt.plot(x,y,'s-b',x,y2,'o--g')

#plt.plot(x,y,formato, linewidth = 3, markersize = 20)
plt.show()


