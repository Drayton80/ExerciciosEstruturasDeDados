# Nota: para o cmd do windowns, rodar o comando chcp1252

import os
import re
import tkinter as tk

encounters_saved = []

def update_characters(characters):
	with open("data/characters.txt", "r") as file:
		for _ in range(len(characters)):
			list.pop()

		for line in file:
			character = re.sub("\n|\t", "", line)
			characters.append(character.split(" "))

def update_information():
	listbox_encounters.delete(0, tk.END)

	with open("data/encounters.txt", "r") as file:
		i = 0
		single_encounter = []
		single_creature = ""
		previous_line = ""
		encounter_end = False

		for line in file:
			if (i == 0):
				encounter_title = str(i+1) + "º - Encontro: " + line
				listbox_encounters.insert(tk.END, encounter_title)

				single_encounter.append(line)

				i += 1

			else:
				# Se o encontro acabou na linha passada, é salvo o título do próximo encontro:
				if encounter_end is True:
					encounter_title = str(i+1) + "º - Encontro: " + line
					listbox_encounters.insert(tk.END, encounter_title)

					single_encounter.append(line)

					encounter_end = False
					i += 1

				# Se ambas as linhas, atual e anterior, estiverem vazias, significará
				# que o encontro acabou:
				if (not line.strip() and not previous_line.strip()):
					encounters_saved.append(single_encounter)
					single_encounter = []
					encounter_end = True
				# Se apenas a atual estiver vazia, significa que a descrição de uma criatura acabou:
				elif (not line.strip()):
					single_encounter.append(single_creature)
					single_creature = ""
				# Se não for nenhuma das anteriores, significará que a criatura ainda está sendo descrita:
				else:
					single_creature += line

			# Salva o conteúdo da linha anterior:
			previous_line = line

		listbox_information.delete(0, tk.END)

		for element in encounters_saved:
			text = ""

			for lines in element:
				divide = lines.split("\n")

				for single in divide:
					listbox_information.insert(tk.END, single)

			

encounters_title   = []
button_width = 20

root = tk.Tk()

# WIDGETS CREATION:
# scroll bar:
scrollbar_encounters  = tk.Scrollbar(root)
scrollbar_information = tk.Scrollbar(root)
scrollbar_roll        = tk.Scrollbar(root)
# list box:
listbox_encounters  = tk.Listbox(root)
listbox_information = tk.Listbox(root)
listbox_roll        = tk.Listbox(root)
# button:
button_update_information = tk.Button(root, width=button_width, text="Atualizar Informações", 
                                          command=update_information)
button_select_encounter   = tk.Button(root, width=button_width, text="Selecionar Encontro")
button_roll_dices         = tk.Button(root, width=button_width, text="Rolar Dados de Iniciativa e Ataque")

# LAYOUT ORGANIZATION:
# top buttons:
button_update_information.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
button_select_encounter.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
button_roll_dices.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
# lists and scroll bars:
scrollbar_encounters.pack(side=tk.RIGHT, fill=tk.Y)
listbox_encounters.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
scrollbar_information.pack(side=tk.RIGHT,  fill=tk.Y)
listbox_information.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
scrollbar_roll.pack(side=tk.RIGHT, fill=tk.Y)
listbox_roll.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# LISTBOX AND SCROLL BAR HITCHING:
# list box:
listbox_encounters.config(yscrollcommand=scrollbar_encounters.set)
listbox_information.config(yscrollcommand=scrollbar_information.set)
listbox_roll.config(yscrollcommand=scrollbar_roll.set)
# scroll bar:
scrollbar_encounters.config(command=listbox_encounters.yview)
scrollbar_information.config(command=listbox_information.yview)
scrollbar_roll.config(command=listbox_roll.yview)

# 
update_information()

# SCREEN DEFINITIONS:
root.geometry("1360x920")
root.title("Auxiliar RPG")
root.mainloop()

'''
while True:
	divide_screen()

	characters = []

	selected = input("Escolha uma das 3 Opções Abaixo:" +
                     "\n  0 - Sair"                     +
                     "\n  1 - Iniciativa por Arquivo"   +
                     "\n  2 - Ataque e Dano por Arquivo"+
                     "\n  C - Mostrar Personagens\n  "  )


	if not os.path.exists('data'):
		os.makedirs("data")

	update_characters(characters)

	divide_screen()


	if selected is '0':
		break

	elif selected is '1':
		roll_initiatives = True

		
		while roll_initiatives is True:
			# É exibido a primeira opção antes da lista de encontros:
			print("0 - Voltar")

			encounters_title = ""

			i = 1

			# Aqui é feito print de todos os encontros que podem ser selecionados
			# para haver a rolagem de iniciativas	
			with open("data/encounters.txt", "r") as file:
				for line in file:
					if symbol_encounter_start() in line:
						line = line.replace("|{", " ")
						encounters_title += str(i) + " - Encontro: " + line + "\n"
						i += 1

			# Aqui é pego o input do teclado relativo a escolha do usuário:
			selected_initiative = input(encounters_title)

			# Se a escolha for 0 significará que ele quer voltar para o menu inicial:
			if selected_initiative is '0':
				roll_initiatives = False

			# Se a escolha for um dígito inteiro válido procura-se o encontro relativo
			# ao inteiro colocado como entrada:
			elif selected_initiative.isdigit():
				encounter_creatures = []
				encounter_selected = int(selected_initiative)
				encounter_index = 1
				encounter_found = False
				creature_information = ""

				with open("data/encounters.txt", "r") as file:
					for line in file:
						# Encontra-se o encontro o qual está sendo procurando:
						if encounter_found is False:
							if symbol_encounter_start() in line:
								if encounter_selected == encounter_index:
									encounter_found = True
								else:
									encounter_index += 1
						# Caso o encontro seja encontrado, ele é salvo numa lista:
						else:
							# Se a linha não possuir nada escrito nela, ou seja, se
							# ela estiver vazia:
							if not line.strip():
								# A criatura anterior é salva e
								encounter_creatures.append(creature_information)
								# limpa o string de informações da criatura para poder
								# começar a salvar uma nova:
								creature_information = ""
							else:
								creature_information += line + "\n"

					print(encounter_creatures)


	elif selected is '2':
		break
	elif selected is 'C' or 'c':
		print('Personagens no Arquivo:')
		print(characters, "\n")
'''