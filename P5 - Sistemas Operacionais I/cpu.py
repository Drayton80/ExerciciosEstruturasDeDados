from process import Process
import scheduler

print("<MESSAGE: Certifique-se que o arquivo a ser lido esteja no formato txt e inserido no diretório inputs>")
file_name = input("  Informe o nome do arquivo que será executado: ")

process_list_fcfs = []
process_list_sjf  = []
process_list_rr   = []

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
		process_list_fcfs.append(Process(process_id, time_arrival, -1, -1, time_remaining, 0, False))
		process_list_sjf.append(Process(process_id, time_arrival, -1, -1, time_remaining, 0, False))
		process_list_rr.append(Process(process_id, time_arrival, -1, -1, time_remaining, 0, False))

		process_id += 1

# ESCALONADOR DO TIPO FCFS:
scheduler.fcfs(process_list_fcfs)

number_of_process = len(process_list_fcfs)

sum_return_time   = 0
sum_response_time = 0
sum_waiting_time  = 0

for process in process_list_fcfs:
	process.show_info()
	sum_return_time   += process.get_return_time()
	sum_response_time += process.get_response_time()
	sum_waiting_time  += process.get_waiting_time()	

mean_return_time   = sum_return_time/number_of_process
mean_response_time = sum_response_time/number_of_process
mean_waiting_time  = sum_waiting_time/number_of_process

print("FCFS", "{0:0.1f}".format(mean_return_time), "{0:0.1f}".format(mean_response_time), "{0:0.1f}".format(mean_waiting_time))
print("\n\n")


# ESCALONADOR DO TIPO SJF:
for process in process_list_sjf:
	process.show_info()

process_list_sjf = scheduler.sjf(process_list_sjf)

number_of_process = len(process_list_sjf)

sum_return_time   = 0
sum_response_time = 0
sum_waiting_time  = 0

for process in process_list_sjf:
	process.show_info()
	sum_return_time   += process.get_return_time()
	sum_response_time += process.get_response_time()
	sum_waiting_time  += process.get_waiting_time()	

mean_return_time   = sum_return_time/number_of_process
mean_response_time = sum_response_time/number_of_process
mean_waiting_time  = sum_waiting_time/number_of_process

print("SJF", "{0:0.1f}".format(mean_return_time), "{0:0.1f}".format(mean_response_time), "{0:0.1f}".format(mean_waiting_time))
print("\n\n")



