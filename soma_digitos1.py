num = int(input('Me diga um número: '))
num1 = num
while True:
    if num // 10 < 1:
        print(int(soma))
        break
    ope = 1
    soma = 0
    while num // ope != 0:
        divi = num // ope
        ope *=10
    for i in range(1, num1):
        if ope < 1:
            num = soma
            break
        ope /= 10
        divi = num // ope
        num = num % ope
        soma = divi + soma