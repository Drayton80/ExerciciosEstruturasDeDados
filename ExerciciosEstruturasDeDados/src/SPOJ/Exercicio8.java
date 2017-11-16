/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package SPOJ;

import static java.lang.System.out;
import java.util.Scanner;

/**
 * @author drayton80
 */

public class Exercicio8 {
    static class ABP {
        
        static class No {
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
    
     
        private No raiz;
        private int saida;

        public ABP(){
            saida = 0;
            raiz = null;
        }

        public int get_saida(){
            return saida;
        }

        /** Verifica se a árvore está vazia */
        public boolean vazia(){
                return (raiz == null);
        }

        /**Buscar recursivamente a partir da raiz.
            Retorna o endereço se o elemento for
            encontrado, caso contrário retorna NULL*/
        private No busca(No T, int valor) {
                if (T == null)
                        return null;  // Arvore Vazia

                if(T.getConteudo() == valor)
                        return T; 	// Elem. encontrado na raiz

                if (valor < T.getConteudo())
                        return busca(T.getEsq(), valor);
            else
                        return busca(T.getDir(), valor);
        }

        /**Buscar um elemento na ABP
                Retorna o endereço se o elemento for
                encontrado, caso contrário retorna NULL*/
        public No busca(int valor) {          
                if (raiz != null) 
                        return busca(raiz, valor);
                return null;
        }


        /**Exibe o conteúdo de uma árvore no formato in-ordem
            (preserva a ordenação)*/
        private void exibe (No T){
                if (T != null) {
                        exibe(T.getEsq());
                        System.out.print(" " + T.getConteudo());
                        exibe(T.getDir());
                }
        }

        public void exibe() {
                if (raiz == null)
                        System.out.println("Arvore vazia");
                else
                        exibe(raiz);
        }

        /**Insere um nó em uma árvore ABP
            Retorna 1 se a inserção for com sucesso.
            Caso contrário retorna 0*/
        public boolean insere(int valor){

                No novoNo = new No();
                novoNo.setConteudo(valor);
                novoNo.setEsq(null);
                novoNo.setDir(null);

                if (raiz == null){ // Arvore vazia
                        raiz = novoNo;
                        return true;
                }

            // Procura a posicao correta pra inserir o novo no
            No aux = raiz;
            No p = null;
            while (aux != null) {
                        p = aux;
                        if (valor < aux.getConteudo()){
                                aux = aux.getEsq();
                                saida++;
                        }else{
                                aux = aux.getDir();
                                saida++;
                        }
                }

                // Encontrou um nó folha para inserir
                if (valor < p.getConteudo()){
                        p.setEsq(novoNo);
                }else{
                        p.setDir(novoNo);
                }
                return true;
        }
    }

    public static void main(String[] arguments){
        Scanner scan = new Scanner(System.in);
        ABP arvore = new ABP();
        int valores_entrada, numero_elementos;
        
        numero_elementos = Integer.parseInt(scan.nextLine());
        
        if(numero_elementos > 300000) return;
   
        for(int i = 0; i < numero_elementos; i++){
            valores_entrada = Integer.parseInt(scan.nextLine());
            
            arvore.insere(valores_entrada);
            
            out.println(arvore.get_saida());
        }   
    }
}