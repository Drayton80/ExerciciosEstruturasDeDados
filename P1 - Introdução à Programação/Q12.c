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

        acumulador ++;                  //O ++ serve para adicionar de um em um ao valor.
        printf ("%i", acumulador);

        if (acumulador %2 == 0){        //Se, ao dividir por zero, o resto é igual à 2, ou seja, um par.

            printf ("(Par)\n");

        }else{

            printf ("(Impar)\n");

        }

    }

return 0;
}
