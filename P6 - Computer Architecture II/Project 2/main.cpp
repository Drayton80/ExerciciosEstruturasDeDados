#include <iostream>
#include <array>
#include <cstdlib>
#include <chrono>
#include <fstream>
#include <omp.h>

using namespace std;

int const data_size = 1400;


void original(){
	// Cria duas variáveis para guardarem o tempo do sistema:
	std::chrono::time_point<std::chrono::system_clock> time_start, time_end; 
	
	// Definição alternativa de um array bidimensional em C++ para 
	// possibilitar o uso de size e outras funções úteis:
	std::array< std::array<float, data_size> , data_size> fake_data;
	
	// Preenche a matriz com diversos valores aleatórios:
	for(int i = 0; i < fake_data.size(); i++){
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = rand();
		}
	}
	
	// Valor inicial do tempo:
	time_start = std::chrono::system_clock::now();
	
	// Normalização de valores:
	for(int i = 0; i < fake_data.size(); i++){
		// Como aqui já é pego os primeiros elementos
		// para serem feitas as comparações, os loops
		// a segior irão começar no segundo elemento,
		// ou seja, no elemento de índice número 1
		int biggest_column_value  = fake_data[i][0];
		int smallest_column_value = fake_data[i][0];

		// É pego o maior valor de toda uma coluna:
		for(int j = 1; j < fake_data[0].size(); j++){
			if(biggest_column_value < fake_data[i][j]){
				biggest_column_value = fake_data[i][j];
			}
		}
		// e o menor valor da mesma coluna:
		for(int j = 1; j < fake_data[0].size(); j++){
			if(fake_data[i][j] < smallest_column_value){
				smallest_column_value = fake_data[i][j];
			}
		}

		// Aplica-se a fórmula da normalização utilizando
		// o menor e maior valor de determinada coluna:
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = (fake_data[i][j]      - smallest_column_value)/ 
                              (biggest_column_value - smallest_column_value);
		}
	}

	// Valor final do tempo:
	time_end = std::chrono::system_clock::now();
	// Salva o tempo decorrido em elapsed_time:
	std::chrono::duration<double> elapsed_time = time_end - time_start;

	// Abre-se um arquivo referenciado por file indicando que será 
	// usado no modo de inserção no fim (append, resumido aqui como "app"):
	ofstream file("times_original.txt", ios::app);
	// Salva no arquivo a linha indicada abaixo:
	file << data_size << " " << elapsed_time.count() << endl;
}


void optimized(){
	// Cria duas variáveis para guardarem o tempo do sistema:
	std::chrono::time_point<std::chrono::system_clock> time_start, time_end; 

	// Definição alternativa de um array bidimensional em C++ para 
	// possibilitar o uso de size e outras funções úteis:
	std::array< std::array<float, data_size> , data_size> fake_data;
	
	// Preenche a matriz com diversos valores aleatórios:
	for(int i = 0; i < fake_data.size(); i++){
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = rand();
		}
	}
	
	// Valor inicial do tempo:
	time_start = std::chrono::system_clock::now();
	
	// Normalização de valores:
	for(int i = 0; i < fake_data.size(); i++){
		// Como aqui já é pego os primeiros elementos
		// para serem feitas as comparações, os loops
		// a segior irão começar no segundo elemento,
		// ou seja, no elemento de índice número 1
		int biggest_column_value  = fake_data[i][0];
		int smallest_column_value = fake_data[i][0];

		// FUSÃO DE LOOPS:
		// É pego o maior valor de toda uma coluna:
		// e o menor valor da mesma coluna
		for(int j = 1; j < fake_data[0].size(); j++){
			if(biggest_column_value < fake_data[i][j]){
				biggest_column_value = fake_data[i][j];
			}

			if(fake_data[i][j] < smallest_column_value){
				smallest_column_value = fake_data[i][j];
			}
		}

		// Aplica-se a fórmula da normalização utilizando
		// o menor e maior valor de determinada coluna:
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = (fake_data[i][j]      - smallest_column_value)/ 
                              (biggest_column_value - smallest_column_value);
		}
	}

	// Valor final do tempo:
	time_end = std::chrono::system_clock::now();
	// Salva o tempo decorrido em elapsed_time:
	std::chrono::duration<double> elapsed_time = time_end - time_start;

	// Abre-se um arquivo referenciado por file indicando que será 
	// usado no modo de inserção no fim (append, resumido aqui como "app"):
	ofstream file("times_optimized.txt", ios::app);
	// Salva no arquivo a linha indicada abaixo:
	file << data_size << " " << elapsed_time.count() << endl;
}


void parallelized(){
	//const int number_of_threads = omp_get_max_threads();
	//std::cout << "OpenMP running with " << number_of_threads << " threads" << std::endl;

	// Cria duas variáveis para guardarem o tempo do sistema:
	std::chrono::time_point<std::chrono::system_clock> time_start, time_end; 
	
	// Definição alternativa de um array bidimensional em C++ para 
	// possibilitar o uso de size e outras funções úteis:
	std::array< std::array<float, data_size> , data_size> fake_data;
	
	// Preenche a matriz com diversos valores aleatórios:
	for(int i = 0; i < fake_data.size(); i++){
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = rand();
		}
	}
	
	// Valor inicial do tempo:
	time_start = std::chrono::system_clock::now();
	
	// Comando paralelizar um for:
	#pragma omp parallel for
	for(int i = 0; i < fake_data.size(); i++){
		// Como aqui já é pego os primeiros elementos
		// para serem feitas as comparações, os loops
		// a segior irão começar no segundo elemento,
		// ou seja, no elemento de índice número 1
		int biggest_column_value  = fake_data[i][0];
		int smallest_column_value = fake_data[i][0];

		// É pego o maior valor de toda uma coluna:
		for(int j = 1; j < fake_data[0].size(); j++){
			if(biggest_column_value < fake_data[i][j]){
				biggest_column_value = fake_data[i][j];
			}
		}
		// e o menor valor da mesma coluna:
		for(int j = 1; j < fake_data[0].size(); j++){
			if(fake_data[i][j] < smallest_column_value){
				smallest_column_value = fake_data[i][j];
			}
		}

		// Aplica-se a fórmula da normalização utilizando
		// o menor e maior valor de determinada coluna:
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = (fake_data[i][j]      - smallest_column_value)/ 
                              (biggest_column_value - smallest_column_value);
		}
	}


	// Valor final do tempo:
	time_end = std::chrono::system_clock::now();
	// Salva o tempo decorrido em elapsed_time:
	std::chrono::duration<double> elapsed_time = time_end - time_start;

	// Abre-se um arquivo referenciado por file indicando que será 
	// usado no modo de inserção no fim (append, resumido aqui como "app"):
	ofstream file("times_parallelized.txt", ios::app);
	// Salva no arquivo a linha indicada abaixo:
	file << data_size << " " << elapsed_time.count() << endl;
}


void optimized_and_parallelized(){
	// Cria duas variáveis para guardarem o tempo do sistema:
	std::chrono::time_point<std::chrono::system_clock> time_start, time_end; 

	// Definição alternativa de um array bidimensional em C++ para 
	// possibilitar o uso de size e outras funções úteis:
	std::array< std::array<float, data_size> , data_size> fake_data;
	
	// Preenche a matriz com diversos valores aleatórios:
	for(int i = 0; i < fake_data.size(); i++){
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = rand();
		}
	}
	
	// Valor inicial do tempo:
	time_start = std::chrono::system_clock::now();
	
	// Comando para paralelizar parte do programa:
	// Normalização de valores:
	#pragma omp parallel for
	for(int i = 0; i < fake_data.size(); i++){
		// Como aqui já é pego os primeiros elementos
		// para serem feitas as comparações, os loops
		// a seguir irão começar no segundo elemento,
		// ou seja, no elemento de índice número 1
		int biggest_column_value  = fake_data[i][0];
		int smallest_column_value = fake_data[i][0];

		// FUSÃO DE LOOPS:
		// É pego o maior valor de toda uma coluna:
		// e o menor valor da mesma coluna
		for(int j = 1; j < fake_data[0].size(); j++){
			if(biggest_column_value < fake_data[i][j]){
				biggest_column_value = fake_data[i][j];
			}

			if(fake_data[i][j] < smallest_column_value){
				smallest_column_value = fake_data[i][j];
			}
		}

		// Aplica-se a fórmula da normalização utilizando
		// o menor e maior valor de determinada coluna:
		for(int j = 0; j < fake_data[0].size(); j++){
			fake_data[i][j] = (fake_data[i][j]      - smallest_column_value)/ 
                              (biggest_column_value - smallest_column_value);
		}
	}

	// Valor final do tempo:
	time_end = std::chrono::system_clock::now();
	// Salva o tempo decorrido em elapsed_time:
	std::chrono::duration<double> elapsed_time = time_end - time_start;

	// Abre-se um arquivo referenciado por file indicando que será 
	// usado no modo de inserção no fim (append, resumido aqui como "app"):
	ofstream file("times_optimized_and_parallelized.txt", ios::app);
	// Salva no arquivo a linha indicada abaixo:
	file << data_size << " " << elapsed_time.count() << endl;
}


int main(){
	original();
	optimized();
	parallelized();
	optimized_and_parallelized();
}