# Sistema de fila com prioridade utilizando heap em Python

## O que é o heap e como ele funciona:
Neste projto utilizo a bibloteca ```heapq```, que implementa uma estrutura de dados chamada Min-Heap. Abaixo esplico o funcionamento por trás desta biblioteca:

 O algoritmo de heap organiza os dados de forma que o elemento de menos valor(ou maior prioridade) esteja sempre no topo (na raiz), deixando o acesso mais rápido ao próximo item da fila. 


Ele utiliza a estrutura de uma árvore, então: 
- Quando utilizo ```heapq.heappush(...)``` ele insere o valor da esquerda para a direita e do menor para o maior (min-heap). Também pode ser adicionado do maior para o menor (max-heap), mas no caso da fila de hospital isso não é necessário. Quando insiro ele insere ao final da árvore e vai comparando para ordenar as prioridades corretamente. Complexidade: O(log n). 

- Quando utilizo o ```heapq.heappop(...)``` ele remove sempre o elemento do topo da árvore, o que tem mais prioridade de antendimento. Ao remover o último valor da esquerda é movido para o topo da árvore e ele vai comparando novamente os valores dos galhos da árvore, para ordena-la novamente e deixar no topo o valor com maior prioridade. Complexidade: O(log n). 



## Explicação do código:

Este código é um sistema para a fila de um hospital, onde antes de ser atendido você é classificado pelo nível de prioridade dos sintomas que tem. Podendo ser das seguintes categorias: 
- 1- Emergência
- 2- Urgente
- 3- Pouco urgente
- 4- Não urgente

Támbem é cadastrado sua idade, pois duas pessoas com o mesmo nível de prioridade o mais velho deve ser chamado primeiro. 

Para evitar que as pessoas da categoria "4 -não urgente" nunca sejam atendidos, (problema conhecido como starvation, onde um processo nunca consegue ser executado, pois sempre tem processos com mais prioridade que ele para serem executados), a cada 3 pessoas "Pouco urgente" uma pessoa "Não urgente" é chamada. 

## Funcionalidades: 
Este sistema possue as seguintes funcionalidades: 
- Cadastrar pacientes
- Inserir os pacientes na fila
- Atender pacientes
- Exibir a fila de paciente 
- Finalizar o programa 


## Intenção do projeto: 
Este projeto tem um intuito de priorizar os pacientes com estados de saúde mais graves (maior emergência), e ao mesmo tempo não deixa de lado os que não são tão urgentes, garantindo que todos sejam atendidos de forma segura e rápida. 


