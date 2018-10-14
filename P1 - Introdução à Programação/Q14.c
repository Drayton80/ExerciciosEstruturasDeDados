#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){

    float Raio, Raio2;
    float Area, Area2;
    float pi = 3.14;

    printf ("Vamos calcular a area do seu circulo :3\n");
    printf ("Para isso, basta por o valor do raio dele aqui:");
    scanf ("%f", &Raio);

    Area = Raio*Raio * pi;
    printf ("Sua area eh igual ah: %.2f\n\n", Area);

    if (Raio == 0){

        printf ("Esse eh o codigo para sair, obrigado pela sua atencao e volte sempre.\n\n");

        return 1;

    }

    while (Raio2 != 0){

        printf ("Caso queira calcular outra area, ponha o valor do novo raio aqui:");
        scanf ("%f", &Raio2);

        Area2 = Raio2*Raio2 * pi;

        printf ("Sua nova area eh igual ah: %.2f\n\n", Area2);

        if (Raio2 != 0){

            printf ("Para sair, coloque o valor do novo raio = 0\n\n");

        }

    }


return 0;
}
