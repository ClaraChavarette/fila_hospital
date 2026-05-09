import heapq
import sys
import logging

filaPacientes = []


# configura o arquivo, o nível de log e o formato da mensagem
logging.basicConfig(
    filename='registro-atendimentos.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)



def exibirMenu():
    print('\n' + '='*30) #linha separadora
    print('      MENU HOSPITAL')
    print('='*30) #linha separadora

    print('1- Cadastrar paciente')
    print('2 - Atender paciente')
    print('3- Mostrar fila de pacientes')
    print('4- Sair')

    acao = int(input('Digite o número da ação que dejesa fazer: '))

    match acao:  #switch-case
        case 1: 
            cadastrarPaciente()
        case 2:
            atenderPaciente()
        case 3: 
            exibirFilaPacientes()
        case 4: 
            logging.info("Atendimento finalizado.") # Registra log 

            print('\n' + '-'*30) #linha separadora
            print('   ATENDIMENTO FINALIZADO')
            print('-'*30) #linha separadora
            sys.exit() # Fecha o programa 

            



def cadastrarPaciente():
    print('\n' + '-'*30) #linha separadora
    print('      CADASTRO')
    print('-'*30) #linha separadora

    nome = input('Nome: ')
    prioridade = int(input('Prioridade (1- emergencia, 2- urgente, 3- pouco urgente, 4- não urgente): '))
    idade = int(input('Idade: '))

    #crio uma tupla de dados e insiro na heap 
    #o heap ordena a prioridade pelo 1º elemento da tupla, caso o 1º de empate, ele pula para o 2º e assim vai
    heapq.heappush(filaPacientes, (prioridade, -idade, nome))

    logging.info(f"Paciente cadastrado {(prioridade, -idade, nome)}.") # Registra log 
    exibirMenu()





def  atenderPaciente():
    print('\n' + '-'*30) #linha separadora
    print('      ATENDIMENTO')
    print('-'*30) #linha separadora

    if filaPacientes:
        paciente1 = heapq.heappop(filaPacientes)

        print(f"Chamando: {paciente1[2].upper()}")
        print(f"Prioridade: {paciente1[0]} | Idade: {-paciente1[1]}")

        logging.info(f"Paciente atendido - {paciente1[2]}, {paciente1[0]}, {paciente1[1]}.") # Registra log     
    else:
        print(f"A fila está vazia no momento.")
        logging.info(f"fila está vazia no momento.\n") # Registra log 

    exibirMenu()


def exibirFilaPacientes():
    print('\n' + '-'*30) #linha separadora
    print('      FILA')
    print('-'*30) #linha separadora

    # exibe todos os pacientes em ordem real de prioridade
    #o heapq.nsmallest(parm1, parm2) é nativo da biblioteca, onde o parm1 é a qtd de items da fila que quero que percorra e o parm2 é a fila, o heap que ele vai percorrer
    for p in heapq.nsmallest(len(filaPacientes), filaPacientes):
        print(f"Prioridade: {p[0]} - Idade: {-p[1]} - Nome: {p[2]}")
        logging.info(f"Fila - Prioridade: {p[0]} - Idade: {-p[1]} - Nome: {p[2]}") # Registra log 

   # logging.info(f"Fila: {len(filaPacientes)} pacientes aguardando.") # Registra log       
    exibirMenu()




exibirMenu()


 