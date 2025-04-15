dias = int(input())

ano = dias // 365
dias %= 365
mes = dias // 30
dias %= 30

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dias, "dia(s)")
