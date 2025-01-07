qtd_linhas = 5
qtd_colunas = 5

coluna = 1
linha = 1
while coluna <= qtd_colunas:
    while linha <= qtd_linhas:
        print(f'{coluna=}, {linha=}')
        linha += 1
    coluna += 1
    linha = 1


print('Acabou')