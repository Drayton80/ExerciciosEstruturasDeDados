from process import Process
import scheduler

print("<MESSAGE: Certifique-se que o arquivo a ser lido esteja no formato txt e inserido no diretório inputs>")
file_name = input("  Informe o nome do arquivo que será executado: ")

process_list = []

with open('inputs/{0}.txt'.format(file_name), 'r') as file_text:
	# Separa o arquivo em linhas e salva elas em uma lista
	lines = file_text.read().splitlines()

	process_id = 1

	# Separa as linhas por espaço para obter os números relativos à cada processo
	for line in lines:
		# Separa cada linha em uma lista de números dela:
		line = line.split()

		# Obtém-se aqui os tempos de chegada e restante:
		time_arrival = int(line[0])
		time_remaining = int(line[1])

		# Cria uma lista de processos baseada nos elementos obtidos do arquivo de
		# entrada:
		process_list.append(Process(process_id, time_arrival, -1, -1, time_remaining, 0, False))

		process_id += 1


scheduler.fcfs(process_list)

for process in process_list:
	process.show_info()


