import matplotlib.pyplot as plt
import pandas as pd
import time
import original
import optimized


def save_iterations_in_file(data_frame, file_name, initial_size, jump_size, number_of_iterations):
	original_durations = []
	optimized_durations = []
	data_frame_sizes = []

	for actual_size in range(initial_size, initial_size+jump_size*number_of_iterations, jump_size):
		data_frame_sizes.append(actual_size)

		subset_data_frame = pd.DataFrame(data_frame.loc[0:actual_size])
		
		start = time.time()
		original.preprocess_data(subset_data_frame)
		end = time.time()

		original_durations.append(end - start)

	for actual_size in range(initial_size, initial_size+jump_size*number_of_iterations, jump_size):
		subset_data_frame = pd.DataFrame(data_frame.loc[0:actual_size])
		
		start = time.time()
		optimized.preprocess_data(subset_data_frame)
		end = time.time()

		optimized_durations.append(end - start)

	# Abrindo (ou criando, caso não exista) um 
	# arquivo em modo de inserção no fim (append):
	with open("{0}.txt".format(file_name),'a') as file:
		for i in range(len(original_durations)):
			line = str(data_frame_sizes[i]) + ' ' + str(original_durations[i])   + ' ' + str(optimized_durations[i]) + '\n'
			file.write(line)


def plot_iterations(file_name):
	original_durations = []
	optimized_durations = []
	data_frame_sizes = []

	# Abrindo um arquivo em modo de leitura:
	with open("{0}.txt".format(file_name),'r') as file:
		each_file_line = file.read().splitlines()

		for line in each_file_line:
			# Separa cada linha em uma lista com
			# cada um dos três dados que cada uma contém
			data = line.split(' ')

			data_frame_sizes.append(float(data[0]))
			original_durations.append(float(data[1]))
			optimized_durations.append(float(data[2]))

	# Monta o gráfico com as listas obtidas:
	#plt.plot(data_frame_sizes, original_durations , 'c',
    #         data_frame_sizes, optimized_durations, 'm')
	plt.plot(data_frame_sizes, original_durations, color="b", label="Original")
	plt.plot(data_frame_sizes, optimized_durations, color="c",  label="Otimizado")
	plt.legend(loc='upper left', frameon=False)
	plt.ylabel('Tempo (s)')
	plt.xlabel('Número de Instâncias')
	# Exibe o gráfico na tela:
	plt.show()


def plot_percentage(file_name):
	percentage_gain = []
	data_frame_sizes = []

	# Abrindo um arquivo em modo de leitura:
	with open("{0}.txt".format(file_name),'r') as file:
		each_file_line = file.read().splitlines()

		for line in each_file_line:
			# Separa cada linha em uma lista com
			# cada um dos três dados que cada uma contém
			data = line.split(' ')

			data_frame_sizes.append(float(data[0]))
			original_duration = float(data[1])
			optimized_duration = float(data[2])

			difference = original_duration - optimized_duration

			percentage_gain.append((difference*100)/original_duration)

	# Monta o gráfico com as listas obtidas:
	#plt.plot(data_frame_sizes, original_durations , 'c',
    #         data_frame_sizes, optimized_durations, 'm')
	plt.plot(data_frame_sizes, percentage_gain, color="m", label="Original")
	plt.legend(loc='upper left', frameon=False)
	plt.ylabel('Porcentagem')
	plt.xlabel('Número de Instâncias')
	plt.ylim(0, 100)
	# Exibe o gráfico na tela:
	plt.show()


# MAIN:
data_frame = pd.read_csv("ks-projects-201801.csv")
file_name  = 'iterations_total_optimized'

#save_iterations_in_file(data_frame, file_name, 18000, 2000, 2)
#plot_iterations(file_name)
plot_percentage(file_name)
