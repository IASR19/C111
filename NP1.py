import numpy as np

brands = np.loadtxt('brands.csv', delimiter=";", dtype=str, encoding = 'utf-8', skiprows=1)


#Questão 1:
# Mostre o quanto ($) a empresa Google valorizou de 2021 para 2022;

arr = brands[0:]
arr_values = arr[arr[:,0] == 'Google',9]
arr_names = arr[arr[:,0] == 'Google',10]
print(arr_values)
print(arr_names)
print(arr_values - arr_names)


#Questão 2:
# Mostre quantas marcas neste dataset possuem a palavra “Group” em seu nome;
for group in brands[:,0]:
    busca = np.char.find(brands,0)
    if(busca.find('group'!=-1)):
    print(busca)

#Questão 3
#Mostre o nome e qual seria o valor de mercado das 5 primeiras empresas deste dataset em 2023 caso tivessem um aumento de 10%;
arr = brands[0:]
arr_values = arr[arr[:,0],9]
print(arr_values+(arr_values*(10/100)))


#Questão 4
# Faça um Slicing no dataset e extraia apenas as colunas "nome da marca, por quem foi
# fundada e o ano que ela foi fundada". Em seguida, mostre apenas o nome das empresas
# fundadas depois dos anos 2000;

unique,counts = np.unique (brands[:,0], return_counts=True)
print("marca\t \Quem\t \Ano\t\t\t\t\t\t")
for i in range (len(unique)):
    print("{}\t\{}:{}").format(i+1,unique[i],counts[i])


#Questão 5
#Busque os diferentes anos em que as empresas foram fundadas. Em seguida, mostre em qual ano mais empresas abriram as portas.
arr = np.array(brands[:, 2], dtype=np.float)
unique,counts = np.unique(brands[:,2], return counts = True)
for i in range (len(unique)):
    print(unique[i])
