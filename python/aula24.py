frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum'
i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais = ' '
while i < len(frase):
   letra_atual = frase[i]

   if letra_atual == ' ':
       i += 1
       continue

   num_de_vezes_que_apareceu = frase.count(letra_atual) 

   if qtd_apareceu_mais_vezes < num_de_vezes_que_apareceu:
       qtd_apareceu_mais_vezes = num_de_vezes_que_apareceu
       letra_que_apareceu_mais = letra_atual
   
   i += 1
print(f'A letra que mais apareceu foi "{letra_que_apareceu_mais}" com {qtd_apareceu_mais_vezes} aparições')