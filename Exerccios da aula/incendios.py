f = open("/home/ifc/Downloads/amazon_UTF8_CLEANED.csv", "r")
soma = 0
for linha in f:
    partes = linha.split(",")
    if partes[0] == "2010" and partes [1] == "Santa Catarina"
        partes[3] = int(partes[3])
        soma += partes[3]

f.close()
print("O total de incêndios é de:", soma)
