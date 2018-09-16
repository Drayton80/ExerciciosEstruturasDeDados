# Essa função serve para passar como parâmetro para a função sorted
# com objetivo de, assim, tal função saber o que será ordenado dentre
# os processos
def process_sort_time_arrival(process):
	return process.time_arrival

def fcfs(process_list):
	# Aqui é ordenado a lista baseado na ordem de quem chegou primeiro na fila
	process_list = sorted(process_list, key=process_sort_time_arrival)

	time = 0
	total_time = 0
	most_priority_process = 0

	'''
	for process in process_list:
		print("ID do Processo:", process.number)
		process.show_info()
		print("\n\n")
	'''
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
			# Se o processo não está em execução e seu tempo restante é maior que 0, ou seja,
			# ele ainda não terminou:
			if(process_list[i].running == False and process_list[i].time_remaining > 0):
				# Seu tempo na fila de espera é aumentado
				process_list[i].time_waiting += 1

			# Se o processo está executando:
			if(process_list[i].running == True):
				# Seu tempo restante é decrementado:
				process_list[i].time_remaining -= 1

		time += 1