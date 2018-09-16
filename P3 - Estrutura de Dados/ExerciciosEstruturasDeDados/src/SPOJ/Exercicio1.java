package SPOJ;

import java.util.Arrays;
import java.util.Scanner;
import listas.*;

/**
 *
 * @author drayton80
 */
public class Exercicio1 {
    public static void main(String[] arguments){
        Scanner entrada = new Scanner(System.in);
        int[] valores_s, valores_q;
        int sn, qm, contador = 0;
        int[] valores_diferentes;
        boolean possui_igual;
        String exibicao_dos_diferentes = "";
        
        sn = Integer.parseInt(entrada.nextLine());
        valores_s = new int[sn];
        String valores_s_com_espacos = entrada.nextLine();
        String[] valores_s_sem_espacos = valores_s_com_espacos.split(" ");
        
        for(int i = 0; i < valores_s_sem_espacos.length; i++){
            valores_s[i] = Integer.parseInt(valores_s_sem_espacos[i]);
        }
        
        qm = Integer.parseInt(entrada.nextLine());
        valores_q = new int[qm];
        String valores_q_com_espacos = entrada.nextLine();
        String[] valores_q_sem_espacos = valores_q_com_espacos.split(" ");
        
        for(int i = 0; i < valores_q_sem_espacos.length; i++){
            valores_q[i] = Integer.parseInt(valores_q_sem_espacos[i]);
        }
        
        /* O máximo que o tamanho do array de valores diferentes pode ter é o tamanho
           da soma dos dois arrays comparados, pois, nesse caso, todos os números de
           ambos os arrays seriam diferentes. */
        //valores_diferentes = new int[(sn+qm)];
        
        /* Erro de interpretação meu, é mais fácil do que eu pensava, o teste não
         * não é em diferença de ambos, mas apenas de um em relação ao outro.
         */
        valores_diferentes = new int[sn];
        
        for(int i = 0; i < valores_s.length; i++){
            possui_igual = false;
            
            for(int j = 0; j < valores_q.length; j++){
                if(valores_s[i] == valores_q[j]){
                    possui_igual = true;
                }
            }
            
            if(possui_igual != true){
                valores_diferentes[contador] = valores_s[i];
                contador++;
            }
        }
        
        //for(int i = 0; i < valores_q.length; i++){
        //    possui_igual = false;
        //    
        //    for(int j = 0; j < valores_s.length; j++){
        //        if(valores_q[i] == valores_s[j]){
        //            possui_igual = true;
        //        }
        //    }
        //    
        //    if(possui_igual != true){
        //        valores_diferentes[contador] = valores_q[i];                
        //        contador++;
        //    }
        //}
        
        /* O Arrays.sort ordena em ordem crescente. Os dois ultimos parametros
         * definem o limite da ordenação. Se não fosse limitado, os 0 que completam
         * o restante do Array iriam ser os únicos a aparecer no exibição_dos_diferentes
         */
        Arrays.sort(valores_diferentes, 0, (contador-1));

        
        for(int i = 0; i < contador; i++){
            if(i == 0){
                exibicao_dos_diferentes += String.valueOf(valores_diferentes[i]);
            }else{
                exibicao_dos_diferentes += " " + String.valueOf(valores_diferentes[i]);
            }
        }
        
        System.out.println(exibicao_dos_diferentes);
    }
    
    //Compara dois inteiros e retorna o maior, se os dois forem iguais, retorna
    //qualquer um dos dois.
    //private static int compara(int p, int q){
    //    if(p > q){
    //        return p;
    //    }else{
    //        return q;
    //    }
    //}
}
