package SPOJ;

import java.util.Scanner;
import java.util.*;

/**
 *
 * @author drayton80
 */

public class Exercicio5 {
    public static class No<Tipo> {
        private No ant;
        private Tipo conteudo;
        private No prox;

        public No(){
                setProx(null);
        }

        public Tipo getConteudo() {
                return conteudo;
        }

        public void setConteudo(Tipo conteudo) {
                this.conteudo = conteudo;
        }

        public No getProx() {
                return prox;
        }

        public void setProx(No prox) {
                this.prox = prox;
        }

        public No getAnt() {
                return ant;
        }

        public void setAnt(No ant) {
                this.ant = ant;
        }
    }
    
    public static class PilhaEnc<Tipo> {
        No topo;
        int nElementos;

        public PilhaEnc(){
                topo = null;
                nElementos = 0;
        }

        /** Verifica se a Pilha está vazia*/
        public boolean vazia () {
            if (nElementos == 0)
                return true;
            else
                return false;
        }

        /** Obtém o tamanho da Pilha*/
        public int tamanho() {
            return nElementos;

        /*  No p = topo;
                int i = 0;
                while(p != null){
               p = p.getProx();
               i++;
            }
            return i;
        */
        }

        /** Consulta o elemento do topo da Pilha
            Retorna -1 se a pilha estiver vazia.*/
        public Tipo top (){
            if (vazia()){
                return null; // Pilha vazia 
            }

            return (Tipo) topo.getConteudo();
        }

        /** Insere um elemento no topo da pilha.
            Retorna true se a insercao funcionar*/
        public boolean push(Tipo valor) {

                // Aloca memoria para novo no e preenche conteudo 
            No novoNo = new No();
            novoNo.setConteudo(valor);

            // Faz o novo no apontar pro atual topo da pilha
            novoNo.setProx(topo);

            // Atualiza o topo da pilha que agora sera o novo nó 
            topo = novoNo;

            // Atualiza o tamanho da pilha 
            nElementos++;
            return true;
        }

        /** Retira o elemento do topo da pilha.
            Retorna -1 se a pilha estiver vazia.
            Caso contrário retorna o valor removido */
        public Tipo pop () {
            if (vazia()) {
                return null; // pilha vazia 
            }
            // Guarda o nó que é topo da pilha e o seu conteudo
            No p = topo;
            Tipo valor = (Tipo) p.getConteudo();

            /* Modifica o topo da pilha para ser o proximo elemento (2o elemento da pilha) */
            /* Isso equivale a retirar o 1o elemento (topo) da pilha */
            topo = p.getProx();

            // Decrementa o tamanho da pilha 
            nElementos--;

            /* sugere ao garbage collector que libere a memoria
             *  da regiao apontada por p*/
            p= null;

            return valor;
        }
    }
    
    public static class AdaQueue <Tipo> {
	private No cabeca;
	private No cauda;
	private int tamanho;
	
	public AdaQueue(){
            cabeca = null;
            cauda = null;		
            tamanho = 0;
	}
	
	public boolean empty() {
	    if (tamanho == 0)
	        return true;
	    else
	        return false;
	}

	public int size() {
	    return tamanho;
	}
        
        public Tipo content (int posicao) {
	    No auxiliar = cabeca;
	    int contador = 1;

	    if (empty()) {
	        return null;
	    }

	    if ((posicao < 1) || (posicao > size())){
	        return null;
	    }

	    while (contador < posicao){
	        auxiliar = auxiliar.getProx();
	        contador++;
	    }

	    return (Tipo) auxiliar.getConteudo();
	}


	public boolean toFront(Tipo valor) {
	    No novo_no = new No();
	    
	    novo_no.setConteudo(valor);
	    novo_no.setProx(cabeca);
	    novo_no.setAnt(null);
            
	    if (empty()){
                cauda = novo_no;
                
            }else{
                cabeca.setAnt(novo_no);
                
            }	    
	    
	    cabeca = novo_no;
	    tamanho++;
	    return true;
	}
        
        public boolean push_back(Tipo valor) {
	    No novo_no = new No();
	    
	    novo_no.setConteudo(valor);
	    novo_no.setAnt(cauda);
	    novo_no.setProx(null);
            
	    if (empty()){
                cabeca = novo_no;
                
            }else{
                cauda.setProx(novo_no);
                
            }	    
	    
	    cauda = novo_no;
	    tamanho++;
	    return true;
	}


	private Tipo front_unitary(){          
	    Tipo valor = (Tipo) cabeca.getConteudo();
	    cabeca = null;
	    cauda = null; 
	    tamanho--;
	    return valor;
	}
	
	private Tipo front_filled(){
	    No p = cabeca;

	    Tipo valor = (Tipo) p.getConteudo();

	    cabeca = p.getProx();
	    p.getProx().setAnt(null);
	    
	    tamanho--;

	    p = null;

	    return valor;
	}
        
        public Tipo front() {
	    if (empty()) {
	    	return null;
	    }

	    if (size() == 1){ 
                return front_unitary();
            }else{
	        return front_filled();
	    }  
	}

	
	public Tipo back(){          
	    if (empty()) {
	    	return null;
	    } 
            
            if(size() == 1){
                return front_unitary();
            }
            
            No p = cauda;
	     Tipo valor = (Tipo) p.getConteudo();
	     
	     cauda.getAnt().setProx(null);
	     cauda = cauda.getAnt();
	     tamanho--;
	     
	     p = null; 
	     return valor;
	}
        
        //public AdaQueue reverse(AdaQueue fila){
        //    PilhaEnc pilha = new PilhaEnc();
        //    //No auxiliar = fila.cabeca;
        //    
        //    for(int i = 1; i <= fila.size(); i++){             
        //        pilha.push((Tipo) fila.front());
        //    }
        //    
        //    for(int i = 1; i <= fila.size(); i++){                             
        //        fila.toFront( pilha.pop() );
        //    }
        //    
        //    return fila;
        //}
		
    }
    
    public static void main(String[] arguments){
        AdaQueue<Integer> fila = new AdaQueue<Integer>();
        Scanner scan = new Scanner(System.in);
        String[] resultados;
        int contador = 0;
        int tamanho = 1;
        
        try{
            tamanho = Integer.parseInt(scan.nextLine());
        }catch(NumberFormatException n){
            
        }
        
        resultados = new String[tamanho];  // O maior tamanho possível de resultados é igual ao tamanho
                                           // de comandos, pois não poderá ser produzidos mais resultados
                                           // que comandos.
        
        for(int i = 0; i < tamanho; i++){
            String comando = scan.nextLine();
            String[] comando_e_numero = comando.split(" ");
            
            // Se o comando e número for igual a 2, isso significa que nessa linha foram passados dois parametros
            // , ou seja, um comando (para inserir) e um número (que será inserido).
            if(comando_e_numero.length == 2){
                if(comando_e_numero[0].equals("toFront")){
                    fila.toFront( Integer.parseInt( comando_e_numero[1] ) );
                }
                
                if(comando_e_numero[0].equals("push_back")){
                    fila.push_back( Integer.parseInt( comando_e_numero[1] ) );
                }
            
            // Se o tamanho for igual a 1, isso singifica que apenas foi passado um comando e nenhum número.
            }else{
                switch(comando_e_numero[0]){
                    case "front":
                        if(fila.empty()){
                            resultados[contador] = "No job for Ada?";
                        }else{
                            resultados[contador] = String.valueOf(fila.front());
                        }
                        
                        contador++;
                        break;
                        
                    case "back":
                        if(fila.empty()){
                            resultados[contador] = "No job for Ada?";
                        }else{
                            resultados[contador] = String.valueOf(fila.back());
                        }
                            
                        contador++;
                        break;
                        
                    case "reverse":
                        PilhaEnc pilha = new PilhaEnc();

                        int tamanhoFixo = fila.size();
                        
                        for(int j = 1; j <= tamanhoFixo; j++){             
                            pilha.push(fila.front());   // Põem o primeiro elemento da fila em uma pilha
                                                        // para acumular invertido.
                        }
                        
                        for(int j = 1; j <= tamanhoFixo; j++){                             
                            fila.push_back((Integer) pilha.pop());    // Pega o elemento do topo da pilha e põem
                                                                      // no fim da fila efetivamente invertendo-a
                        }
                        //if(!fila.empty()){
                        //    int[] numeros = new int[fila.size()];
                        //    int tamanhoFila = fila.size();
//
                        //    for(int j = 0; j < tamanhoFila; j++){
                        //        numeros[j] = fila.back();
                        //    }
//
                        //    for(int j = 0; j < tamanhoFila; j++){
                        //        fila.push_back(numeros[j]);
                        //    }
                        //}

                        break;
                    
                    default:
                        break;
                }
            }
        }
        
        for(int i = 0; i < contador; i++){
            System.out.println(resultados[i]);
        }
         
    }
    
}
