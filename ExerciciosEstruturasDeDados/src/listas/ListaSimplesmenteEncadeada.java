/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listas;

/**
 *
 * @author drayton80
 */

import exceptions.*;

public class ListaSimplesmenteEncadeada<Generico> {
   //Classe Interna Nó:
    class No{
        private Generico conteudo;
        private No proximo;
        
       //Construtores:
        public No(){
            this.set_proximo(null);
        }
        
        public No(Generico conteudo, No proximo){
            this.conteudo = conteudo;
            this.proximo = proximo;
        }
        
       //Métodos Get e Set:
        public void set_conteudo(Generico conteudo){
            this.conteudo = conteudo;
        }
        
        public void set_proximo(No proximo){
            this.proximo = proximo;
        }
        
        public Generico get_conteudo(){
            return conteudo;
        }
        
        public No get_proximo(){
            return proximo;
        }
    }
    
   //Classe Lista Simplesmente Encadeada:
    private No cabeca;
    private int numero_de_elementos;
    
    public ListaSimplesmenteEncadeada(){
        numero_de_elementos = 0;
        cabeca = null;
    }
    
    public boolean vazia(){
        if(cabeca == null){
            return true;
        }else{
            return false;
        }
    }
    
    public int tamanho(){
        return numero_de_elementos;
    }
    
    public Generico elemento(int posicao) 
            throws ListaVaziaException, PosicaoInvalidaException{
        No auxiliar = cabeca;
        
        if(vazia()){
            throw new ListaVaziaException();
        }
        
        if(posicao <= 0 || numero_de_elementos < posicao){
            throw new PosicaoInvalidaException();
        }else{
            for(int i = 1; i <= numero_de_elementos; i++){
                if(i == posicao){
                    return auxiliar.get_conteudo();
                }else{
                    auxiliar = auxiliar.get_proximo();
                }
            }
        }
        
        return null;
    }
    
}
