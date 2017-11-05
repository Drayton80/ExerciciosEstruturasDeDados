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
    public static class ArvBin {
        public static int indice = 0;
        
        public class No {
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
        
        private No raiz;

        public ArvBin(){
                raiz = null;
        }

        /** Verifica se a árvore está vazia */
        public boolean vazia (){
                return (raiz == null);
        }

        /** Funcao de busca recursiva.
                Retorna o endereço do elemento se ele for encontrado.
                Caso contrario, retorna null*/
        private No busca(No T, int valor) {          
                No aux;

                // Condicao de parada
                if (T == null) 
                        return null;  // Arvore Vazia

                // Condicao de parada
                if(T.getConteudo() == valor) 
                        return T; //Elem. encontrado na raiz

                // Caso recursivo
                aux = busca(T.getEsq(), valor);
                if (aux == null) 
                        aux = busca(T.getDir(), valor);

                return aux;
        }

        /** Buscar um elemento na árvore
                Retorna o endereço se o elemento for encontrado, 
                Caso contrário retorna NULL*/
        public No busca(int valor) {          
                if (vazia())
                        return null;

                //No res = busca(raiz, valor);
                //return res;
                return busca(raiz, valor);
        }


        /** Insere um nó raiz em uma árvore vazia 
                Retorna true se a inserção for com sucesso.
                Caso contrário, retorna false */   
        public boolean insereRaiz(int valor) {   
                if (raiz != null) 
                        return false;  //Erro: Arvore não está vazia

                No novoNo = new No();
                novoNo.setConteudo(valor);
                novoNo.setEsq(null);
                novoNo.setEsq(null);

                raiz = novoNo;
                return true;
        }   

        /** Insere um filho à direita de um dado nó.
                Retorna true se a inserção for com sucesso,
                Caso contrário false  */
        public boolean insereDir(int vPai, int vFilho ) {

                // Verifica se o elemento já existe
                No filho = busca(vFilho);
                if (filho != null)
                return false;  // Err: dado já existe

                // Busca o pai e verifica se possui filho direito
                No pai = busca(vPai);
                if (pai == null)
                        return false;  // Err: pai não encontrado

                if (pai.getDir() != null)
                        return false;  // Err: filho dir já existe

                No novoNo = new No();
                novoNo.setConteudo(vFilho);
                novoNo.setEsq(null);
                novoNo.setDir(null);

                pai.setDir(novoNo);

                return true;
        }

        /** Insere um filho à esquerda de um dado nó.
                Retorna true se a inserção for com sucesso,
                Caso contrário false  */
        public boolean insereEsq(int vPai, int vFilho ) {

                // Verifica se o elemento já existe 
                No filho = busca(vFilho);
                if (filho != null)
                return false;  // Err: dado já existe

                // Busca o pai e verifica se possui filho da esq
                No pai = busca(vPai);
                if (pai == null)
                        return false; // Err: pai não encontrado

                if (pai.getEsq() != null)
                        return false; // Err: filho esq já existe

                No novoNo = new No();
                novoNo.setConteudo(vFilho);
                novoNo.setEsq(null);
                novoNo.setDir(null);

                pai.setEsq(novoNo);
                return true;
        }

        /** Exibe o conteúdo de uma árvore em pré-ordem*/
        private void exibePreOrdem(No T) {
                if (T == null)
                        return;

                System.out.print(" " + T.getConteudo());
                if (T.getEsq() != null)
                        exibePreOrdem(T.getEsq());

                if (T.getDir() != null)
                        exibePreOrdem(T.getDir());
        }

        /** Exibe o conteúdo de uma árvore em pré-ordem*/
        public void exibePreOrdem() {
                if (raiz == null)
                        System.out.println("Arvore vazia");
                else
                        exibePreOrdem(raiz);
        }	


        /** Exibe o conteúdo de uma árvore em pré-ordem*/
        private void exibeInOrdem(No T) {
                if (T == null)
                        return ;

                if (T.getEsq() != null)
                        exibeInOrdem(T.getEsq());

            System.out.print(" " + T.getConteudo());

                if (T.getDir() != null)
                        exibeInOrdem(T.getDir());
        }


        /** Exibe o conteúdo de uma árvore em pré-ordem*/
        public void exibeInOrdem() {
                if (raiz == null)
                        System.out.println("Arvore vazia");
                else
                        exibeInOrdem(raiz);
        }	

        /** Exibe o conteúdo de uma árvore em pré-ordem*/
        private void exibePosOrdem(No T) {
                if (T == null)
                        return ;

                if (T.getEsq() != null)
                        exibePosOrdem(T.getEsq());
                

                if (T.getDir() != null)
                        exibePosOrdem(T.getDir());

                System.out.print(" " + T.getConteudo());
        }

        /** Exibe o conteúdo de uma árvore em pré-ordem*/
        public void exibePosOrdem() {
                if (raiz == null)
                        System.out.println("Arvore vazia");
                else
                        exibePosOrdem(raiz);
        }
        
        private String gera_pos_order(No T) {
            String aux = "";
            
            if (T == null){
                return aux;
            }

            if (T.getEsq() != null){
                aux = aux + gera_pos_order(T.getEsq());
                //System.out.println(aux);
                
            }
                
            if (T.getDir() != null){
                aux = aux + gera_pos_order(T.getDir());
                //System.out.println(aux);
            }
            
            System.out.println(aux);
            return String.valueOf(T.getConteudo()) + " ";
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
        ArvBin arvore = new ArvBin();
        Scanner scan = new Scanner(System.in);
        String pre_com_espacos, pos_com_espacos, in_com_espacos;
        String[] pre_sem_espacos, pos_sem_espacos, in_sem_espacos;
        int numero_elementos;
        int[] valores_pre_order, valores_pos_order, valores_in_order;  
        
        numero_elementos = Integer.parseInt(scan.nextLine());
        valores_pre_order = new int[numero_elementos];
        valores_pos_order = new int[numero_elementos];
        valores_in_order = new int[numero_elementos];
        
        pre_com_espacos = scan.nextLine();
        pre_sem_espacos = pre_com_espacos.split(" ");
        pos_com_espacos = scan.nextLine();
        pos_sem_espacos = pos_com_espacos.split(" ");
        in_com_espacos = scan.nextLine();
        in_sem_espacos = in_com_espacos.split(" ");
        
        for(int i = 0; i < numero_elementos; i++){
            valores_pre_order[i] = Integer.parseInt(pre_sem_espacos[i]);
            valores_pos_order[i] = Integer.parseInt(pos_sem_espacos[i]);
            valores_in_order[i]  = Integer.parseInt(in_sem_espacos[i]);
        }
        
        // Usei primeiro o in order e o pre order para montar montar uma árvore temporário. Em seguida, a raiz
        // da árvore é trocada pela raiz da árvore temporária
        arvore.set_raiz(arvore.construir_arvore(valores_pre_order, valores_in_order, 0, numero_elementos - 1));
        
        arvore.exibePosOrdem();
        
        // Depois comparo o pos order lançado pela arvore com o post order pego como entrada
        String pos_order_arvore = arvore.gera_pos_order();
        System.out.println(pos_order_arvore);
        
        if(pos_order_arvore.equals(" " + pos_com_espacos + " ")){
            System.out.print("yes");
        }else{
            System.out.print("no");
        }
        
        
        
        
        
    }
    
}
