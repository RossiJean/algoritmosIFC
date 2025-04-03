#For loop
#repita 10 vezes
for i in range(1,11):
    #mostre o contador
    print("i=", i)

import random

s = 0

for i in range(0,10001):
    n = random.randint(1, 10001)
    s = s + n
    print(n)

m = s / 10000

print('média:', m)
