import heapq
import sys

filaPacientes = []


def exibirMenu():
    print('MENU:')
    print('1- Cadastrar paciente')
    print('2 - Atender paciente')
    print('3- Mostrar fila de pacientes')
    print('4- Sair')

    acao = int(input('Digite o número da ação que dejesa fazer:'))

    match acao:  #switch-case
        case 1: 
            cadastrarPaciente()
        case 2:
            atenderPaciente()
        case 3: 
            exibirFilaPacientes()
        case 4: 
            sys.exit() # Fecha o programa 




def cadastrarPaciente():
    print("Preencha o cadastro do paciente abaixo!")
    nome = input('Nome:')
    prioridade = int(input('Prioridade (1- emergencia, 2- urgente, 3- pouco urgente, 4- não urgente):'))
    idade = int(input('Idade:'))

    #crio uma tupla de dados e insiro na heap 
    #o heap ordena a prioridade pelo 1º elemento da tupla, caso o 1º de empate, ele pula para o 2º e assim vai
    heapq.heappush(filaPacientes, (prioridade, -idade, nome))

    exibirMenu()





def  atenderPaciente():
    print('atender')

    if(filaPacientes):
        paciente1 = heapq.heappop(filaPacientes)
        print(f"Paciente {paciente1[2]} se direcione para o atendimento")

    exibirMenu()


def exibirFilaPacientes():
    print('FILA:')
    # exibe todos os pacientes em ordem real de prioridade
    #o heapq.nsmallest(parm1, parm2) é nativo da biblioteca, onde o parm1 é a qtd de items da fila que quero que percorra e o parm2 é a fila, o heap que ele vai percorrer
    for p in heapq.nsmallest(len(filaPacientes), filaPacientes):
        print(f"Prioridade: {p[0]} - Idade: {-p[1]} - Nome: {p[2]}")


    exibirMenu()




exibirMenu()


 