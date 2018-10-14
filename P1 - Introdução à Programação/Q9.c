#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){

    int a, b, c;

    printf ("Ponha o valor de a aqui:");
    scanf ("%i", &a);

    printf ("Ponha o valor de b aqui:");
    scanf ("%i", &b);

    printf ("Ponha o valor de c aqui:");
    scanf ("%i", &c);

    if ((a == b) && (a == c)){

        printf ("O maior valor eh: %i\n", a);

    return 1;
    }

    if ((a >= b) && (a >= c)){

        printf ("O maior valor eh igual ah: %i\n", a);

    return 2;
    }

    if ((b >= c) && (b >= a)){

        printf ("O maior valor eh igual ah: %i\n", b);

    return 3;
    }

    if ((c >= b) && (c >= a)){

        printf ("O maior valor eh igual ah: %i\n", c);

    return 4;
    }

return 0;

}
