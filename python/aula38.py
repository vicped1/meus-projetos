string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'
salas = [
    ['Ana', 'Carlos',],
    ['João',], 
    ['Maria', 'Pedro', 'José', ], 
]

#p,b,*_, u = lista
#print(p,u)

#for nome in lista:
    #print(nome)

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')