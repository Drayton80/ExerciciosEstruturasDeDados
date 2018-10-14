#include <stdio.h>
#include <stdlib.h>

int main (void){

    int valor;
    int menor;

    while (valor != 0){

        printf ("Ponha seu numero aqui:");
        scanf ("%i", &valor);

        if (valor != 0){

            if (valor <= menor){

                menor = valor;
                printf ("Menor valor = %i\n", valor);

            }else{

                printf ("Nao ha alteracao no valor.\n");

            }

        }

    }

    printf ("O Processo terminou. Menor valor = %i\n", menor);

return 0;
}
