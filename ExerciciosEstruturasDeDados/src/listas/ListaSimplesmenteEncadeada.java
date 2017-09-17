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
        }
        
        //Meu Jeito (Menos Eficiente):
        //for(int i = 1; i <= numero_de_elementos; i++){
        //    if(i == posicao){
        //        return auxiliar.get_conteudo();
        //    }else{
        //        auxiliar = auxiliar.get_proximo();
        //    }
        //}
        
        //Modelo do Professor (Mais Eficiente):
        for(int i = 1; i < posicao; i++){
            auxiliar = auxiliar.get_proximo();
        }

        return auxiliar.get_conteudo();
    }
    
    public int posicao(Generico valor){
        No auxiliar = cabeca;
        
        if(numero_de_elementos == 1 && auxiliar.get_conteudo().equals(valor)){
            return numero_de_elementos; 
        }
        
        for(int i = 1; i < numero_de_elementos; i++){            
            if(auxiliar.get_conteudo().equals(valor)){
                return i;
            }else{
                auxiliar = auxiliar.get_proximo();
            }
        }
        
        //Outra forma de implementação:
        //int contador = 1;
        //
        //while(auxiliar != null){
        //    if(auxiliar.get_conteudo().equals(valor)){
        //        return contador;
        //    }
        //    
        //    auxiliar = auxiliar.get_proximo();
        //    
        //    contador++;
        //}
        
        return -1;
    }
    
    private void insere_no_inicio(Generico valor){
        No novo_no = new No();
        
        novo_no.set_conteudo(valor);
        novo_no.set_proximo(cabeca);
        
        cabeca = novo_no;
        
        numero_de_elementos++;
    }
    
    private void insere_no_meio(int posicao, Generico valor){
        No novo_no  = new No();
        No auxiliar = cabeca;
        
        novo_no.set_conteudo(valor);
        
        for(int i = 1; i < (posicao - 1); i++){
            auxiliar = auxiliar.get_proximo();
        }
        
        if(posicao == numero_de_elementos){
            novo_no.set_proximo(null);
        }else{
            novo_no.set_proximo(auxiliar.get_proximo());
        }

        auxiliar.set_proximo(novo_no);
        
        numero_de_elementos++;
    }
    
    public void insere(int posicao, Generico valor)
            throws OutOfLimitsException, PosicaoInvalidaException{
        
        if(vazia() && posicao != 1){
            throw new PosicaoInvalidaException();
        }
        
        
        if( posicao == 1 ){
            insere_no_inicio(valor);
            
        }else{
            if(posicao < 1 || numero_de_elementos < posicao){
                throw new OutOfLimitsException();
            }
            
            insere_no_meio(posicao, valor);
        }
    }
    
    private Generico remove_no_inicio(){
        No auxiliar = cabeca;
        Generico valor = auxiliar.get_conteudo();
        
        cabeca = auxiliar.get_proximo();
        
        auxiliar.set_proximo(null);
        
        numero_de_elementos--;
        
        return valor;
    }
    
    //private Generico remove_no_meio(int posicao){
    //    
    //}
    //Ainda a ser terminada
}
