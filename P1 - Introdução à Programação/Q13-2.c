#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){

    int natural;
    int acumulador = -1;

    printf ("Ponha seu numero natural aqui:");
    scanf ("%i", &natural);

    if (natural < 0){

        printf ("Seu numero nao pertence ao conjunto dos naturais.\n");

    }

    while ((acumulador != natural) && (acumulador < natural)){

        acumulador ++;

        if (acumulador % 5 == 0){

        printf ("%i\n", acumulador);

        }

    }

return 0;
}
