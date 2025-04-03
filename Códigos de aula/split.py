linha = "João da Silva,josilva@gmail.com,47 9 9234"
partes = linha.split(",")

for p in partes:
    print(p)

print(f"Email: {partes[1]}")
##################################################################
a, b, c, d = [float(x) for x in input().strip().split(" ")]

a = float(a) * 2
b = float(b) * 3
c = float(c) * 4
d = float(d) * 1
media = (a + b + c + d) / 10
print(f"Media: {media:.1f}")
if media >= 7.0:
print("Aluno aprovado.")
elif media < 5.0:
print("Aluno reprovado.")
else:
print("Aluno em exame.")
exame = float(input())
print("Nota do exame:", exame)
nota = (exame + media) / 2
if nota >= 5:
print("Aluno aprovado.")
else:
print("Aluno reprovado.")
print(f"Media final: {nota:.1f}")
