num = int(input('Qual número começa o intervalo? '))
num1 = int(input('Qual número termina o intervalo? '))
cont = num
while cont != num1:
    num = cont
    soma1 = 0
    ope = 1
    soma = 0
    while num // ope != 0:
        soma1 += 1
        divi = num // ope
        ope *= 10
    ope /= 10
    while True:
        divi = num // ope
        num = num % ope
        soma = (divi ** soma1) + soma
        ope /= 10
        if soma == cont:
            print(f'o número {cont} é um armstrong')
            cont += 1
            break
        elif num == 0:
            cont += 1
            break