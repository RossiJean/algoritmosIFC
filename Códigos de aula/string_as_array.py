frase = "Olá tudo bem com você"

# percorrer a frase em cada caracter
for c in frase:
    print(c)

# remover os acentos da frase
frase = frase.replace("á", "a")
frase = frase.replace("ê", "e")

print(frase)
