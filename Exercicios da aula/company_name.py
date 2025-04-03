f = open("/home/ifc/Área de trabalho/archive/companies_sorted.csv", "r")

menor_ano = 2025.0
menorAnoLinha = []
for linha in f:
    partes = linha.split(",")
    if len(partes) > 10 and partes[3].isnumeric():
        ano = float(partes[3])
        if ano < menor_ano:
            menor_ano = ano
            menorAnoLinha = linha

print(menor_ano)
print(menorAnoLinha)


'''retornou 4.0
6390069,"create land capital limited (sfc types 1,2,4,5,6,9)",,,,1 - 10,,,linkedin.com/company/create-land-capital-limited,0,1
talvez arquivo csv tenha erro de formatação.
'''
