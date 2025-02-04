cpf = '34877451005'
nove_digito = cpf[:9]
contador_regressivo_1 = 10
dez_digito = cpf[:10]
contador_regressivo_2 = 11

resultado_digito_1 = 0
resultado_digito_2 = 0

for digito_1 in nove_digito:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

for digito_2 in dez_digito:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)