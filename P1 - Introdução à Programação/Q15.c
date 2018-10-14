#include <stdlib.h>
#include <stdio.h>

int main()
{
	int valor, valor_menor;
	valor_menor = 2147483647;
	while (valor != 0)
	{
		printf("Informe um numero:");
		scanf("%i", &valor);
			if (valor != 0)
			{
				if (valor <= valor_menor)
				{
				valor_menor = valor;
				printf("Menor valor: %i\n", valor_menor);
				}
				else	{
					printf("Não eh menor\n");
				}


			}
	}
	printf("Fim - Menor > %i\n", valor_menor);
	return 0;
}
