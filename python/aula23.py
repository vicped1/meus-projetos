string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('essa string não tem espaços')
print('fim do programa')