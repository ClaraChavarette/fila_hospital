import heapq
import sys
import logging

filaPacientes = []
contadorPoucoUrgente = 0

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
            atenderPaciente(0)
        case 3: 
            exibirFilaPacientes()
        case 4: 
            logging.info("Atendimento finalizado./n") # Registra log 

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





def  atenderPaciente(prioridadePassada):
    global contadorPoucoUrgente # Permite alterar a variável lá de fora

    print('\n' + '-'*30) #linha separadora
    print('      ATENDIMENTO')
    print('-'*30) #linha separadora

    if not filaPacientes:
        print(f"A fila está vazia no momento.")
        logging.info(f"fila está vazia no momento.") # Registra log 
        exibirMenu()
        return

    paciente_atendido = None
  
    if contadorPoucoUrgente >= 3:   # após 3 atendimentos "Pouco Urgente", tenta prioridade 4

        indice_nao_urgente = -1
        for i in range(len(filaPacientes)):
            if filaPacientes[i][0] == 4:
                indice_nao_urgente = i
                break
        
        if indice_nao_urgente != -1:
            paciente_atendido = filaPacientes.pop(indice_nao_urgente) # Remove o paciente não urgente encontrado
            heapq.heapify(filaPacientes) # Reorganiza
            contadorPoucoUrgente = 0 # Reseta o contador
            print(">>> Atendimento Especial (Não Urgente após 3 Pouco Urgentes)")
        else:
            paciente_atendido = heapq.heappop(filaPacientes) #se não tiver prioridade 4, segue fila normal
    else:
        paciente_atendido = heapq.heappop(filaPacientes) #atende normal, prioridade

    print(f"Chamando: {paciente_atendido[2].upper()}")
    print(f"Prioridade: {paciente_atendido[0]} | Idade: {-paciente_atendido[1]}")
    logging.info(f"Paciente atendido - {paciente_atendido}")
    #logging.info(f"Paciente atendido - {pacienteEspecf[2]}, {pacienteEspecf[0]}, {pacienteEspecf[1]}.") # Registra log   

    
    if paciente_atendido[0] == 3:
        contadorPoucoUrgente += 1
    print(f"(Status do contador de 'Pouco Urgentes': {contadorPoucoUrgente})")

    exibirMenu()

    



def exibirFilaPacientes():
    print('\n' + '-'*30) #linha separadora
    print('      FILA')
    print('-'*30) #linha separadora

    if not filaPacientes:
        print(f"A fila está vazia no momento.")
        logging.info(f"Fila está vazia no momento.") # Registra log 
        exibirMenu()
        return

    # exibe todos os pacientes em ordem real de prioridade
    #o heapq.nsmallest(parm1, parm2) é nativo da biblioteca, onde o parm1 é a qtd de items da fila que quero que percorra e o parm2 é a fila, o heap que ele vai percorrer
    for p in heapq.nsmallest(len(filaPacientes), filaPacientes):
        print(f"Prioridade: {p[0]} - Idade: {-p[1]} - Nome: {p[2]}")
        logging.info(f"Fila - Prioridade: {p[0]} - Idade: {-p[1]} - Nome: {p[2]}") # Registra log 

   # logging.info(f"Fila: {len(filaPacientes)} pacientes aguardando.") # Registra log       
    exibirMenu()





exibirMenu()


 