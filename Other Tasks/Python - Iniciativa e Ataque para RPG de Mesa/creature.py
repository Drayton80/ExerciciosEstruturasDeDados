import re

class Creature:
	# CLASS CONSTRUCTOR:
	def __init__(self, text):
		self.text = text
		self.name = Creature.search_name(text)
		self.initiative = Creature.search_initiative(text)
	# SET METHODS:
	def set_text(self, text):
		self.text = text

	def set_name(self, name):
		self.name = name

	def set_initiative(self, initiative):
		self.initiative = initiative

	# GET METHODS:
	def get_text(self):
		return self.text

	def get_name(self):
		return self.name

	def get_initiative(self):
		return self.initiative

	# OTHER METHODS:
	@staticmethod
	def search_initiative(text):
		# Caso find() não encontre o substring ele retorna -1, então apenas será salvo o valor do índice
		# caso seja encontrado:
		if (text.find("Iniciativa:") != -1 or text.find("iniciativa:") != -1):
			# O índice onde começará a ser buscado a iniciativa começa após a palavra de pesquisa:
			index_start = text.find("Iniciativa:") + len("Iniciativa:")
			index_end   = text.find(";", index_start)

			# É retirado apenas o texto entre 'Iniciativa:' (ou 'iniciativa:') e ';'
			initiative_text = text[index_start:index_end]
			# Aqui todos os caracteres que não sejam números, + e -
			initiative_text = re.sub("[^0-9\+\-]","", initiative_text)

			return int(initiative_text)

		# Caso contrário, a função encerra:
		else:
			print("ERRO: search_initiative() não encontrou iniciativa")
			
			return None

	@staticmethod
	def search_name(text):
		name = text.split("\n")[0]

		return name


