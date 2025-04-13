def calculadora():
    import math
    resultado = 0
    conti = 0
    print(f'{"CALCULADORA":-^45}')
    num1 = float(input('Me diga um número: '))
    print('='*45)
    while True:
        operacao = input('Qual a operação você deseja:\n'
                    'somar (+)\n'
                    'subtrair (-)\n' 
                    'dividir (/)\n'
                    'multiplicar (*)\n' 
                    'exponencial (**)\n'
                    'raiz quadrada (*/)\n'
                    'operação: ')
        if operacao == 'raiz quadrada' or operacao == '*/':
            print('='*45)
            resultado = num1
            num1 = resultado
            resultado = math.sqrt(resultado)
            print(resultado)
            print('='*45)
            conti = input('deseja continuar?\n '
                      'sim(1)\n'
                      'não(2)\n'
                      'resposta: ')
        print('='*45)
        if conti == 'não' or conti == '2':
                print(f'O resultado é {resultado}')
                print('='*45)
                break
        elif conti == 'sim' or conti == '1':
            continue
        num = float(input('Número: '))
        print('='*45)
        if operacao == "somar" or operacao == '+':
            resultado = num1 + num
            num1 = resultado
            print(resultado)
            print('='*45)
        elif operacao == 'subtrair' or operacao == '+':
            resultado = num1 - num
            num1 = resultado
            print(resultado)
            print('='*45)
        elif operacao == 'dividir' or operacao == '/':
            if num == 0:
                print('Essa ação não pode ser feita')
                break
            resultado = num1 / num
            num1 = resultado
            print(resultado)
            print('='*45)
        elif operacao == 'multiplicar' or operacao == '*':
            resultado = num1 * num
            num1 = resultado
            print(resultado)
            print('='*45)
        elif operacao == 'exponencial' or operacao == '**':
            resultado = num1 ** num
            num1 = resultado
            print(resultado)
            print('='*45)
        conti = input('deseja continuar?\n '
                      'sim(1)\n'
                      'não(2)\n'
                      'resposta: ')
        print('='*45)
        if conti == 'não' or conti == '2':
            print(f'O resultado é {resultado}')
            print('='*45)
            break
calculadora()
