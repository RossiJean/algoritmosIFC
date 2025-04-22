a, b = map(int, input().split(" "))
total = 0
match a:
    case 1:
        total = b * 4.00
    case 2:
        total = b * 4.50
    case 3:
        total = b * 5.00
    case 4:
        total = b * 2.00
    case 5:
        total = b * 1.50
print(f"Total: R$ {total:.2f}")
