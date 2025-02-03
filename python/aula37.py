salas = [
    ['Ana', 'Carlos',],
    ['João',], 
    ['Maria', 'Pedro', 'José', ], 
]

#print(salas[1][0])
#print(salas[0][1])
#print(salas[2][2])
#print(salas[2][3][2])

for sala in salas:
    print(f'a sale é {sala}')
    for aluno in sala:
        print(aluno)