aluno = []
def menu():
    escolha = int(input('O que você deseja fazer? \n' \
    'Adicionar alunos (1): \n' \
    'Remover alunos (2): \n' \
    'Ver alunos (3): \n' \
    'sair (4):\n' \
    'resposta: '))
    return escolha
def adicionar_alunos():
    alunos_cadas = input('Qual o aluno você deseja cadastrar? ')
    bolean = True
    for y in aluno:
        if y == alunos_cadas:
            print('Aluno já está adicionado!')
            bolean = False
    if bolean == True:
        aluno.append(alunos_cadas)
        print('aluno adicionado com sucesso!!')
def remover_alunos():
    bolean = True
    if len(aluno) == 0:
        print('Não existe alunos cadastrados')
    elif len(aluno) != 0:
        remover = input('Qual aluno você deseja remover? ')
        for x, y in enumerate(aluno):
            if y == remover:
                aluno.remove(remover)
                print('Aluno removido com sucesso!')
                bolean = False
                break
        if bolean == True:
            print('Aluno não encontrado!')
while True:
    print('='*45)
    rece = menu()
    if rece == 1:
        print('='*45)
        adicionar_alunos()
    elif rece == 2:
        print('='*45)
        remover_alunos()