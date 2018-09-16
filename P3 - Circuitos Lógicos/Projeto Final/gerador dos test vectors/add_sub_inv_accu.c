#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (void){
    int pg, gg;
    int sel0, sel1, i;
    int c0, bit0, bit1, bit2 , bit3;
    int a[4], b[4], acc[4], s[4];
    int ainv[4];
    int clock = 1;
    int clk = 0;
    int contador = 1;

    for(sel0 = 0; sel0 <= 1; sel0++){
        for(sel1 = 0; sel1 <= 1; sel1++){
            for(bit3 = 0; bit3 <= 1; bit3++){
                for(bit2 = 0; bit2 <= 1; bit2++){
                    for(bit1 = 0; bit1 <= 1; bit1++){
                        for(bit0 = 0; bit0 <= 1; bit0++){
                            int cout;

                            if(clock == 0){
                                clk = 0;
                            }

                            if(clock == 1){
                                clk = 1;
                            }

                            // Entrada do a de 4 bits
                            a[3] = bit3;
                            a[2] = bit2;
                            a[1] = bit1;
                            a[0] = bit0;

                            // Representação do Inversor, como em C 0 é falso e tudo que não seja esse número é true, épossível
                            // utilizar o operador ternário ? : dessa forma.
                            ainv[3] = bit3 ? 0 : 1;
                            ainv[2] = bit2 ? 0 : 1;
                            ainv[1] = bit1 ? 0 : 1;
                            ainv[0] = bit0 ? 0 : 1;

                            // Carry in
                            int carry = sel0;


                            if((sel0 == 0) && (sel1 == 0)){
                                int i;

                                //Representação do Somador
                                for(i = 0; i <= 3; i++){
                                    int p, g;

                                    p = a[i] ^ acc[i];
                                    g = a[i] & acc[i];
                                    carry = g | (p & carry);
                                }

                                s[0] = a[0];
                                s[1] = a[1];
                                s[2] = a[2];
                                s[3] = a[3];
                            }

                            if((sel0 == 0) && (sel1 == 1)){
                                int i;

                                // Somador:
                                for(i = 0; i <= 3; i++){
                                    int p, g;

                                    p = a[i] ^ acc[i];
                                    g = a[i] & acc[i];
                                    s[i] = p ^ carry;
                                    carry = g | (p & carry);
                                }
                            }

                            if((sel0 == 1) && (sel1 == 0)){
                                int i;

                                // Somador:
                                for(i = 0; i <= 3; i++){
                                    int p, g;

                                    p = ainv[i] ^ acc[i];
                                    g = ainv[i] & acc[i];
                                    //s[i] = p ^ carry;
                                    carry = g | (p & carry);
                                }

                                s[0] = ainv[0];
                                s[1] = ainv[1];
                                s[2] = ainv[2];
                                s[3] = ainv[3];
                            }

                            if((sel0 == 1) && (sel1 == 1)){
                                int i;

                                // Somador:
                                for(i = 0; i <= 3; i++){
                                    int p, g;

                                    p = ainv[i] ^ acc[i];
                                    g = ainv[i] & acc[i];
                                    s[i] = p ^ carry;
                                    carry = g | (p & carry);
                                }
                            }

                            cout = carry;
                            // Momento de registro da subida desse clock representativo
                            if(clock == 0){
                                acc[0] = s[0];
                                acc[1] = s[1];
                                acc[2] = s[2];
                                acc[3] = s[3];
                            }


                            // Estados em que o acumulador ainda está em alta impedância, por algum motivo, isso no Quartus apenas
                            // occorre na linha 2
                            if(contador == 2){
                                printf("%i_%i_%i%i%i%i_" , sel0, sel1
                                                         , a[3] , a[2] , a[1], a[0]);
                                //printf("_UUUU__"         , acc[3], acc[2], acc[1], acc[0]);
                                printf("%i%i%i%i_U_%i\n", s[3] , s[2] , s[1], s[0]
                                                         , clk);
                            }else{
                                printf("%i_%i_%i%i%i%i_" , sel0, sel1
                                                         , a[3] , a[2] , a[1], a[0]);
                                //printf("_%i%i%i%i__"     , acc[3], acc[2], acc[1], acc[0]);
                                printf("%i%i%i%i_%i_%i\n", s[3] , s[2] , s[1], s[0]
                                                         , cout, clk);
                            }


                            clock++;
                            contador++;
                            if(clock == 2){
                                clock = 0;
                            }
                        }
                    }
                }
            }
        }
    }


    return 0;
}
