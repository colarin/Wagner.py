num = int(input('Me diga um número: '))
inverso = 0
multi = 1
multi1 = 1
while num // multi != 0:
    divi = num // multi
    multi *= 10
multi /= 10
while True:
    divi = num // multi
    num = num % multi
    multi /= 10
    inverso = (divi * multi1) + inverso
    multi1 *= 10
    if num == 0:
        print(int(inverso))
        break