# NOME: Luis Wagner Araújo Colares Filho
# NOME: José Satiro De Lima
import json
def carregar_agenda():
    with open ('agenda.json', 'r') as f:
        return json.load (f)
def menu():
    print('+' + '-' * 38 + '+')
    print(f'|{"AGENDA DE CONTATOS":^38}|')
    print('+' + '-' * 38 + '+')
    print(f'| {"1":<2} - {"Adicionar contato":<30}  |')
    print(f'| {"2":<2} - {"Buscar contato":<30}  |')
    print(f'| {"3":<2} - {"Editar contato":<30}  |')
    print(f'| {"4":<2} - {"Remover contato":<30}  |')
    print(f'| {"5":<2} - {"Sair":<30}  |')
    print('+' + '-' * 38 + '+')
    opcao = input('>> Escolha uma opção: ')
    print()
    return opcao
def adicionar_contato(agenda, usuario, nome, telefone, email):
    agenda[usuario] = [nome, telefone, email]
    salvar_agenda(agenda) 
def salvar_agenda(agenda):
    with open ('agenda.json', 'w') as f:
        return json.dump(agenda, f)    
def buscar_contato(agenda, usuario):
    print()
    print(f'== Detalhes do Contato ==')
    print(f'Nome: {agenda[usuario][0]}')
    print(f'Telefone: {agenda[usuario][1]}')
    print(f'Email: {agenda[usuario][2]}')
    print()
def editar_agenda(agenda , usuario , campo , novo_valor):
    usuarios_adicionados()
    if campo == '1':
        nome = novo_valor
        if verificacao_nome(nome):
            agenda[usuario][0] = novo_valor
            print('Nome modificado com sucesso!')
    elif campo == '2':
        telefone = novo_valor
        if verificacao_telefone(telefone):
            agenda[usuario][1] = telefone
            print('Telefone modificado com sucesso!')
        else:
            print('Telefone inválido')
    elif campo == '3':
        email = novo_valor.lower()
        if verificacao_email(email):
            agenda[usuario][2] = telefone
            print('Email modificado com sucesso!')
        else:
            print('Email inválido')

def menu_editar():
    titulo = " EDITAR "
    largura = 36
    print('+' + '-' * (largura - 2) + '+')
    print(f'| {titulo:^32} |')
    print('+' + '-' * (largura - 2) + '+')
    print(f'| {"Qual campo você deseja editar?" :<32} |')
    print(f'| {"1. Alterar nome" :<32} |')
    print(f'| {"2. Alterar telefone" :<32} |')
    print(f'| {"3. Alterar email" :<32} |')
    print(f'| {"4. sair" :<32} |')
    print('+' + '-' * (largura - 2) + '+')
    campo = input('>> opção: ')
    return campo

def verificacao_email(email):
        proibidos_no_email = """()<>[];:,/"'`´~=+*&%$#!{ }|?^çáãâàéêèóòõôíìîúùû§¬¢£°ª\ """
        cont_arroba = email.count('@') #conta quantos '@' o usuário escreveu na variável 'email'
        verificacao = False
        verificacao_proibidos = False
        for caracter in proibidos_no_email:
            if caracter in email: # se um caractere proibido estiver no email que o usuário digitou
                verificacao_proibidos = True
                break
        if cont_arroba == 1 and verificacao_proibidos == False: # se o email tiver so um '@' e não tiver nenhum caractere  proibido
            pontos_seguidos = 0 # variável para ajudar na verificação
            for i in range(len(email)+1):
                if i == len(email)-1: # condição para o codigo não quebar
                    break
                if email[i] == email[i+1] and email[i] == '.': # se uma string em uma pocição for igual ao do lado, e a string verificada for um ponto
                    pontos_seguidos += 1 
                                    
            posicao_arroba = email.index('@') # posição de onde está o '@'
            sub_email_antes_do_arroba = email[:posicao_arroba] # sub_email, do começo até antes do "@"
            
            verificacao_email = True
            if len(sub_email_antes_do_arroba) >= 3:
                if sub_email_antes_do_arroba[-2] == '.' and sub_email_antes_do_arroba[-1] == '-' or sub_email_antes_do_arroba[-1] == '_' and sub_email_antes_do_arroba[-2] == '.':
                    verificacao_email = False
            email_invertido = email[::-1]
            if '.' in email_invertido:
                posicao_ponto = email_invertido.index('.')
                verificacao_numero = True
                for i in email_invertido[:posicao_ponto]: # verificar se tem número na extensão
                    if i in '1234567890':
                        verificacao_numero = False
                        break
            if email_invertido[posicao_ponto+1] != '-' and email_invertido[posicao_ponto-1] != '-' and verificacao_numero == True:
                if verificacao_email == True and email[0] != '@' and email[0] != '.' and email[-1] != '@' and email[-1] != '.' and pontos_seguidos == 0 and email[posicao_arroba-1] != '.' and email[posicao_arroba+1] != '.' and email[posicao_arroba+1] != '-' and email[posicao_arroba-1] != '-'and '_' not in email[posicao_arroba:]: # se não começar com "@" nem "." e não terminar com "@" nem "." e não tiver pontos seguidos e antes e dps do arroba não for um "." e se não tem "" depois do "@"
                    if email[0] != "-" and email[0] != "_" and email[-1] != "-" and email[-1] != "_":
                        if len(email[posicao_arroba:]) >= 4: # se o tamanho da 'sub_string' começando de onde está o '@' for maior que 4
                            sub_email = email[posicao_arroba:]
                            if '.' in sub_email: # se tiver '.' no "sub_email"
                                if '.' not in sub_email[-2:]: # se um '.' não estiver nem na penúltima e nem última posição 
                                    verificacao = True
                                            
        return verificacao
def verificacao_nome(nome):
    verificacao_nome = False
    for i in range(len(nome)):
        if nome[i] in '0123456789':
                break
        else:
            if i == len(nome)-1:
                verificacao_nome = True
    return verificacao_nome
def verificacao_telefone(telefone):
    bolean = False
    if len(telefone) == 10:
        contagem = 0
        for numero in telefone:
            if telefone[5] == '-':
                if numero in '0123456789':
                    contagem += 1
                    if contagem == 9:
                        bolean = True
                continue
    return bolean
def remover_contato(usuario):
    del agenda[usuario]
    salvar_agenda(agenda)
    print(f'Usuario "{usuario}" removido com sucesso!')
def usuarios_adicionados():
    lista_usuario = []
    maior = 'a'
    # Descobrindo o nome de usuário com maior comprimento
    for usuario in agenda.keys():
        if len(usuario) > len(maior):
            maior = usuario 
        lista_usuario.append(usuario)
    mensagem = "USUÁRIOS ADICIONADOS"
    if len(mensagem) > len(maior):
        maior = mensagem
    
    largura = len(maior) + 6 # margem extra pros espaços
    # Título
    print('+' + '-' * largura + '+')
    print(f'|{mensagem:^{largura}}|')
    print('+' + '-' * largura + '+')
    # Listagem dos usuários
    for nome in lista_usuario:
        print(f'| {nome:<{largura-2}} |')

    print('+' + '-' * largura + '+')
agenda = carregar_agenda()
while True:
    escolha = menu()
    if escolha == '1':
        usuario = input('>> Qual o nome do usuário (Utilize @ no começo. Ex: @gaguin)? ').lower()
        bolean = False
        if len(usuario) <= 1:
            print('Escreva algo para continuar')
        elif usuario[0] == '@':
            if usuario in agenda:
                print('Usuário existente.')
            else:
                nome = input('>> Digite o nome do contato: ').title().strip()
                if verificacao_nome(nome):
                    telefone = input('>> Qual o seu número de Telefone (Lembre-se de colocar o hífen. ex: xxxxx-xxxx)? ').strip()
                    if verificacao_telefone(telefone):
                        email = input('>> Email: ').lower().strip() 
                        if verificacao_email(email):
                            adicionar_contato(agenda, usuario, nome, telefone, email)
                            print(f'Contado adiconado!')
                        else:
                            print('email inválido!')
                    else:
                        print('telefone inválido!')
                else:
                    print('Nome inválido!')
        else:
            print('Por favor, comece o nome do usuário com @')
    elif escolha == '2':
        if len(agenda) == 0:
            print('Agenda vazia, adicione antes de buscar contatos')
        else:
            usuarios_adicionados()
            usuario = input('>> Qual o nome do usuario? ').lower()
            if usuario in agenda.keys():
                buscar_contato(agenda, usuario)
            else:
                print(f'Usuário "{usuario}" não encontrado!')              
    elif escolha == '3':
        if len(agenda) == 0:
            print('Agenda vazia, adicione antes de buscar contatos')
        else:
            usuarios_adicionados()
            usuario = input('>> Qual o nome do usuario? ').lower()
            if usuario in agenda.keys():
                buscar_contato(agenda, usuario)
                campo = menu_editar()
                if campo == '1' or campo == '2' or campo == '3':
                    novo_valor = input('>> Qual o novo valor que deseja adicionar? ').strip().title()
                    editar_agenda(agenda, usuario, campo, novo_valor)
                elif campo == '4':
                    print('Até mais!')
                else:
                    print('Opção incorreta!')
            else:
                print(f'Usuário: {usuario} não encontrado!')
    elif escolha == '4':
        if len(agenda) == 0:
            print('Agenda vazia, adicione antes de buscar contatos')
        else:
            usuarios_adicionados()
            usuario_remover = input('>> Qual usuário você deseja remover? ')
            if usuario_remover in agenda.keys():
                remover_contato(usuario_remover)
            else:
                print(f'Usuário "{usuario_remover}"não encontrado!')
    elif escolha == '5':
        print('Programa encerrando em 3, 2, 1...')
        print('programa encerrado!')
        break
    else:
        print('Opção inválida!')