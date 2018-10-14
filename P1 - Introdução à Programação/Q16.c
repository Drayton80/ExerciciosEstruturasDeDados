#include <stdio.h>
#include <stdlib.h>

int main (void){

    float altura;
    char sexo;
    float pesoH, pesoM;

    printf ("Coloque sua altura aqui (em metros):");
    scanf ("%f", &altura);

    printf ("Ponha seu genero (m para Masculino ou f para Feminino) aqui:");
    scanf (" %[^\n]", &sexo);

    if ((sexo != 'm') && (sexo != 'f')){

        printf ("Voce nao colocou os caracteres corretos, feche e repita novamente.\n");

    return 1;
    }

    if (sexo == 'm'){

        pesoH = 72.7 * altura;
        printf ("Seu peso ideal eh igual ah: %.2f kg\n", pesoH);

    return 1;
    }

    if (sexo == 'f'){

        pesoM = 62.1 * altura;
        printf ("Seu peso ideal eh igual ah: %.2f kg\n", pesoM);

    return 2;
    }



return 0;
}
