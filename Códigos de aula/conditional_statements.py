a = input("digite um número")
b = input("digite outro número")
if a < b:
	print(a, b)
else:
	print(b, a)
###################################################################
a = int(input("digite um número"))
b = int(input("digite outro número"))
c = int(input("digite outro número"))
if a < b < c:
    print(a, b, c)
else:
    if b < a < c:
        print(b, a, c)
    if c < a < b:
        print(c, a, b)
    if c < b < a:
        print(c, b, a)
    if b < c < a:
        print(b, c, a)
    if a < c < b:
        print(a, c, b)
