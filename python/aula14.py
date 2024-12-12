numero = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero)
    print(f'o dobro de {numero} é {numero_float * 2:.0f}')
except:
    print('Isso não é um numero')


#if numero.isdigit():
    #numero_float = float(numero)
    #print(f'o dobro de {numero} é {numero_float * 2:.0f}')
#else:
    #print('Isso não é um numero')
