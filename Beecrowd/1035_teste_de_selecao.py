A, B, C, D = map(int, input().split(" "))

if A % 2 == 0:
    if C > 0 and D > 0:
        if (C + D) > (A + B):
            if B > C and D > A:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")

        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
