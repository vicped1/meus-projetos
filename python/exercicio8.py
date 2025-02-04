cpf_enviado = '61668309394'
nove_digito = cpf_enviado[:9]
contador_regressivo_1 = 10
dez_digito = cpf_enviado[:10]
contador_regressivo_2 = 11

resultado_digito_1 = 0
resultado_digito_2 = 0

for digito in nove_digito:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

for digito in dez_digito:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'

if cpf_enviado == cpf_gerado:
    print(f'o cpf enviado {cpf_enviado} é válido')
else:
    print('cpf inválido')