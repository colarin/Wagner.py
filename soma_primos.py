cont = int(input('Me diga um número: '))
cod = 0
soma = 0
for i in range(1, cont + 1):
    cod = 0
    for x in range(1, i + 1):
        divi = i % x
        if divi == 0:
            cod += 1
    if cod == 2:
        soma = i + soma
print(f'O resultado da soma dos números primos é {soma}')