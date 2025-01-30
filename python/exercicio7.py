import os

compras = []
while True:
    
    print('Selecione uma opicão')
    opcao = input('[i, a, l] i para inserir, a para apagar, l para listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Digite o nome do item: ')
        compras.append(valor)
    elif opcao == 'a':
        indice_str = input('Digite o indice do item que deseja apagar: ')
        try:
            indice = int(indice_str)
            del compras[indice]
        except ValueError:
            print('digite apenas números inteiros')
        except IndexError:
            print('digite apenas indices que estão na lista')
    elif opcao == 'l':
        os.system('cls')

        if len(compras) == 0:
            print('Lista vazia')
        
        for i, valor in enumerate(compras):
            print(i, valor)
    else:
        print('Opção inválida')
    
    