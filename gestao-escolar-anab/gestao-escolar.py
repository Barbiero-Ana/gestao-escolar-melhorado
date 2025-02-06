from datetime import datetime

def process_dados():
    alunos = []
    try:
        with open('alunos.txt', 'r') as arquivo:
            for linha in arquivo:
                nome, matricula, birth, notas, faltas = linha.strip().split(';')
                alunos.append({'nome' : nome, 'matricula' : matricula, 'data_nascimento' : birth, 'notas' : notas, 'faltas' : faltas})
    except FileNotFoundError:
        pass
    return alunos

def save_dados(alunos):
    with open('alunos.txt', 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno['nome']};{aluno['matricula']};{aluno['data_nascimento']};{aluno['notas']};{aluno['faltas']}\n")

def add_alun(alunos):
    nome = input('Digite o nome do(a) aluno(a): ')
    matricula = int(input('Digite o número de matrícula do(a) aluno(a): '))
    birth = input('Digite a data de nascimento do(a) aluno(a) (no formato DD/MM/AAAA): ')
    try:
        data = datetime.strptime(birth, '%d/%m/%Y')
        birth_format = data.strftime('%d-%m-%Y')
    except ValueError:
        print('Formato de data inválido... Por favor, tente novamente da forma indicada.')
        return
    notas = []
    qtd = int(input('Quantas notas deseja adicionar ao perfil do(a) aluno(a): '))
    for i in range(qtd):
        nota = float(input(f'Digite a {i+1}° nota: '))
        notas.append(nota)

    while True:
        try:
            faltas = int(input('Quantas faltas o(a) aluno(a) apresentou: '))
            break
        except ValueError:
            print('Valor inválido, tente novamente.')

    alunos.append({'nome': nome, 'matricula': matricula, 'data_nascimento': birth_format, 'notas': notas, 'faltas': faltas})
    save_dados(alunos)
    print('\nAluno(a) adicionado ao sistema.')

def list_al(alunos):
    if not alunos:
        print('Sem alunos registrados no sistema.')
    else:
        for aluno in alunos:
            print(f'Nome: {aluno["nome"]}\nMatrícula: {aluno["matricula"]}\nData de nascimento: {aluno["data_nascimento"]}\nNotas: {aluno["notas"]}\nFaltas: {aluno["faltas"]}')

def find_al(alunos):
    while True:
        try:
            filtro = int(input('Digite o número de matrícula do aluno'))
            break
        except ValueError:
            print('Valor não válido, tente novamente.')
    for aluno in alunos:
        if filtro == aluno['matricula']:
            print(f'Aluno(a) encontrado:\nNome: {aluno["nome"]}\nMatrícula: {aluno["matricula"]}\nData de nascimento: {aluno["data_nascimento"]}\nNotas: {aluno["notas"]}\nFaltas: {aluno["faltas"]}')
            return aluno
    print('\nAluno não encontrado...')
    return None

def modificar(alunos):
    aluno = find_al(alunos)
    if aluno:
        print(f'O que gostaria de alterar:\n1 - Nome\n2 - Matrícula\n3 - Data de nascimento\n4 - Notas\n5 - Faltas\n6 - Cancelar')
        opc = int(input('Digite o número da opção que deseja: '))
        if opc == 1:
            aluno['nome'] = input('Digite o novo nome: ')
        elif opc == 2:
            while True:
                try:
                    matricula = int(input('Digite o novo número de matrícula: '))
                    aluno['matricula'] = matricula
                    break
                except ValueError:
                    print('Valor inválido, tente novamente.')
        elif opc == 3:
            while True:
                birth = input('Digite a nova data de nascimento(no formato DD/MM/AAAA): ')
                try:
                    data = datetime.strptime(birth, '%d/%m/%Y')
                    aluno['data_nascimento'] = data.strftime('%d-%m-%Y')
                    break
                except ValueError:
                    print('Formato de data inválido, tente novamente.')
        elif opc == 4:
            try:
                qtd = int(input('Quantas notas deseja alterar: '))
                for i in range(qtd):
                    print(f"As notas atuais são: {aluno['notas']}")
                    new_nota = float(input(f'Digite a {i+1}° nova nota: '))
                    aluno['notas'].append(new_nota)
            except ValueError:
                print('Erro, valor de nota inválido.')
        elif opc == 5:
            while True:
                try:
                    faltas = int(input('Digite o novo número de faltas do(a) aluno(a): '))
                    aluno['faltas'] = faltas
                    break
                except ValueError:
                    print('Valor inválido, tente novamente.')
        elif opc == 6:
            print('Voltando ao menu inicial...')
            return
        else:
            print('Opção inválida, tente novamente.')
        save_dados(alunos)
        print('Dados atualizados.')

def excluir(alunos):
    aluno = find_al(alunos)
    if aluno:
        alunos.remove(aluno)
        save_dados(alunos)
        print('\nRemoção realizada.')

def organizar(alunos):
    filtro = input('- Organizar por nome\n- Organizar por número de matrícula\n- Organizar por data de nascimento\nDigite: "nome" ou "matricula" ou "data de nascimento": ')
    if filtro.lower() == 'nome':
        alunos.sort(key=lambda aluno: aluno['nome'])
    elif filtro.lower() == 'matricula':
        alunos.sort(key=lambda aluno: aluno['matricula'])
    elif filtro.lower() == 'data de nascimento':
        alunos.sort(key=lambda aluno: aluno['data_nascimento'])
    else:
        print('Opção inválida')
        return
    
    save_dados(alunos)
    print(f'Alunos ordenados por {filtro}')

def menu():
    alunos = process_dados()
    while True:
        print(f'{"=" * 50}')
        print('\nSISTEMA DE GESTÃO DE ALUNOS')
        print(f'{"=" * 50}')
        print('\n1 - Adicionar um novo aluno\n2 - Listar alunos já registrados\n3 - Buscar aluno\n4 - Editar dados de um aluno já cadastrado\n5 - Remover um aluno do sistema\n6 - Organizar lista de alunos\n0 - Sair do sistema')
        decisao = int(input('- '))
        if decisao == 1:
            add_alun(alunos)
        elif decisao == 2:
            list_al(alunos)
        elif decisao == 3:
            find_al(alunos)
        elif decisao == 4:
            modificar(alunos)
        elif decisao == 5:
            excluir(alunos)
        elif decisao == 6:
            organizar(alunos)
        elif decisao == 0:
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida, tente novamente.')

menu()
