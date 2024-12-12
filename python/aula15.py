velocidade = 62
local_carro = 102

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_acima = velocidade > RADAR_1
carro_multado_rad = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_multado_rad and velocidade_acima

if velocidade_acima:
    print('O carro esta acima da velocidade permitida')

if  carro_multado:
    print('O carro foi multado')
else:
    print('O carro não foi multado')