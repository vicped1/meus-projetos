condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')