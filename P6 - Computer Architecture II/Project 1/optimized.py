import pandas as pd
import numpy  as np
from tqdm import tqdm

'''
class Days:
	def __init__(self, initialDay, finalDay, duration):
		self.initialDay = initialDay
		self.finalDay = finalDay
		self.duration = duration

	def get_initialDay(self):
		return self.initialDay

	def get_finalDay(self):
		return self.finalDay

	def get_duration(self):
		return self.duration

	def set_initialDay(self, initialDay):
		self.initialDay = initialDay

	def set_finalDay(self, finalDay):
		self.finalDay = finalDay

	def set_duration(self, duration):
		self.duration = duration
'''

def convertToDays(date):
	#|print("Ano:", int(date[0:4]))
	# Soma-se os dias de todos os anos anteriores [ ( int(date[0:4])-1 )*365 ], contando com à soma dos dias à 
	# mais advindos dos anos bissextos anteriores [ int( (int(date[0:4])-1)/4) ], até chegar no ano da data e 
	# verificar quantos dias em específico ele têm indo para os meses e, por fim, os dias
	days = 0 + ( int(date[0:4])-1 )*365 + int( (int(date[0:4])-1)/4)

	#|print("Dias após anos:", days)

	# Se for maior que o mês significa que o número de dias do respectivo mês deve ser
	# acrescentado na conta dos dias, ou seja, a cada mês passado seu número de dias deve ser
	# incrementado na contagem de dias até que chegue no mês que o atributo da data está para só assim
	# poder passar para a parte dos dias e somá-los na conta
	# somar com os dos meses posteriores
	#|print("Mês:", int(date[5:7]) )
	if 1 < int(date[5:7]):
		days += 31
	if 2 < int(date[5:7]):
		# Se o ano for bissexto Fevereiro terá 29 dias
		if (int(date[0:4])%4) == 0:
			days += 29
		else:
			days += 28
	if 3 < int(date[5:7]):
		days += 31
	if 4 < int(date[5:7]):
		days += 30
	if 5 < int(date[5:7]):
		days += 31
	if 6 < int(date[5:7]):
		days += 30
	if 7 < int(date[5:7]):
		days += 31
	if 8 < int(date[5:7]):
		days += 31
	if 9 < int(date[5:7]):
		days += 30
	if 10 < int(date[5:7]):
		days += 31
	if 11 < int(date[5:7]):
		days += 30
	
	# Por fim, soma-se os dias da data aos dias totais:
	days += int(date[8:10])

	#|print("Dias após dias", days)
	return days


def deleteNoise_and_atributoNeutro(df, i): 
	if(df['state'][i] == "suspended" or 
       df['state'][i] == "undefined" or
       df['state'][i] == "canceled"  or
       df['state'][i] == "failed"    or
       df['state'][i] == "live"      or
       df['usd pledged'][i] == 0.0   ):
		df.drop(i, inplace = True)
		return True
	else:
		return False			

	


# Parte mais significante de um pré-processamento feito para a disciplina 
# de Introdução à Inteligência Artificial:
def preprocess_data(data_frame):
	modified_data_frame = pd.DataFrame(data_frame)

	# 3 Listas resumidas em apenas uma lista de objetos, ou seja,
	# foi feita uma "Mesclagem de Arrays"
	days_information = []
	duration = []

	# Junção de Loops:
	for index in range(len(modified_data_frame)):
		deleted = deleteNoise_and_atributoNeutro(modified_data_frame, index)

		if not deleted:
			duration.append(convertToDays(modified_data_frame['deadline'][index]) - convertToDays(modified_data_frame['launched'][index]))

	# Caso algum elemento tenha sido removido, é necessário reorganizar os índices:
	if(len(data_frame) != len(modified_data_frame)):
		# Quando usa-se o método drop, não há reorganização dos índices. 
		# Para tal, é necessário usar o reset_index
		modified_data_frame.reset_index(inplace=True, drop=True)

	modified_data_frame = modified_data_frame.drop(['deadline', 'launched'], 1)
	modified_data_frame['duration'] = duration



