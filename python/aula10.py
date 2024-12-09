#nome = 'pedro'
#print('e' in nome)
#print('a' in nome)
#print('a' not in nome)
#print(nome[2])
#print(nome[-3])

nome = input('digite o seu nome: ')
encontrar = input('Digite o que voce quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')
