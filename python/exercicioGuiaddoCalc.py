while True:
    primeiroNumero = input('digite um numero: ')
    segundoNumero = input('digite outro numero: ')
    operador = input('digite um operadores (+-/*): ')

    numeros_validos = None

    num_1 = 0
    num_2 = 0

    try:
        num_1 = float(primeiroNumero)
        num_2 = float(segundoNumero)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('digite numeros validos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('digite um operador permitido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    print('resultado da sua conta: ', end='')
    if operador == '+':
        print(f'{num_1 + num_2}')
    elif operador == '-':
        print(f'{num_1 - num_2}')
    elif operador == '/':
        print(f'{num_1 / num_2}')
    elif operador == '*':
        print(f'{num_1 * num_2}')
    else:
        print('nunca deve chegar aqui')

    sair = input('quer sair? [s] pra sim ').lower().startswith('s')
    
    if sair is True:
        break

