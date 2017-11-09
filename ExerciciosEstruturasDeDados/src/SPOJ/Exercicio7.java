package SPOJ;

import java.util.Scanner;

/**
 * @author drayton80
 */

public class Exercicio7{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int profundidade_auxiliar, numero_de_arvores;
        int profundidade;
        char[] nos_da_arvore;
        boolean[] sequencia_de_checagens;

        numero_de_arvores = Integer.parseInt (scan.nextLine());

        for(; numero_de_arvores >= 1; numero_de_arvores--){
            String no = scan.nextLine();
            
            // Se o primeiro for uma folha, profundidade é igual a 0
            if (no.equals("l")) {
                profundidade = 0;
                System.out.println(profundidade);

            // Se isso não ocorrer, checa qual a profundidade
            }else{
                profundidade_auxiliar = 0;
                profundidade = 0;
                
                sequencia_de_checagens = new boolean [no.length()];
                sequencia_de_checagens[0] = true;

                nos_da_arvore = new char[no.length()];

                for(int i = 0; i < no.length(); i++){
                    nos_da_arvore[i] = no.charAt(i);
                }

                for (int i = 0; i < nos_da_arvore.length; i++) {
                    if (nos_da_arvore[i] == 'n'){
                        // A cada nó que não seja uma folha (um ramo, talvez?) adiciona true na sequencia
                        profundidade_auxiliar++;
                        sequencia_de_checagens[profundidade_auxiliar] = true;
                    }else{
                        // Cada folha transforma em false um boolean da sequencia que representa um ramo
                        while(sequencia_de_checagens[profundidade_auxiliar] != true){
                            profundidade_auxiliar--;
                        }
                        sequencia_de_checagens[profundidade_auxiliar] = false;
                    }
                    
                    // Retorna qual profundidade for maior
                    if(profundidade_auxiliar > profundidade){
                        profundidade = profundidade_auxiliar;
                    }
                    
                }
                
                System.out.println(profundidade);
                
            }
            
        }
        
    }
    
}