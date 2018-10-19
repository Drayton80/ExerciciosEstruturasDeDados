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

	# Inicia todas as posições da lista com 'empty' para saber que estão vazias:
	for _ in range(memory_frames_size):
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

	# Inicia todas as posições da lista com 'empty' para saber que estão vazias:
	for _ in range(memory_frames_size):
		list_memory_pages.append('empty')

	i = 0

	# Aqui é onde toda a simulação roda, não sendo necessário contabilizar o tempo, mas sim a
	# posição na lista de páginas em sequência de execução em que se encontra a simulação a cada momento
	for page in list_pages:
		#>print(list_memory_pages, "\n")
		#>print(page)

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

				# Inicia todos os índices da lista de próximas chamadas com 'none', ou seja, assume de primeira
				# que não há próximas chamadas para depois checar se realmente há ou não:
				for _ in range(memory_frames_size):
					next_call_index.append('none')

				# Guarda a posição do elemento atual que será checado da lista de páginas na memória
				memory_page_index = 0

				# Verifica quando será a próxima chamada das páginas que estão nos quadros da memória principal:
				for memory_page in list_memory_pages:
					# Checa se a página na memória é chamada novamente em algum momento da próxima posição da lista
					# de sequência de páginas até o final da lista:
					if(memory_page in list_pages[i:]):
						# Se ela for referenciada, varre a lista para saber qual será sua próxima posição:
						for index in range(i, len(list_pages)):
							# Se encontrar a próxima referência:
							if(memory_page == list_pages[index]):
								# Retira-se um dos 'none' da lista e salva o índice em seu lugar da lista de próximas chamadas
								next_call_index[memory_page_index] = index
								# Encerra o laço interno para não salvar mais de um índice
								# de referência, garantindo que apenas a próxima referência
								# seja salva na lista:
								break
						# Se a página não for referenciada, continuará com -1 como índice da próxima referência (já que é um
						# índice que nunca será uma posição válida da lista)
					# Incrementa o elemento de posição:
					memory_page_index += 1

				# Checa se há algum elemento que não possuí próxima chamada na lista next_call_index:
				if('none' in next_call_index):
					# Se houver, é retirado a primeira página da fila que não possuir próxima chamada, ou seja, a condição
					# de retirada torna-se uma FIFO entre as páginas que não possuem próxima referência na lista: 
					list_memory_pages.pop(next_call_index.index('none'))
					# Adiciona-se a nova página no final:
					list_memory_pages.append(page)
				else:
					# Caso contrário, pega o índice da página que foi a ultima a ser referenciada dentre as próximas 
					# chamadas, ou seja, a que demora mais tempo para ser chamada novamente:
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
''     Data de Criação: 15/10/2018
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
def lru(list_pages, memory_frames_size):
	list_memory_pages = []   # Lista de páginas que estão nos quadros da memória em determinado momento
	missing_pages = 0        # Número de falta de páginas

	# Inicia todas as posições da lista com 'empty' para saber que estão vazias:
	for _ in range(memory_frames_size):
		list_memory_pages.append('empty')

	i = 0

	# Aqui é onde toda a simulação roda, não sendo necessário contabilizar o tempo, mas sim a
	# posição na lista de páginas em sequência de execução em que se encontra a simulação a cada momento
	for page in list_pages:

		# FALTA DE PÁGINAS:
		# Se a página não estiver na lista de páginas que estão naquele momento nos quadros da memória
		# isso significa que ocorreu uma falta de páginas
		if(not page in list_memory_pages):
			# Incrementa-se o inteiro que define a quantidade de falta de páginas
			missing_pages += 1

			# SUBSTITUIÇÃO DE PÁGINAS:
			# Quando não houver mais espaços vazios na lista de páginas na memória significará que ela estará toda
			# preenchida, ou seja, será necessário haver substituição de páginas:
			if(not 'empty' in list_memory_pages):
				# Lista que guarda o índice da chamada anterior de cada elemento presente na lista das páginas
				# que estão em quadros da memória
				previous_call_index = []

				# Inicia-os indices com valores 'none' ou, em outras palavras, assume primeiramente que não há
				# referências anteriores das páginas na memória para apenas em seguida checar se isso é verdade:
				for _ in range(memory_frames_size):
					previous_call_index.append('none')

				# Guarda a posição do elemento atual que será checado da lista de páginas na memória
				memory_page_index = 0

				# Verifica se houve chamada anterior das páginas na memória e, em caso afirmativo, pega o índice
				# de quando isso aconteceu:
				for memory_page in list_memory_pages:
					# Checa se a página na memória foi chamada anteriormente alguma vez:
					if(memory_page in list_pages[0:i]):
						# Se ela foi referenciada, varre a lista para saber qual foi sua última chamada:
						for index in range(0,i):
							# Se encontrar a próxima referência:
							if(memory_page == list_pages[index]):
								# Substitui um dos elementos 'none' pelo índice relativo ao elemento
								previous_call_index[memory_page_index] = index
								# Como a cada chamada o valor aqui é atualizado, tem-se que apenas
								# a última referência anterior a i que ficará salva
					# Atualiza o índice relativo ao bloco que está sendo referenciado na memória:
					memory_page_index += 1 

				# Como toda vez que uma página é adicionada na memória significa também que ela foi referenciada,
				# ou seja, ela vai existir anteriormente na lista, tem-se que não é preciso sequer checar se ela
				# está lá, apenas pegar sua referência, pois é certo que ela estará (isso ocorre também devido a
				# condição de substituição dos 'empty' quando a lista de processos na memória inicia vazia)
				# Pega o índice da página que foi chamada a mais tempo dentre as anteriores:
				less_call_index = previous_call_index.index(min(previous_call_index))

				# Retira-se a página que demorará mais tempo para ser chamada novamente: 
				list_memory_pages.pop(less_call_index)
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