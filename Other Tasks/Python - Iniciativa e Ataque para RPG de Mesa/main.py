import os
import re

while True:
	selected = input("Escolha uma das 3 Opções Abaixo:" ,
                     "\n  1 - Atualizar Jogadores   "   ,
                     "\n  2 - Iniciativa por Arquivo"   ,
                     "\n  3 - Ataque e Dano por Arquivo",
                     "\n  4 - Sair"                     ,)

	if not os.path.exists('data'):
		os.makedirs("data")

	if selected is 1:
		with open("data/characters.txt", r+) as file:
	if selected is 2:
		with open("data/initiatives.txt", r+) as file:
			encounters = []

			index = 0

			for line in file:
				if ":" in line:
					encounters[index] = str(index+1) + "º Encontro: " + line
					index += 1

	elif selected is 3:

	elif selected is 4:
		break
	else:
		continue