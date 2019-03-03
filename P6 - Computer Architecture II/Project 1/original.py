import pandas as pd
import numpy  as np


def atributoNeutro(df, atributo):
	new_df = pd.DataFrame(df)	

	for i in range(len(new_df)):
		if(new_df['state'][i] == "suspended" or 
           new_df['state'][i] == "undefined" or
           new_df['state'][i] == "canceled"  or
           new_df['state'][i] == "failed"    or
           new_df['state'][i] == "live"      ):
			new_df.drop(i, inplace = True)					

	# Caso algum elemento tenha sido removido, é necessário reorganizar os índices:
	if(len(df) != len(new_df)):
		# Quando usa-se o método drop, não há reorganização dos índices. 
		# Para tal, é necessário usar o reset_index
		new_df.reset_index(inplace=True, drop=True)	

	return new_df


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


def deleteNoise(df, atributo):
	new_df = pd.DataFrame(df)

	i = 0		
 
	for i in range(len(new_df)):
		if(new_df[atributo][i] == 0.0):
			new_df.drop(i, inplace = True)				
		i+=1			

	# Caso algum elemento tenha sido removido, é necessário reorganizar os índices:
	if(len(df) != len(new_df)):
		# Quando usa-se o método drop, não há reorganização dos índices. 
		# Para tal, é necessário usar o reset_index
		new_df.reset_index(inplace=True, drop=True)

	return new_df

# Parte mais significante de um pré-processamento feito para a disciplina 
# de Introdução à Inteligência Artificial:
def preprocess_data(data_frame):
	dataFrame = pd.DataFrame(data_frame)

	dataFrame = atributoNeutro(dataFrame, 'state')
	dataFrame = deleteNoise(dataFrame, 'usd pledged')

	initialDay = []	# No formato de data ano-mês-dia
	finalDay = []	# No formato de data ano-mês-dia
	duration = []	# No formato convertido para dias

	#for i in range(len(dataFrame)):
		#initialDay.append(convertToDays(dataFrame['launched'][i]))


	#for i in range(len(dataFrame)):
		#finalDay.append(convertToDays(dataFrame['deadline'][i]))
		# A duração dos dias é igual a diferença entre o dia final e o inicial
		#duration.append(finalDay[counter] - initialDay[counter])

	dataFrame = dataFrame.drop(['deadline', 'launched'], 1)
	#dataFrame['duration'] = duration


