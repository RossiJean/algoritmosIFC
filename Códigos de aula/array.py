numbers = []

for i in range(10):
    n = input("Digite um número")
    numbers.append(n)

for i in range(10):
    print(f"vetor[{i}] = {numbers[i]}")
########################################################

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


numbers = []

for i in range(10):
    n = input("Digite um número")
    numbers.append(n)
bubbleSort(numbers)
print(numbers)
