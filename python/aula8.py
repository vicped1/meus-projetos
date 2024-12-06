entrada = input('digite [e] para Entrar e [s] para Sair ')
if entrada == 'e' or 'E':
    senha_digitada = input('Senha: ')

senha_permitida = '1234'

if entrada == 'e' or 'E' and senha_digitada == senha_permitida:
    print('voce entrou no sistema')
elif entrada == 's' or 'S':
    print('Voce Saiu do sistema')
else:
    print('digite e ou s')