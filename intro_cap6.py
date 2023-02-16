# Capitulo 6 - Matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds
import pydataset as pds


# CRIANDO UM NP ARRAY
arr = np.array ([1,2,3,4])
y = arr*2

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.plot(arr,y)
plt.show()
