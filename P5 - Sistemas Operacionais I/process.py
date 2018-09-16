''' Classe Process:
''"  Informações:   
''"    Autor: Drayton80
''"    Data de Criação: 16/09/2018
''"
''"  Descrição: 
''"    Esta classe serve como uma simulação de um Processo da CPU contendo informações
''"    abstratas sobre o mesmo;
''"
''"  Atributos:
''"    number: numero inteiro que identifica o processo;
''"    time_arrival: tempo em que ele chegou na fila de espera pela primeira vez;
''"    time_start: tempo em que ele começou a ser executado pela primeira vez;
''"    time_end: tempo exato de sua finalização;
''"    time_remaining: tempo de execução restante para terminar;    
''"    time_waiting: serve para salvar o tempo que o processo passou na fila de espera; 
'''
class Process:
	def __init__(self, number, time_arrival, time_start, time_end, time_remaining, time_waiting):
		self.number = number
		self.time_arrival = time_arrival
		self.time_start = time_start
		self.time_end = time_end
		self.time_remaining = time_remaining
		self.time_waiting = time_waiting

	def get_return_time(self):
		# Tempo de retorno é dado pelo tempo em que o processo levou para terminar de executar
		return time_end - time_arrival

	def get_response_time(self):
		# O tempo de resposta é dado pela diferença entre o tempo em que o processo chegou na
		# fila de espera e o tempo de sua primeira execução
		return time_start - time_arrival

	def get_waiting_time(self):
		return time_waiting