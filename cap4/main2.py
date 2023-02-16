import numpy as np
# SEGUNDO ENCONTRO DE NUMPY
# NUMEROS ALEATORIOS

# SEMENTE ALEATORIA
np.random.seed(5)

# 1. DENTRO DE UMA JANELA
arr = np.random.randint(1,20,10)
#print(arr)
#print(np.unique(arr,return_counts=True))

# DISTRIBUICAO DE PROBABILIDADE
arr2 = np.random.rand(10)
# FAZENDO UM BROADCASTING
#print(arr2*100)

# MATRIZ DE VALORES
mtz = np.arange(1, 21, 1).reshape(4,5)
#print(mtz)
#print(mtz.sum(axis=1)[0])


########## EXERCICIOS PAGINA 19

# CONDICIONAIS NO NUMPY
#print(mtz%2==1)
#print(mtz[mtz%2==1])

# ATENCAO NO SLICING
arr = mtz[0].copy()
arr[0] = 1000
#print(mtz)
#print(arr)

# SUBPACOTE CHAR DO NUMPY
arr = np.array(['Mari','Itamar','Bruno'])
#print(np.char.find(arr,'a'))
#print(arr[np.char.find(arr,'a') > 0])

# Exercicio 3 (Analisar Dataset) - Página 27