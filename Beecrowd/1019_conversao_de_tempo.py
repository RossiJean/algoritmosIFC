N = int(input())

horas = N // 3600
N %= 3600
minutos = N // 60
N %= 60

print(f"{horas}:{minutos}:{N}")
