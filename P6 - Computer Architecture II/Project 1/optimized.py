import pandas as pd
import numpy  as np
from tqdm import tqdm


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


def delete_empty_pledge_and_unnecessary_state(df, i): 
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
	# Recebe o data frame e cria uma cópia dele para fazer alterações nela
	# sem afetar o data frame original:
	modified_data_frame = pd.DataFrame(data_frame)

	# Deleta as colunas irrelevantes para o treinamento do modelo de IA:
	modified_data_frame.drop(['ID', 'name'], inplace=True, axis=1)

	# 3 Listas resumidas em apenas uma lista de objetos, ou seja,
	# foi feita uma "Mesclagem de Arrays"
	days_information = []
	duration = []

	# Junção de Loops:
	for index in range(len(modified_data_frame)):
		# Deleta linhas que possuem valores na coluna state os quais não serão úteis e
		# também deleta linhas que possuem valores vazios na coluna usd pledged. Se
		# o valor for deletado, retorna True, caso contrário, False:
		deleted = delete_empty_pledge_and_unnecessary_state(modified_data_frame, index)

		if not deleted:
			# Se não houve remoção, guarda a duração da arrecadação do projeto dado pela diferença da data do deadline
			# com a data de inicio da arrecadação, ambas convertidas para um valor em dias:
			duration.append(convertToDays(modified_data_frame['deadline'][index]) - convertToDays(modified_data_frame['launched'][index]))

	# Após pegar a duração do projeto, as colunas deadline e launched não são mais úteis:
	modified_data_frame.drop(['deadline', 'launched'], inplace=True, axis=1)
	# É criado uma nova coluna com nome duration:
	modified_data_frame['duration'] = duration

	# Caso algum elemento tenha sido removido, é necessário reorganizar os índices:
	if(len(data_frame) != len(modified_data_frame)):
		# Quando usa-se o método drop, não há reorganização dos índices. 
		# Para tal, é necessário usar o reset_index
		modified_data_frame.reset_index(inplace=True, drop=True)

	# Transforma os atributos que são classes em numeros naturais:
	modified_data_frame['main_category'] = pd.factorize(modified_data_frame['main_category'])[0]
	modified_data_frame['category'] = pd.factorize(modified_data_frame['category'])[0]
	modified_data_frame['currency'] = pd.factorize(modified_data_frame['currency'])[0]
	modified_data_frame['country'] = pd.factorize(modified_data_frame['country'])[0]
	modified_data_frame['state'] = pd.factorize(modified_data_frame['state'])[0]

	data_frame_list = []
	biggest_value_in_attribute = []
	smallest_value_in_attribute = []

	# Para cada coluna (atributo) no data frame:
	for attribute in modified_data_frame:
		# Salva seus valores como uma lista em data_frame_list:
		data_frame_list.append(modified_data_frame[attribute].to_list())
		# Guarda o menor e o maior valor de cada atributo em uma lista:
		biggest_value_in_attribute.append(max(modified_data_frame[attribute].to_list()))
		smallest_value_in_attribute.append(min(modified_data_frame[attribute].to_list())) 

	number_of_lines = len(data_frame_list)
	number_of_columns = len(data_frame_list[0])
	# Itera em cada elemento da matriz formada por lista de atributos que
	# constituem listas de valores:
	B = 100
	ii = 0
	jj = 0

	# Aplicação da blocagem:
	while (ii < number_of_lines):
		while (jj < number_of_columns):
			i = ii
			j = jj	

			while (i < min(ii+B-1, number_of_lines)):
				if i != 5:
					while (j < min(jj+B-1, number_of_columns)):
						# Fórmula de normalização de valores numa lista:
						normalized_value = (data_frame_list[i][j] - smallest_value_in_attribute[i])/(biggest_value_in_attribute[i] - smallest_value_in_attribute[i])

			            # iat substitui um valor por outro na posição especificada do data frame,
			            # aqui o j e i são trocados pois houve a inversão de coluna por linha
			            # quando o data frame foi transformado numa lista de listas:
						modified_data_frame.iat[j,i] = normalized_value
						
						j += 1
				i += 1
			jj += B
		ii += B