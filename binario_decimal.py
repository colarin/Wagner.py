num = int(input('Digite um número binario: '))
soma = 0
ope = 10
decimal = 0
while num // ope != 0:
    divi = num // ope
    soma += 1
    ope *= 10
while True:
    ope /= 10
    divi = num // ope
    num = num % ope
    decimal = (divi * 2 **soma) + decimal
    soma -= 1
    if ope == 1:
        print(f'O número decimal é {decimal}')
        break