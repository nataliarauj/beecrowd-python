c = int(input())

for i in range(c):
    nome, forca = input().split()
    forca = int(forca)

    if nome != 'Thor':
        print('N')
    else:
        print('Y')