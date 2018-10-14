#include <stdio.h>
#include <stdlib.h>

int main (void){

    int idade;

    printf ("Ponha sua idade aqui:");
    scanf ("%i", &idade);


    if (idade < 18){

        printf("Ce eh Crianço, meu jovenzito.\n");

    return 4;
    }

    if ((idade >= 18) && (idade < 24)){

        printf ("Voce eh Jovem, meu jovem.\n");

    return 1;
    }

    if ((idade >= 24) && (idade < 65)){

        printf ("Voce eh adulto, meu caro.\n");

    return 2;
    }

    if (idade >= 65){

        printf ("Voce eh Idoso, meu velho.\n");

    return 5;
    }


return 0;
}
