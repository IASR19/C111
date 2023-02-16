'''

Nome: Itamar Augusto Silva Ribeiro
Matrícula: 91
Curso: GES

'''

# 1)
print('Ex1')
times_campeonato = ['Real Madrid', 'Betis', 'Barcelona', 'Bilbao', 'Villareal']
print("3 primeiros colocados:")
print(times_campeonato[:3])
print("2 ultimos colocados:")
print(times_campeonato[3:])
print("Posicao Barcelona:")
print(times_campeonato.index('Barcelona') + 1)
print("Ordenando os times em ordem alfabética:")
print(sorted(times_campeonato))

print('')
print('')

# 2
print('Ex2')
loja1 = {'Xiaomi Redmi 7', 'Xiaomi Redmi 9', 'Xiaomi Redmi 10'}
loja2 = {'iPhone 13', 'iPhone 11', 'iPhone XS'}
print("Loja 1:")
print(loja1)
print("Loja 2")
print(loja2)
print("Smartphones união das lojas")
print(loja1 | loja2)

print('')
print('')

# 3
print('Ex3')
SITUACAO = {
    'Nome do Aluno': 'Carimbo',
    'NP1': 95,
    'NP2': 25
}

print(SITUACAO)

SITUACAO['MEDIA'] = ((SITUACAO['NP1'] + SITUACAO['NP2']) / 2)
print('')
print('MEDIA: ')
print(SITUACAO['MEDIA'])
print('')
print('SITUACAO:')
if SITUACAO['MEDIA'] < 60: 
    print('Aluno RP')

else: 
    print('Aluno AP')


