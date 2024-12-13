"""
numero_inteiro = input('digite um numero inteiro: ')

try:
    numero = int(numero_inteiro)
    contaParInpar = numero %2
    if contaParInpar == 0:
        print(f'O numero {numero} ele e par ')
    else:
        print(f'O numero {numero} ele é inpar') 
except:
   print('digite apenas numeros inteiros')
"""
"""
data_local = input('digite a data de hoje: ')
try:
    data = float(data_local)
    if data >= 0 and data < 12:
        print('Bom dia')
    elif data >= 12 and data < 18:
        print('Boa tarde')
    elif data >= 18 and data <= 23:
        print('Boa noite')
    else:
        print('horario invalido')
except:
    print('digite apenas numeros')
"""
nome = input('Digite o seu nome: ')

if len(nome) <= 4:
    print('Seu nome e muinto curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome e normal')
elif len(nome) > 6:
    print('Seu nome e muito grande')