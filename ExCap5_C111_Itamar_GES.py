import pandas as pd

paises = pd.read_csv("paises.csv", delimiter=";")
oceania = paises[paises["Region"].str.contains("OCEANIA")]

# Ex1

# A
print(oceania)
# B
cont = 0
for i in oceania:
    cont = cont + 1
print(cont)

# Ex2
print("\n")
print(paises["Literacy (%)"].mean())

# Ex3
area = paises.loc[paises["Population"].idxmax()]
print("\n")
print(area["Country"],
      area["Region"])

# Ex4

noCoast = (paises[paises["Coastline (coast/area ratio)"] == 0])
noCoast["Country"].to_csv("noCoast.csv",
                          sep=";",
                          header=False)
print("\n")
print(noCoast)
