# condicao1 = 10 == 10
# condicao2 = 10 == 11
# primeira_variavel= 'valor' if condicao1 else 'outro valor'
# segunda_variavel = 'valor' if condicao2 else 'outro valor'
# print(primeira_variavel)
# print(segunda_variavel)
digito = 10
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)