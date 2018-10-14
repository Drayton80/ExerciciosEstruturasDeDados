#include <stdio.h>
#include <stdlib.h>

int main (void){

    float pi = 3.14;
    float Area;
    float Raio;

    printf ("Vamos calcular a area de seu circulo.\n");
    printf ("Para isso ponha o raio dele aqui:");
    scanf ("%f", &Raio);

    Area = pi * (Raio * Raio);

    printf ("Sua area eh igual a: %.2f", Area);

    return 0;
}
