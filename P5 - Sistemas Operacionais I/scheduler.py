from process import Process

# Essa função serve para passar como parâmetro para a função sorted
# com objetivo de, assim, tal função saber o que será ordenado dentre
# os processos
def process_sort_time_arrival(process):
	return process.time_arrival


# Essa função serve para passar como parâmetro para a função sorted
# com objetivo de, assim, tal função saber o que será ordenado dentre
# os processos
def process_sort_time_remaining(process):
	return process.time_remaining


def fcfs(process_list):
	# Aqui é ordenado a lista baseado na ordem de quem chegou primeiro na fila
	process_list = sorted(process_list, key=process_sort_time_arrival)

	time = 0
	total_time = 0
	most_priority_process = 0

	# Obtém-se o tempo total baseado em todos os tempos de execução fornecidos:
	for process in process_list:
		total_time += process.time_remaining

	while(time <= total_time):
		# Aqui é definido qual processo será executado:
		if(process_list[most_priority_process].time_remaining > 0):
			# Se o processo de maior prioridade ainda tiver tempo de execução restante,
			# ele deve ser executado:
			process_list[most_priority_process].running = True

			# O tempo de inicio da execução só é -1 quando o processo ainda não executou pela
			# primeira vez:
			if(process_list[most_priority_process].time_start == -1):
				process_list[most_priority_process].time_start = time
		else:
			# Caso contrário ele para de executar e salva o tempo em que finalizou sua execução
			process_list[most_priority_process].running  = False
			process_list[most_priority_process].time_end = time

			# A prioridade passa para o próximo elemento da fila:
			most_priority_process += 1

			# Apenas acessa o próximo elemento se ainda não chegou no ultimo elemento:
			if(most_priority_process < len(process_list)):
				# O elemento de maior prioridade começa a executar e é salvo seu tempo de inicio:
				process_list[most_priority_process].running = True
				process_list[most_priority_process].time_start = time
		

		# Percorre-se todos os elementos da lista:
		for i in range(len(process_list)):
			# Se o processo não está em execução, seu tempo de chegada na fila é menor ou igual ao 
			# tempo atual (ou seja, ele já chegou na fila) e seu tempo restante é maior que 0, 
			# ou seja, ele ainda não terminou:
			if(process_list[i].running == False and process_list[i].time_remaining > 0 and
			   process_list[i].time_arrival <= time):
				# Seu tempo na fila de espera é aumentado
				process_list[i].time_waiting += 1

			# Se o processo está executando:
			if(process_list[i].running == True):
				# Seu tempo restante é decrementado:
				process_list[i].time_remaining -= 1

		time += 1


def sjf(process_list):
	process_complete_list = []
	queue = []
	cpu = []
	total_time = 0
	time = 0

	# Obtém-se o tempo total baseado em todos os tempos de execução fornecidos:
	for process in process_list:
		total_time += process.time_remaining

	while(True):
		# Aqui é checado se há algum processo que está no tempo exato de chegar na fila,
		# ou seja, se seu tempo de chegada é igual ao tempo atual
		for i in range(len(process_list)):
			if(process_list[i].time_arrival == time):
				queue.append(Process(process_list[i].number, process_list[i].time_arrival, 
					                 process_list[i].time_start, process_list[i].time_end, 
					                 process_list[i].time_remaining, process_list[i].time_waiting, 
					                 process_list[i].running))

				# A cada vez que um novo processo chega é preciso reordenar a fila
				# para colocar ele na posição correta baseado na sua prioridade de
				# execução:
				queue = sorted(queue, key=process_sort_time_remaining)

		# Aqui é colocado um processo na CPU caso ela esteja vazia e a fila possua algum
		# elemento. Isso serve tanto no inicio da execução quanto quando há espaços vazios
		# de execução entre processos (um processo termina e o outro apenas executa n unidades
		# de tempo depois, deixando a CPU ociosa):
		if(len(cpu) == 0 and len(queue) != 0):
			cpu.append(queue.pop(0))
			cpu[0].running = True
			# O tempo de inicio do processo apenas é -1 quando ele ainda não entrou na CPU
			if(cpu[0].time_start == -1):
				cpu[0].time_start = time

		# Aqui é definido quando o processo sairá da fila:
		if(cpu[0].time_remaining == 0):
			# É salvo o tempo do processo que finalizou:
			cpu[0].time_end = time
			# e ele é retirado da CPU e salvo na lista de processos que já
			# completaram a sua execução:
			process_complete_list.append(cpu.pop())

			# Automaticamente o próximo processo na fila é adicionado na CPU,
			# se não há processos na fila a CPU ficará ociosa
			if(len(queue) != 0):
				cpu.append(queue.pop(0))
				cpu[0].running = True
				# O tempo de inicio do processo apenas é -1 quando ele ainda não entrou na CPU
				if(cpu[0].time_start == -1):
					cpu[0].time_start = time	

		# Se houver algum processo na CPU, seu tempo de execução deve decrementar:
		if(len(cpu) != 0):
			cpu[0].time_remaining -= 1

		# Todos os processos fora da CPU que estiverem na fila de espera aumentam
		# o tempo que define o quanto eles esperaram em espera:
		for i in range(len(queue)):
			queue[i].time_waiting += 1

		# A lista de processos que completaram apenas fica com o tamanho igual a
		# lista de processos quando todos os processos terminaram de executar
		if(len(process_complete_list) == len(process_list)):
			return process_complete_list 

		time += 1


def rr(process_list):
	process_complete_list = []
	queue = []
	cpu = []
	total_time = 0
	quantum = 2
	time = 0

	# Obtém-se o tempo total baseado em todos os tempos de execução fornecidos:
	for process in process_list:
		total_time += process.time_remaining

	while(True):
		# Aqui é checado se há algum processo que está no tempo exato de chegar na fila,
		# ou seja, se seu tempo de chegada é igual ao tempo atual
		for i in range(len(process_list)):
			if(process_list[i].time_arrival == time):
				# Não é preciso sequer ordenar a fila de espera, pois cada processo é colocado
				# no fim dela conforme chega já garantindo que o primeiro a chegar será o primeiro
				# a ser executado
				queue.append(Process(process_list[i].number, process_list[i].time_arrival, 
					                 process_list[i].time_start, process_list[i].time_end, 
					                 process_list[i].time_remaining, process_list[i].time_waiting, 
					                 process_list[i].running))

		# Aqui é colocado um processo na CPU caso ela esteja vazia e a fila possua algum
		# elemento. Isso serve tanto no inicio da execução quanto quando há espaços vazios
		# de execução entre processos (um processo termina e o outro apenas executa n unidades
		# de tempo depois, deixando a CPU ociosa):
		if(len(cpu) == 0 and len(queue) != 0):
			cpu.append(queue.pop(0))
			cpu[0].running = True
			# O tempo de inicio do processo apenas é -1 quando ele ainda não entrou na CPU
			if(cpu[0].time_start != -1):
				cpu[0].time_start = time

		# Quando o quantum termina e o tempo de execução do processo na cpu for
		# diferente de zero, tal processo é retirado na CPU e colocado no final
		# da fila de espera
		if(quantum == 0 and cpu[0].time_remaining != 0):
			# O contador do quantum é reiniciado:
			quantum = 2
			# Tira o processo da CPU e coloca-o na fila de espera:
			queue.append(cpu.pop())

			# Automaticamente o próximo processo na fila é adicionado na CPU,
			# se não há processos na fila a CPU ficará ociosa
			if(len(queue) != 0):
				cpu.append(queue.pop(0))
				cpu[0].running = True
				# O tempo de inicio do processo apenas é -1 quando ele ainda não entrou na CPU
				if(cpu[0].time_start == -1):
					cpu[0].time_start = time

		# Aqui é definido quando o processo sairá da fila:
		if(cpu[0].time_remaining == 0):
			# O contador do quantum é reiniciado:
			quantum = 2
			# Salva-se o tempo do processo que finalizou:
			cpu[0].time_end = time
			# e ele é retirado da CPU e salvo na lista de processos que já
			# completaram a sua execução:
			process_complete_list.append(cpu.pop())

			# Automaticamente o próximo processo na fila é adicionado na CPU,
			# se não há processos na fila a CPU ficará ociosa
			if(len(queue) != 0):
				cpu.append(queue.pop(0))
				cpu[0].running = True
				# O tempo de inicio do processo apenas é -1 quando ele ainda não entrou na CPU
				if(cpu[0].time_start == -1):
					cpu[0].time_start = time	

		# Se houver algum processo na CPU, seu tempo de execução deve decrementar:
		if(len(cpu) != 0):
			cpu[0].time_remaining -= 1
			quantum -= 1

		# Todos os processos fora da CPU que estiverem na fila de espera aumentam
		# o tempo que define o quanto eles esperaram em espera:
		for i in range(len(queue)):
			queue[i].time_waiting += 1

		# A lista de processos que completaram apenas fica com o tamanho igual a
		# lista de processos quando todos os processos terminaram de executar
		if(len(process_complete_list) == len(process_list)):
			return process_complete_list 

		time += 1



