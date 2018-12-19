import os
import re
import math
import tkinter as tk

from random import randint
from encounter import Encounter
from creature  import Creature


encounters_saved = []

'''
def update_information_old():
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
'''
'''			
def select_encounter_old():
	# Define o índice do encontro que será exibido baseado no que foi selecionado
	# na list box dos encontros. Nada acontece caso não tenha sido feito a seleção
	if listbox_encounters.curselection():
		selected = listbox_encounters.curselection()
		encounter_index = selected[0]

		encounter_selected = encounters_saved[encounter_index]

		listbox_information.delete(0, tk.END)

		# Esse for serve para formatar o texto do encontro de tal forma a ficar corretamente
		# disposto linha a linha no listbox sem ultrapassar um certo limite horizontal
		for element in encounter_selected:
			# Define o número máximo de palavras que uma linha pode ter:
			max_line_size = 40

			lines = element.split("\n")

			for line in lines:
				words = line.split(" ")

				# Se o tamanho do parágrafo exceder o número máximo de palavras permitida,
				# é organizado para que apenas haja no máximo um número n de palavras por linha:
				if len(words) > max_line_size:
					text_size = 0
					text = ""

					for word in words:
						# Se o tamanho do texto for igual ao tamanho máximo, é impresso o
						# texto atual no listbox, o conteúdo do texto é apagado e o tamanho 
						# atual do texto retorna ao valor inicial, que é 0
						if text_size == max_line_size:
							listbox_information.insert(tk.END, text)
							text_size = 0
							text = ""
						# As palavras são adicionadas ao texto enquanto o tamanho máximo
						# não for alcançado:
						else:
							text += word + " "

						text_size += 1

				# Caso contrário, exibe-se normalmente no listbox o conteúdo da linha
				else:
					listbox_information.insert(tk.END, line)
'''

def update_information():
	listbox_encounters.delete(0, tk.END)

	with open("data/encounters.txt", "r") as file:
		i = 0
		creature_text = ""
		creatures = []
		previous_line = ""
		encounter_end = False

		for line in file:
			if (i == 0): 
				listbox_encounters.insert(tk.END, str(i+1) + "º - Encontro: " + line)

				title = line
				i += 1

			else:
				# Se o encontro acabou na linha passada, é salvo o título do próximo encontro:
				if encounter_end is True:
					listbox_encounters.insert(tk.END, str(i+1) + "º - Encontro: " + line)

					title = line
					encounter_end = False
					i += 1
				# Se ambas as linhas, atual e anterior, estiverem vazias, significará
				# que o encontro acabou:
				elif (not line.strip() and not previous_line.strip()):
					encounters_saved.append(Encounter(title, creatures))
					encounter_end = True
					creatures = []
				# Se apenas a atual estiver vazia, significa que a descrição de uma criatura acabou:
				elif (not line.strip()):
					creatures.append(Creature(creature_text))
					creature_text = ""
				# Se não for nenhuma das anteriores, significará que a criatura ainda está sendo descrita:
				else:
					creature_text += line

			# Salva o conteúdo da linha anterior:
			previous_line = line


def select_encounter():
	# Define o índice do encontro que será exibido baseado no que foi selecionado
	# na list box dos encontros. Nada acontece caso não tenha sido feito a seleção
	if listbox_encounters.curselection():
		selected = listbox_encounters.curselection()
		encounter_index = selected[0]

		encounter_selected = Encounter(encounters_saved[encounter_index].get_title(),
                                       encounters_saved[encounter_index].get_creatures())

		listbox_information.delete(0, tk.END)
		listbox_information.insert(tk.END, encounter_selected.get_title())

		# Esse for serve para formatar o texto do encontro de tal forma a ficar corretamente
		# disposto linha a linha no listbox sem ultrapassar um certo limite horizontal
		for creature in encounter_selected.get_creatures():
			# Define o número máximo de palavras que uma linha pode ter:
			max_line_size = 38

			lines = creature.get_text().split("\n")

			for line in lines:
				words = line.split(" ")

				# Se o tamanho do parágrafo exceder o número máximo de palavras permitida,
				# é organizado para que apenas haja no máximo um número n de palavras por linha:
				if len(words) > max_line_size:
					text_size = 0
					text = ""

					for word in words:
						# Se o tamanho do texto for igual ao tamanho máximo, é impresso o
						# texto atual no listbox, o conteúdo do texto é apagado e o tamanho 
						# atual do texto retorna ao valor inicial, que é 0
						if text_size == max_line_size:
							listbox_information.insert(tk.END, text)
							text_size = 0
							text = ""
						# As palavras são adicionadas ao texto enquanto o tamanho máximo
						# não for alcançado:
						else:
							text += word + " "

						text_size += 1

				# Caso contrário, exibe-se normalmente no listbox o conteúdo da linha
				else:
					listbox_information.insert(tk.END, line)


def initiative_sort_key(creatures_in_battle):
	return creatures_in_battle.get_initiative()

def roll_dices():
	selected = listbox_encounters.curselection()
	encounter_index = selected[0]

	enemies = encounters_saved[encounter_index].get_creatures()
	enemies_change = []

	print("tamanho de enemies =", len(enemies))

	characters = []
	
	for i in range(len(encounters_saved[0].get_creatures())):
		characters.append(Creature(encounters_saved[0].get_creatures()[i].get_text()))

	for i in range(len(enemies)):
		enemies_change.append(Creature(enemies[i].get_text()))
		enemies_change[i].set_name("Inimigo " + str(i+1) + " - " + enemies[i].get_name())

	characters_encounter = Encounter(encounters_saved[0].get_title(), characters)
	enemies_encounter = Encounter(encounters_saved[encounter_index].get_title(), enemies_change)

	creatures_in_battle = []

	for i in range(len(enemies_encounter.get_creatures())):
		creatures_in_battle.append(enemies_encounter.get_creatures()[i])

	for i in range(len(characters_encounter.get_creatures())):
		creatures_in_battle.append(characters_encounter.get_creatures()[i])

	#creatures_in_battle = enemies_encounter.get_creatures() + characters.get_creatures()

	for i in range(len(creatures_in_battle)):
		dice_roll  = randint(1,20)
		initiative = creatures_in_battle[i].get_initiative()

		print(dice_roll)
		print(initiative)

		creatures_in_battle[i].set_initiative(dice_roll+initiative)

	creatures_in_battle = sorted(creatures_in_battle, key=initiative_sort_key)

	listbox_roll.delete(0, tk.END)

	for creature in creatures_in_battle:
		listbox_roll.insert(tk.END, creature.get_name() + " = " + str(creature.get_initiative()))



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
button_select_encounter   = tk.Button(root, width=button_width, text="Selecionar Encontro",
                                            command=select_encounter)
button_roll_dices         = tk.Button(root, width=button_width, text="Rolar Dados de Iniciativa e Ataque",
                                            command=roll_dices)

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
select_encounter()

# SCREEN DEFINITIONS:
root.geometry("1360x920")
root.title("Auxiliar RPG")
root.mainloop()