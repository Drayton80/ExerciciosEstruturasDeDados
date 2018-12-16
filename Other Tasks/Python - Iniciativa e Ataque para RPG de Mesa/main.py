# Nota: para o cmd do windowns, rodar o comando chcp1252

import os
import re
import tkinter as tk


def symbol_encounter_start():
	return "|{"

def symbol_encounter_end():
	return "}|"

def symbol_creature_start():
	return "|["

def symbol_creature_end():
	return "]|"

def divide_screen():
	print("\n||------------------------------------------------------------||\n")

def update_characters(characters):
	with open("data/characters.txt", "r") as file:
		for _ in range(len(characters)):
			list.pop()

		for line in file:
			character = re.sub("\n|\t", "", line)
			characters.append(character.split(" "))


button_x = 25
button_y = 25
button_margin = 10
button_width = 20

root = tk.Tk()

scrollbar = tk.Scrollbar(root)
listbox = tk.Listbox(root)

button_initiative_file = tk.Button(root, width=button_width, text="Iniciativa por Arquivo")
#button_initiative_file.place(x=button_x, y=button_y)
button_exit = tk.Button(root, width=button_width, text="Sair")
#button_exit.place(x=button_x, y=button_y*2+button_margin)

button_initiative_file.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
button_exit.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
scrollbar.pack(side=tk.RIGHT, anchor=tk.N, fill=tk.Y)
listbox.pack(fill=tk.BOTH, expand=1)

for i in range(500):
	text = "text" + str(i)
	listbox.insert(tk.END, text)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


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