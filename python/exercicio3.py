primeiro_valor = input("digite um valor: ")
segundo_valor = input("digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} è maior do que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} e igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} è maior do que o {primeiro_valor=}')