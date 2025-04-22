A, B, C = map(float, input().split())
if A < B + C and B < C + A and C < B + A:
    print(f"Perimetro = {(A+B+C):.1f}")
else:
    print(f"Area = {(((A+B)/2)*C):.1f}")
