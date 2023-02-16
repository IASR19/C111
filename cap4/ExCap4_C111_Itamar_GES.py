import numpy as np # Apelidando numpy de np

#1
arr1 = np.arange(0,21,1)
print(arr1)

print('')
print('')

#2
arr2 = np.arange(0,51,2)
arr3 = np.arange(100,48,-2)
arr4 = np.concatenate([arr2,arr3])
arr4 = np.sort(arr4)
print(arr2)
print(arr3)
print(arr4)

print('')
print('')

#3
arr5 = np.flip(arr4)
print(arr5)

print('')
print('')

#4
array1 = np.ones(12).reshape(3,4)
print(array1)

print('')
print('')

#5
mtz = np.arange(0,15,1).reshape(3,5)
matriz = (mtz.shape)
print((min(matriz)) * (max(matriz)))
# Número impar.





