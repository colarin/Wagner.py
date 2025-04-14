def jogo_adivinhacao():
    import random
    aleatorio = random.randint(1, 100)
    tentativas = 0
    print(f'{'JOGO DE ADIVINHAÇÃO':^50}')
    print(f'{'bem-vindo ao jogo de adivinhação':^50}')
    while True:
        num = int(input('Me diga um número de 1 a 100: '))
        if num == aleatorio:
            print(f'{num} Número corretooo, parabéns!!')
            print(f'Ao todo, você tentou {tentativas} vezes')
            break
        elif num < aleatorio:
            print(f'Seu número {num} está menor')
            tentativas += 1
        elif num > aleatorio:
            print(f'Seu número {num} está maior')
            tentativas += 1
jogo_adivinhacao()