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

data_sizes = extract_file_column("times_original", 0)
original_durations = extract_file_column("times_original", 1)
optimized_durations = extract_file_column("times_optimized", 1)
parallelized_durations = extract_file_column("times_parallelized", 1)
optimized_and_parallelized_durations = extract_file_column("times_optimized_and_parallelized", 1)

# Monta o gráfico com as listas obtidas:
#plt.plot(data_frame_sizes, original_durations , 'c',
#         data_frame_sizes, optimized_durations, 'm')
plt.plot(data_sizes, original_durations, color="m", label="Original", linewidth=2.0)
plt.plot(data_sizes, optimized_durations, color="b",  label="Otimizado", linewidth=2.0)
plt.plot(data_sizes, parallelized_durations, color="c", label="Paralelizado", linewidth=2.0)
plt.plot(data_sizes, optimized_and_parallelized_durations, color="g",  label="Paralelizado e Otimizado", linewidth=2.0)
plt.legend(loc='upper left', frameon=False)
plt.ylabel('Tempo (s)')
plt.xlabel('Tamanho dos Dados')
plt.ylim(0, 0.2)
plt.xlim(100, 1400)
plt.title("Gráfico de Tempo de Execução por Técnica Aplicada no código (4 Threads)")
# Exibe o gráfico na tela:
plt.show()