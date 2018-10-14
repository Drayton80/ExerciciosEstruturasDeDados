#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){

    float x, y, z;
    float A, B, C;
    float x1, x2;
    float delta;

    printf ("Vamos calcular as raizes de uma equacao de segundo agora.\n");

    printf ("Para isso, ponha seu A aqui:");
    scanf ("%f", &A);
    printf ("Seu B aqui:");
    scanf ("%f", &B);
    printf ("e seu C aqui:");
    scanf ("%f", &C);

    delta = B*B - 4*A*C;

    if (A == 0){

        printf ("Desculpe, mas essa nao eh uma equacao de segundo grau.\n");

    return 1;
    }

    if (delta < 0){

        printf ("As raizes nao sao numeros Reais.\n");

    return 2;
    }

    x1 = (-B + sqrtf(delta))/ (2 * A);
    x2 = (-B - sqrtf(delta))/ (2 * A);

    if (x1 == x2){

        printf ("X' = X'' = %.2f\n", x1);

    }else{

        printf ("X' = %.2f\ne \nX'' = %.2f\n", x1, x2);

    }

return 0;
}
