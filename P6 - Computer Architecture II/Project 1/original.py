import pandas as pd
import numpy  as np


def delete_unnecessary_states(df):
	new_df = pd.DataFrame(df)	

	for index in range(len(new_df)):
		if(new_df['state'][index] == "suspended" or 
           new_df['state'][index] == "undefined" or
           new_df['state'][index] == "canceled"  or
           new_df['state'][index] == "failed"    or
           new_df['state'][index] == "live"      ):
			new_df.drop(index, inplace = True)					

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


def delete_empty(df, atributo):
	new_df = pd.DataFrame(df)

	index = 0		
 
	for index in range(len(new_df)):
		if(new_df[atributo][index] == 0.0):
			new_df.drop(index, inplace = True)				
		index+=1			

	# Caso algum elemento tenha sido removido, é necessário reorganizar os índices:
	if(len(df) != len(new_df)):
		# Quando usa-se o método drop, não há reorganização dos índices. 
		# Para tal, é necessário usar o reset_index
		new_df.reset_index(inplace=True, drop=True)

	return new_df

# Pré-processamento feito para a disciplina 
# de Introdução à Inteligência Artificial:
def preprocess_data(data_frame):
	# Recebe o dataFrame e cria uma cópia dele para fazer alterações nela
	# sem afetar o dataFrame original:
	modified_data_frame = pd.DataFrame(data_frame)

	# Deleta as colunas irrelevantes para o treinamento do modelo de IA:
	modified_data_frame.drop(['ID', 'name'], inplace=True, axis=1)

	# Deleta linhas que possuem valores na coluna state os quais não serão úteis:
	modified_data_frame = delete_unnecessary_states(modified_data_frame)
	# Deleta linhas que possuem valores vazios na coluna usd pledged:
	modified_data_frame = delete_empty(modified_data_frame, 'usd pledged')

	# Cria uma lista para guardar cada valor:
	initial_day = []	# No formato de data ano-mês-dia
	final_day = []	# No formato de data ano-mês-dia
	duration = []	# No formato convertido para dias

	# Itera de 0 até o número de linhas do data frame:
	for index in range(len(modified_data_frame)):
		# Para cada índice converte para dias o valor da data de inicio da
		# arrecadação e salva numa lista:
		initial_day.append(convertToDays(modified_data_frame['launched'][index]))

	# Itera de 0 até o número de linhas do data frame:
	for index in range(len(modified_data_frame)):
		# Para cada índice converte para dias o valor da data de fim da
		# arrecadação e salva numa lista:
		final_day.append(convertToDays(modified_data_frame['deadline'][index]))
		# A duração dos dias é igual a diferença entre o dia final e o inicial
		duration.append(final_day[index] - initial_day[index])

	# Após pegar a duração do projeto, as colunas deadline e launched não são mais úteis:
	modified_data_frame.drop(['deadline', 'launched'], inplace=True, axis=1)
	# É criado uma nova coluna com nome duration:
	modified_data_frame['duration'] = duration

	# Caso algum elemento tenha sido removido, é necessário reorganizar os índices:
	if(len(modified_data_frame) != len(data_frame)):
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
	
	# Itera em cada elemento da matriz formada por lista de atributos que
	# constituem listas de valores:
	for i in range(len(data_frame_list)):
		# O índice 5 é aquele relativo ao state, o qual assume apenas os valores 0 ou 1,
		# significando que já está normalizado:
		if i != 5:
			for j in range(len(data_frame_list[i])):
				# Fórmula de normalização de valores numa lista:
				normalized_value = (data_frame_list[i][j] - smallest_value_in_attribute[i])/(biggest_value_in_attribute[i] - smallest_value_in_attribute[i])

	            # iat substitui um valor por outro na posição especificada do data frame,
	            # aqui o j e i são trocados pois houve a inversão de coluna por linha
	            # quando o data frame foi transformado numa lista de listas:
				modified_data_frame.iat[j,i] = normalized_value









	



