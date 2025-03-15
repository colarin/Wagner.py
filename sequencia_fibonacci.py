num = int(input('me diga quntos números você quer: '))
cont1 = 1
cont2 = 0
for cont in range(0, num):
    soma = cont1 + cont2
    cont2 = soma
    cont1 = cont2 - cont1
    print(soma)