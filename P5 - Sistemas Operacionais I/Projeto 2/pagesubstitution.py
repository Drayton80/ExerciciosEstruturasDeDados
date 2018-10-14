''' Função First In, First Out (FIFO):
''   Informações:   
''     Autor: Drayton80
''     Data de Criação: 14/10/2018
'' 
''   Descrição: 
''     Esta função recebe uma lista de páginas em sequência de execução e o número de quadros disponível em memória para poder
''     simular inserções, faltas e substituições de páginas na memória RAM, retornando o número exato de falta de páginas que houve
''     com a utilização do Algoritmo de Substituicão de Páginas FIFO.
'' 
''   Parâmetros de Entrada:
''     list_pages: lista de páginas em sequência de execução;
''     memory_frames_size: numero de quadros livres na memória para a execução das páginas;
''
''   Retorno:
''     É retornado a o número de falta de páginas;
'''
def fifo(list_pages, memory_frames_size):
	list_memory_pages = []   # Lista de páginas que estão nos quadros da memória em determinado momento
	missing_pages = 0        # Número de falta de páginas

	# Inicia todas as posições da lista com -1 para saber que estão vazias:
	for useless in range(memory_frames_size):
		list_memory_pages.append('empty')

	# Aqui é onde toda a simulação roda, não sendo necessário contabilizar o tempo, mas sim a
	# posição na lista de páginas em sequência de execução em que se encontra a simulação a cada momento
	for page in list_pages:

		# FALTA DE PÁGINAS:
		# Se a página não estiver na lista de páginas que estão naquele momento nos quadros da memória
		# isso significa que ocorreu uma falta de páginas
		if(not page in list_memory_pages):
			# Increment-ase o inteiro que define a quantidade de falta de páginas
			missing_pages += 1

			# SUBSTITUIÇÃO DE PÁGINAS:
			# Quando não houver mais espaços vazios na lista de páginas na memória significará que ela estará toda
			# preenchida, ou seja, será necessário haver substituição de páginas:
			# Nota: Essa parte poderia ser resumida para apenas:
			#         list_memory_pages.pop(0)
			#         list_memory_pages.append(page)
			#       Mas por fins tanto didáticos quanto de visualização de diferenças entre algoritmos resolvi 
			#       deixá-la dessa forma
			if(not 'empty' in list_memory_pages):
				# Retira-se a página do início da lista, ou seja, aquela que foi a primeira a entrar:
				list_memory_pages.pop(0)
				# Adiciona a nova página no final da lista:
				list_memory_pages.append(page)

			# Caso contrário será apenas necessário adicionar a página no fim da lista:
			else:
				# Retira-se um dos 'empty' do início da lista
				list_memory_pages.pop(0)
				# e Adiciona a página no final dela:
				list_memory_pages.append(page)

	return missing_pages


''' Função Ótimo (OTM):
''   Informações:   
''     Autor: Drayton80
''     Data de Criação: 14/10/2018
'' 
''   Descrição: 
''     Esta função recebe uma lista de páginas em sequência de execução e o número de quadros disponível em memória para poder
''     simular inserções, faltas e substituições de páginas na memória RAM, retornando o número exato de falta de páginas que houve
''     com a utilização do Algoritmo de Substituicão de Páginas Ótimo.
'' 
''   Parâmetros de Entrada:
''     list_pages: lista de páginas em sequência de execução;
''     memory_frames_size: numero de quadros livres na memória para a execução das páginas;
''
''   Retorno:
''     É retornado a o número de falta de páginas;
'''
def otm(list_pages, memory_frames_size):
	list_memory_pages = []   # Lista de páginas que estão nos quadros da memória em determinado momento
	missing_pages = 0        # Número de falta de páginas

	# Inicia todas as posições da lista com -1 para saber que estão vazias:
	for useless in range(memory_frames_size):
		list_memory_pages.append('empty')

	i = 0

	# Aqui é onde toda a simulação roda, não sendo necessário contabilizar o tempo, mas sim a
	# posição na lista de páginas em sequência de execução em que se encontra a simulação a cada momento
	for page in list_pages:

		# FALTA DE PÁGINAS:
		# Se a página não estiver na lista de páginas que estão naquele momento nos quadros da memória
		# isso significa que ocorreu uma falta de páginas
		if(not page in list_memory_pages):
			# Increment-ase o inteiro que define a quantidade de falta de páginas
			missing_pages += 1

			# SUBSTITUIÇÃO DE PÁGINAS:
			# Quando não houver mais espaços vazios na lista de páginas na memória significará que ela estará toda
			# preenchida, ou seja, será necessário haver substituição de páginas:
			if(not 'empty' in list_memory_pages):
				# Lista que guarda o índice da próxima chamada de cada elemento presente na lista das páginas
				# que estão em quadros da memória
				next_call_index = []

				# Inicia todos os índices com valores -1:
				for useless in range(memory_frames_size):
					next_call_index.append(-1)

				# Verifica quando será a próxima chamada das páginas que estão nos quadros da memória principal:
				for memory_page in list_memory_pages:
					# Checa se a página na memória é chamada novamente em algum momento da próxima posição da lista
					# de sequência de páginas até o final da lista:
					if(memory_page in list_pages[i+1:]):
						# Se ela for referenciada, varre a lista para saber qual será sua próxima posição:
						for index in range(i+1, memory_frames_size):
							# Se encontrar a próxima referência:
							if(memory_page == list_pages[index]):
								# Retira-se um dos -1 da lista:
								next_call_index.pop(0)
								# Salva o índice no final da lista de próximas chamadas
								next_call_index.append(index)
								# e Encerra o laço interno para não salvar mais de um índice
								# de referência, garantindo que apenas a próxima referência
								# seja salva na lista:
								break
						# Se a página não for referenciada, continuará com -1 como índice da próxima referência (já que é um
						# índice que nunca será uma posição válida da lista)

				# A ultima página a ser chamada apenas será -1 quando todos os elementos de next_call_index forem -1
				# e isso apenas ocorre quando não há mais chamadas de qualquer página que esteja em list_memory_pages
				if(max(next_call_index) != -1):
					# Pega o índice da página que foi a ultima a ser referenciada dentre as próximas chamadas, ou seja,
					# a que demora mais tempo para ser chamada novamente:
					last_call_index = next_call_index.index(max(next_call_index))

					# Retira-se a página que demorará mais tempo para ser chamada novamente: 
					list_memory_pages.pop(last_call_index)

					# Adiciona-se a nova página:
					list_memory_pages.append(page)	

			# Caso contrário será apenas necessário adicionar a página no fim da lista:
			else:
				# Retira-se um dos 'empty' do início da lista
				list_memory_pages.pop(0)
				# e Adiciona a página no final dela:
				list_memory_pages.append(page)

		i += 1

	return missing_pages



''' Função Less Recently Used (LRU):
''   Informações:   
''     Autor: Drayton80
''     Data de Criação: 14/10/2018
'' 
''   Descrição: 
''     Esta função recebe uma lista de páginas em sequência de execução e o número de quadros disponível em memória para poder
''     simular inserções, faltas e substituições de páginas na memória RAM, retornando o número exato de falta de páginas que houve
''     com a utilização do Algoritmo de Substituicão de Páginas LRU.
'' 
''   Parâmetros de Entrada:
''     list_pages: lista de páginas em sequência de execução;
''     memory_frames_size: numero de quadros livres na memória para a execução das páginas;
''
''   Retorno:
''     É retornado a o número de falta de páginas;
'''
def otm(list_pages, memory_frames_size):
	list_memory_pages = []   # Lista de páginas que estão nos quadros da memória em determinado momento
	missing_pages = 0        # Número de falta de páginas

	# Inicia todas as posições da lista com -1 para saber que estão vazias:
	for useless in range(memory_frames_size):
		list_memory_pages.append('empty')

	i = 0

	# Aqui é onde toda a simulação roda, não sendo necessário contabilizar o tempo, mas sim a
	# posição na lista de páginas em sequência de execução em que se encontra a simulação a cada momento
	for page in list_pages:

		# FALTA DE PÁGINAS:
		# Se a página não estiver na lista de páginas que estão naquele momento nos quadros da memória
		# isso significa que ocorreu uma falta de páginas
		if(not page in list_memory_pages):
			# Increment-ase o inteiro que define a quantidade de falta de páginas
			missing_pages += 1

			# SUBSTITUIÇÃO DE PÁGINAS:
			# Quando não houver mais espaços vazios na lista de páginas na memória significará que ela estará toda
			# preenchida, ou seja, será necessário haver substituição de páginas:
			if(not 'empty' in list_memory_pages):
				# Lista que guarda o índice da próxima chamada de cada elemento presente na lista das páginas
				# que estão em quadros da memória
				next_call_index = []

				

			# Caso contrário será apenas necessário adicionar a página no fim da lista:
			else:
				# Retira-se um dos 'empty' do início da lista
				list_memory_pages.pop(0)
				# e Adiciona a página no final dela:
				list_memory_pages.append(page)

		i += 1

	return missing_pages


