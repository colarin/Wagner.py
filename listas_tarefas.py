# agendas = {}
# def menu_tarefas():
#     print('Bem-vindo a lista de tarefas. O que deseja fazer?\n' 
#         '[C] Criar Tarefas \n' 
#         '[R] ler ou visualizar tarefas\n' 
#         '[U] Atualizar tarfas\n'
#         '[D] Deletar tarefas\n' 
#         '[S] Sair do programa')
#     opcao = input('Escolha uma opção: ').lower()
#     return opcao
# def criar_tarefas():
#     id = 0
#     print('lembre-se de colocar descrição ao lado da tarefa')
#     while True:
#         aux = []
#         id += 1
#         tarefa = input('Qual o nome da tarefa que deseja adiconar? ')
#         descricao = input('Qual a descrição da tarefa? ')
#         status = input('Qual o status da sua tarefa? (Feita/Pendente) ').lower()
#         resposta = input('Deseja adcionar mais tarefas(s/n): ').lower()
#         if status != 'feita' or status != 'pendente':
#             status = 'Pendente'
#         aux = descricao
#         if resposta == 's':
#             continue
#         elif resposta == 'n':
#             for k in agendas.keys():
#                 print(f'Id = {k}')
#                 for v in agendas.values():
#                     if v == 0:
#                         print(f'descricao = {v}')
#                     elif v == 1:
#                         print(f'status = {v}')
#             break
# while True:
#     escolha = menu_tarefas()
#     if escolha == 'c':
#         criar_tarefas()
aux = []
oi = 'oiiii'
casa = 'casa'
aux = oi
aux = casa
print(aux)