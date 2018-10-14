#include <stdio.h>
#include <stdlib.h>

int main (void){

    int x, y, z;
    int soma, produto;

    printf ("Insira aqui o valor de x:");
    scanf ("%i", &x);
    printf ("Insira aqui o valor de y:");
    scanf ("%i", &y);
    printf ("Insira aqui o valor de z:");
    scanf ("%i", &z);

    soma = x + y + z;
    produto = x * y * z;

    printf ("Soma eh igual ah: %i \n", soma);
    printf ("Produto eh igual ah: %i \n", produto);

return 0;
}
