import matplotlib.pyplot as plt

def extract_file_column(file_name, column_index):
	column_values = [] 

	# Abrindo um arquivo em modo de leitura:
	with open("{0}.txt".format(file_name),'r') as file:
		all_file_lines = file.read().splitlines()

		for each_line in all_file_lines:
			# Separa cada linha em uma lista com
			# cada um dos três dados que cada uma contém
			data = each_line.split(' ')

			column_values.append(float(data[column_index]))

	return column_values


def extract_file_line(file_name, line_index):
	column_values = [] 

	# Abrindo um arquivo em modo de leitura:
	with open("{0}.txt".format(file_name),'r') as file:
		all_file_lines = file.read().splitlines()

		line_values = all_file_lines[line_index].split(' ')

	return line_values


def comparison_technics(number_of_threads):
	data_sizes = extract_file_column("recorded durations/{}threads_times_original".format(number_of_threads), 0)
	original_durations = extract_file_column("recorded durations/{}threads_times_original".format(number_of_threads), 1)
	optimized_durations = extract_file_column("recorded durations/{}threads_times_optimized".format(number_of_threads), 1)
	parallelized_durations = extract_file_column("recorded durations/{}threads_times_parallelized".format(number_of_threads), 1)
	optimized_and_parallelized_durations = extract_file_column("recorded durations/{}threads_times_optimized_and_parallelized".format(number_of_threads), 1)

	# Monta o gráfico com as listas obtidas:
	plt.plot(data_sizes, original_durations, color="m", label="Original", linewidth=2.0)
	plt.plot(data_sizes, optimized_durations, color="b",  label="Otimizado", linewidth=2.0)
	plt.plot(data_sizes, parallelized_durations, color="c", label="Paralelizado", linewidth=2.0)
	plt.plot(data_sizes, optimized_and_parallelized_durations, color="g",  label="Paralelizado e Otimizado", linewidth=2.0)
	plt.legend(loc='upper left', frameon=False)
	plt.xlabel('Tamanho dos Dados')
	plt.ylabel('Tempo (s)')
	plt.xlim(100, 1400)
	plt.ylim(0, 0.2)
	plt.title("Gráfico de Tempo de Execução por Técnica Aplicada no código ({} Threads)".format(number_of_threads))
	
	# Exibe o gráfico na tela:
	plt.show()

def speedup(line_index):
	data_size = extract_file_line("recorded durations/4threads_times_original", line_index)[0]

	t2_original_duration = extract_file_line("recorded durations/2threads_times_original", line_index)[1]
	t2_optimized_duration = extract_file_line("recorded durations/2threads_times_optimized", line_index)[1]
	t2_parallelized_duration = extract_file_line("recorded durations/2threads_times_parallelized", line_index)[1]
	t2_optimized_and_parallelized_duration = extract_file_line("recorded durations/2threads_times_optimized_and_parallelized", line_index)[1]

	t4_original_duration = extract_file_line("recorded durations/4threads_times_original", line_index)[1]
	t4_optimized_duration = extract_file_line("recorded durations/4threads_times_optimized", line_index)[1]
	t4_parallelized_duration = extract_file_line("recorded durations/4threads_times_parallelized", line_index)[1]
	t4_optimized_and_parallelized_duration = extract_file_line("recorded durations/4threads_times_optimized_and_parallelized", line_index)[1]

	t8_original_duration = extract_file_line("recorded durations/8threads_times_original", line_index)[1]
	t8_optimized_duration = extract_file_line("recorded durations/8threads_times_optimized", line_index)[1]
	t8_parallelized_duration = extract_file_line("recorded durations/8threads_times_parallelized", line_index)[1]
	t8_optimized_and_parallelized_duration = extract_file_line("recorded durations/8threads_times_optimized_and_parallelized", line_index)[1]

	t16_original_duration = extract_file_line("recorded durations/16threads_times_original", line_index)[1]
	t16_optimized_duration = extract_file_line("recorded durations/16threads_times_optimized", line_index)[1]
	t16_parallelized_duration = extract_file_line("recorded durations/16threads_times_parallelized", line_index)[1]
	t16_optimized_and_parallelized_duration = extract_file_line("recorded durations/16threads_times_optimized_and_parallelized", line_index)[1]

	speedup_between_original_and_parallel = [float(t2_original_duration) /float(t2_parallelized_duration) ,
                                             float(t4_original_duration) /float(t4_parallelized_duration) ,
                                             float(t8_original_duration) /float(t8_parallelized_duration) ,
                                             float(t16_original_duration)/float(t16_parallelized_duration)]
	
	speedup_between_optimizeds = [float(t2_optimized_duration) /float(t2_optimized_and_parallelized_duration) ,
                                  float(t4_optimized_duration) /float(t4_optimized_and_parallelized_duration) ,
                                  float(t8_optimized_duration) /float(t8_optimized_and_parallelized_duration) ,
                                  float(t16_optimized_duration)/float(t16_optimized_and_parallelized_duration)]



	# Monta o gráfico com as listas obtidas:
	plt.plot([2, 4, 8, 16], speedup_between_original_and_parallel, color="b",  label="Original e Paralelizado", linewidth=2.0)
	plt.plot([2, 4, 8, 16], speedup_between_optimizeds, color="c", label="Otimizado Original e Paralelizado", linewidth=2.0)
	plt.legend(loc='upper left', frameon=False)
	plt.xlabel('Número de Threads')
	plt.ylabel('Speedup')
	plt.xlim(2, 16)
	plt.ylim(1, 3)
	plt.title("Gráfico do ganho de Speedup (Tamanho do Array igual a {0}x{0})".format(str(data_size)))
	
	# Exibe o gráfico na tela:
	plt.show()