entrada = input('digite [e] para Entrar e [s] para Sair ')
if entrada == 'e':
    senha_digitada = input('Senha: ')

senha_permitida = '1234'
if entrada == 'e' and senha_digitada == senha_permitida:
    print('voce entrou no sistema')
elif entrada == 's':
    print('Voce Saiu do sistema')
else:
    print('digite e ou s')