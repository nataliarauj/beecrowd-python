pares = 0

for i in range(0,5):
    n = int(input())
    
    if n % 2 == 0:
        pares += 1

print('{} valores pares'.format(pares))