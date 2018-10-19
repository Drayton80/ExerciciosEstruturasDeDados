import pagesubstitution

# Define as listas de páginas para cada algoritmo de substituição de páginas:
list_pages = []

# Define o número de quadros da RAM que serão utilizados:
memory_frames_size = 0


# MANIPULAÇÃO DO ARQUIVO:
with open('inputs/test.txt', 'r') as file_text:
	# Separa o arquivo em linhas e salva elas em uma lista
	file_lines = file_text.read().splitlines()

	# Define quando for a primeira linha
	first_line = True

	# Separa as linhas por espaço para obter os números relativos à cada página
	for line in file_lines:
		# A primeira linha das entradas define o número de quadros que será disponibilizados para uso:
		if (first_line):
			# Salva o número de quadros:
			memory_frames_size = int(line)
			# Indica que já se passou da primeira linha:
			first_line = False
		else:
			# Preenche as listas com o número das páginas obtidos no arquivo de entradas:
			list_pages.append(int(line))


# ALGORITMO DE SUBSTITUIÇÃO DE PÁGINAS DO TIPO FIFO:
# Valor que define a quantidade de falta de páginas:
missing_pages = pagesubstitution.fifo(list_pages, memory_frames_size)
print("FIFO", missing_pages)

# ALGORITMO DE SUBSTITUIÇÃO DE PÁGINAS DO TIPO ÓTIMO:
# Valor que define a quantidade de falta de páginas:
missing_pages = pagesubstitution.otm(list_pages, memory_frames_size)
print("OTM", missing_pages)

# ALGORITMO DE SUBSTITUIÇÃO DE PÁGINAS DO TIPO LRU:
# Valor que define a quantidade de falta de páginas:
missing_pages = pagesubstitution.lru(list_pages, memory_frames_size)
print("LRU", missing_pages)