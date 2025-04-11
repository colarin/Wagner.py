num = int(input('Me diga um número: '))
for i in range( 0, num + 1):
    multi = i
    for x in range(1, i ):
       multi = (multi * x) 
    print(f'fatorial de {i} é igual a {multi}')