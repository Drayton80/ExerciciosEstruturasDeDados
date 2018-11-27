import os
import re

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
			line = re.sub("\n|\t", "", line)
			characters.append(line.split(" "))

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

		with open("data/encounters.txt", "r") as file:
			while roll_initiatives is True:
				# É exibido a primeira opção antes da lista de encontros:
				print("0 - Voltar")

				encounters_title = ""

				i = 1

				# Aqui é feito print de todos os encontros que podem ser selecionados
				# para haver a rolagem de iniciativas	
				for line in file:
					if symbol_encounter_start() in line:
						# line.replace("|{", " ")
						encounters_title += str(i) + " - Encontro: " + line + "\n"
						i += 1

				selected_initiative = input(encounters_title)

				if selected_initiative is '0':
					roll_initiatives = False

				elif selected_initiative.isdigit():
					encounter_creatures_index = 0
					encounter_creatures = []
					encounter_selected = int(selected_initiative)
					encounter_index = 1
					encounter_found = False

					for line in file:
						# Encontra-se o encontro o qual está sendo procurando:
						if encounter_found is False:
							if symbol_encounter_start in line:
								if encounter_selected == encounter_index:
									encounter_found = True
								else:
									encounter_index += 1
						# Caso o encontro seja encontrado, ele é salvo numa lista:
						else:
							if symbol_creature_start() in line:
								creature_information = ""
							elif symbol_creature_end() in line:
								encounter_creatures[encounter_creatures_index].append(creature_information)
								encounter_creatures_index += 1
							else:
								creature_information += line + "\n"


	elif selected is '2':
		break
	elif selected is 'C' or 'c':
		print('Personagens no Arquivo:')
		print(characters, "\n")
