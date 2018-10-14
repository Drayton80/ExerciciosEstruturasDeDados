#include <stdio.h>
#include <stdlib.h>

int main (void){

    float polegada;
    float centimetro;

    printf ("Vamos transformar polegadas em centimetros?\n");
    printf ("Ponha seu valor, em polegadas, aqui:");
    scanf ("%f", &polegada);

    centimetro = polegada * 2.54;

    printf ("Seu valor, em centimetros, eh igual ah: %.3f cm\n", centimetro);

    return 0;

}
