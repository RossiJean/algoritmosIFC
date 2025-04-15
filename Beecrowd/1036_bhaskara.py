A, B, C = map(float, input().split(" "))

delta = B**2 - (4 * A * C)

try:
    R1 = (delta ** (1 / 2) - B) / (2 * A)
    R2 = (-(delta ** (1 / 2)) - B) / (2 * A)

    if delta > 0:
        print(f"R1 = {R1:.5f}")
        print(f"R2 = {R2:.5f}")
    else:
        print("Impossivel calcular")
except:
    print("Impossivel calcular")
