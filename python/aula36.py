frase = '           olha só que         ,       coisa interessante         '
palavras_cruas = frase.split(',')

palavras = []
for i, frase in enumerate(palavras_cruas):
    palavras.append(palavras_cruas[i].split())

#print(palavras_cruas)
#print(palavras)
frases_unidas = ', '.join(palavras)
print(frases_unidas)