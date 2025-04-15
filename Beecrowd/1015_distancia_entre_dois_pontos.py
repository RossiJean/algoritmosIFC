a, b = map(float, input().split(" "))
c, d = map(float, input().split(" "))

formula = (((c - a) ** 2) + ((d - b) ** 2)) ** (1 / 2)
print(f"{formula:.4f}")
