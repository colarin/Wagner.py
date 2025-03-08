def sequencia_primo(num):
    for x in range(2, num):
        
        cont = 0
        for i in range(1, x + 1):
            divi = x % i
            if divi == 0:
                cont +=1
        if cont == 2:
                print(i)
num = int(input('Me diga um número: '))
sequencia_primo(num)