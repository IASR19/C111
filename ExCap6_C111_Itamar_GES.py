import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Ex1
space = pd.read_csv("space.csv", delimiter=";")
space_ = space['Company Name'].where(space['Location'].str.contains('USA')).unique()
space__ = space['Company Name'].where(space['Location'].str.contains('China')).unique()

space_eua = len(space_)
space_china = len(space__)

plt.title('Viagens Espaciais')
plt.xlabel('Países') #Legenda no eixo X
plt.ylabel('Nº de Viagens') #Legenda no eixo Y

plt.bar('China', space_china, align='center', alpha=0.5)
plt.bar('EUA', space_eua, align='center', alpha=0.5)

plt.show()


#Ex2
paises = pd.read_csv('paises.csv',delimiter=";")
paises_ = paises[paises['Region'].str.contains("NORTHERN AMERICA")]

plt.xlabel('Países') #Legenda no eixo X
plt.ylabel('Natalidade e Mortalidade') #Legenda no eixo Y
plt.title('Taxa de Natalidade e Mortalidade na America do Norte')
plt.plot(paises_['Country'], paises_['Birthrate'],  'o:r', paises_['Country'], paises_['Deathrate'], '*:b' )

plt.show()

