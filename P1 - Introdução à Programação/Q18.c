#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){

    int fatorial;
    int resposta = 1;

    printf ("Vamos calcular o fatorial de determinado numero inteiro positivo.\n");
    printf ("Para isso, ponha o valor do numero aqui:");
    scanf ("%i", &fatorial);

    if (fatorial < 0){

        printf ("Esse numero nao eh positivo, seu desatento.\n");

    return 1;
    }

        while (fatorial > 0){

        resposta = resposta * fatorial;
        fatorial = fatorial - 1;
    }

    printf ("%i\n", resposta);



return 0;
}
