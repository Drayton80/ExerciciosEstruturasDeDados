#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){

    float a, b;

    printf ("Ponha o valor de a aqui:");
    scanf ("%f", &a);
    printf ("Ponha o valor de b aqui:");
    scanf ("%f", &b);

    if (a == b){

        printf ("O menor valor eh igual ah: %f", a);

    }else{

        if (a < b){

            printf ("O menor valor eh igual ah: %f", a);

        }else{

            printf ("O menor valor eh igual ah: %f", b);

        }
    }

return 0;
}
