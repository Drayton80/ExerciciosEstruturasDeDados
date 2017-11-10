/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package SPOJ;

import java.util.Scanner;

/**
 * @author drayton80
 */

public class Exercicio6 {
    public static class No {
        private int conteudo;
        private No esq;
        private No dir;

        public No(){
            esq = null;
            dir = null;
        }

        public int getConteudo() {
            return conteudo;
        }
        public void setConteudo(int conteudo) {
                this.conteudo = conteudo;
        }

        public No getEsq() {
            return esq;
        }
        public void setEsq(No esq) {
            this.esq = esq;
        }

        public No getDir() {
            return dir;
        }

        public void setDir(No dir) {
            this.dir = dir;
        }
    }
    
    public static class ArvBin {
        public static int indice = 0;

        // Há parametros de inicio e fim por causa da recursão 
        public No construir_arvore(int[] pre_order, int[] in_order, int inicio_in_order, int fim_in_order){
            No no = new No();
            
            // Condições de parada:
            if (inicio_in_order > fim_in_order){
                return null;
            }
                
            no.setConteudo(pre_order[indice++]);

            if (inicio_in_order == fim_in_order){
                return no;
            }

            int indice_do_valor = fim_in_order;
            
            for (int i = inicio_in_order; i <= fim_in_order; i++){
                if (in_order[i] == no.getConteudo()){
                    indice_do_valor = i;
                    break;
                }
            }
            
            // Caso recursivo:
            no.setEsq(construir_arvore(pre_order, in_order, inicio_in_order, indice_do_valor - 1));
            no.setDir(construir_arvore(pre_order, in_order, indice_do_valor + 1, fim_in_order   ));
            
            return no;
        }
        
        public No raiz;

        public ArvBin(){
                raiz = null;
        }

        /** Verifica se a árvore está vazia */
        public boolean vazia (){
                return (raiz == null);
        }
        
        private String gera_pos_order(No T) {
            String aux = "";
            
            if (T == null){
                return "";
            }

            if (T.getEsq() != null){
                aux = aux + gera_pos_order(T.getEsq());
                //System.out.println(aux);
                
            }
                
            if (T.getDir() != null){
                aux = aux + gera_pos_order(T.getDir());
                //System.out.println(aux);
            }
            
            return String.valueOf(aux + " " + T.getConteudo());
        }
        
        public String gera_pos_order() {
            return gera_pos_order(raiz);
        }
        
        // É uma operação perigosa, mas para esse caso é bem funcional
        public void set_raiz(No nova_raiz){
            this.raiz = nova_raiz;
        }

    }
    
    public static void main(String[] arguments){
        try{    
            ArvBin arvore = new ArvBin();
            Scanner scan = new Scanner(System.in);
            String pre_com_espacos, pos_com_espacos, in_com_espacos;
            String[] pre_sem_espacos, pos_sem_espacos, in_sem_espacos;
            int numero_elementos;
            boolean comparacao_de_elementos = false;
            boolean todos_nos_iguais = false;
            int[] valores_pre_order, valores_in_order, valores_pos_order;  

            numero_elementos = Integer.parseInt(scan.nextLine());
            if(numero_elementos == 0){
                System.out.println("no");
                System.exit(0);
            }
            
            valores_pre_order = new int[numero_elementos];
            valores_in_order  = new int[numero_elementos];
            valores_pos_order = new int[numero_elementos];

            pre_com_espacos = scan.nextLine();
            pre_sem_espacos = pre_com_espacos.split(" ");
            pos_com_espacos = scan.nextLine();
            pos_sem_espacos = pos_com_espacos.split(" ");
            in_com_espacos = scan.nextLine();
            in_sem_espacos = in_com_espacos.split(" ");

            for(int i = 0; i < numero_elementos; i++){
                valores_pre_order[i] = Integer.parseInt(pre_sem_espacos[i]);
                valores_in_order[i]  = Integer.parseInt(in_sem_espacos[i]);
                valores_pos_order[i] = Integer.parseInt(pos_sem_espacos[i]);
                
                todos_nos_iguais = pre_sem_espacos[i].equals(pos_sem_espacos[i]) &&
                                   pre_sem_espacos[i].equals(in_sem_espacos[i])  &&
                                   pos_sem_espacos[i].equals(in_sem_espacos[i]);
            }
            
            int indice = compara_pos_orders(valores_pos_order, 0, arvore.raiz);
            comparacao_de_elementos = (valores_in_order.length == indice);
            
            // Usei primeiro o in order e o pre order para montar montar uma árvore temporário. Em seguida, a raiz
            // da árvore é trocada pela raiz da árvore temporária
            arvore.set_raiz(arvore.construir_arvore(valores_pre_order, valores_in_order, 0, numero_elementos - 1));

            String pos_order_arvore_com_espacos = arvore.gera_pos_order();
            // Elimina o espaço que vem junto dele devido a exibição do gera_pos_order
            pos_order_arvore_com_espacos = pos_order_arvore_com_espacos.substring(1); 
            String[] pos_order_sem_espacos = pos_order_arvore_com_espacos.split(" ");
            //System.out.println(pos_order_arvore);
            
            
            //for(int i = 0; i < pos_order_sem_espacos.length; i++){                         
            //    if(pos_order_sem_espacos[i].equals(pos_sem_espacos[i])){
            //        comparacao_de_elementos = true;
            //    }else{
            //        comparacao_de_elementos = false;
            //        System.out.println("no");
            //        break;
            //    }
            //}
            //
            //if(comparacao_de_elementos){
            //    System.out.println("yes");
            //}
            
            if(comparacao_de_elementos || !todos_nos_iguais){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }
            
            //// Aqui eu adiciono um espaço pois, pela forma como fiz o return do gera_pos_order, a string em sequência
            //// da pos ordem sempre vem com um espaçoa à mais no início.
            //if(todos_nos_iguais){
            //    System.out.println("no");
            //}else if(pos_order_arvore_com_espacos ){
            //    System.out.println("yes");
            //}else{
            //    System.out.println("no");
            //}
            
        }catch(Exception e){
            System.out.print(e);
        }
        
    }
    
    static int compara_pos_orders(int[] pos_order, int i, No no){
        if(no == null){
            return i;
        }
        
        i = compara_pos_orders(pos_order, i, no.getEsq());
        i = compara_pos_orders(pos_order, i, no.getDir());
        
        if(no.getConteudo() == pos_order[i]){
            i++;
        }else{
            System.out.println("no");
            System.exit(0);
        }
        
        return i;
    }
}