num = int(input('Me diga um número:'))
soma = 0
ope = 10
num1 = num
soma1 = 0
while True:
    soma1 += 1
    if num // ope == 0:
        ope /= 10
        break
    ope *= 10
while True:
    divi = num // ope
    num = num % ope
    soma = (divi ** soma1) + soma
    ope /= 10
    if soma == num1:
        print(f'o número {num1} é um armstrong')
        break
    elif num == 0:
        print('não é um armstrong')
        break