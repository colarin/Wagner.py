num = int(input('Me diga um número: '))
ope = 10
soma = 0
divi = 0
while True:
    divi == num // ope
    if num // ope == 0:
        ope /= 10
        break
    ope *= 10
while num // ope != 0:
    divi = num // ope
    num = num % ope
    soma = divi + soma
    ope /= 10
print(f'A soma dos digitos é {soma}')
