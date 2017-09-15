package SPOJ;

/**
 *
 * @author drayton80
 */

import java.util.*;

public class Exercicio2 {
    static class LSEGen<T> {
	
	class No {
            private T conteudo;
            private No prox;

            public No(){
                    setProx(null);
            }

            public T getConteudo() {
                    return conteudo;
            }

            public void setConteudo(T conteudo) {
                    this.conteudo = conteudo;
            }

            public No getProx() {
                    return prox;
            }

            public void setProx(No prox) {
                    this.prox = prox;
            }
	}
	
	private No cabeca;
	private int tamanho;
	
	public LSEGen(){
		cabeca = null;
		tamanho = 0;
	}
	
	/** Verifica se a Lista está vazia */
	public boolean vazia() {
	    if (tamanho == 0)
	        return true;
	    else
	        return false;
	}

	/**Obtém o tamanho da Lista*/
	public int tamanho() {
	    return tamanho;
	}

	/** Obtém o i-ésimo elemento de uma lista
	    Retorna o valor encontrado. */
	public T elemento (int pos) {
	    No aux = cabeca;
	    int cont = 1;

	    if (vazia()) {
	        return null; // Consulta falhou 
	    }

	    if ((pos < 1) || (pos > tamanho())){
	        return null; // Posicao invalida 
	    }

	    // Percorre a lista do 1o elemento até pos 
	    while (cont < pos){
	        // modifica "aux" para apontar para o proximo elemento da lista 
	        aux = aux.getProx();
	        cont++;
	    }

	    return aux.getConteudo();
	}

	/**Retorna a posição de um elemento pesquisado.
	    Retorna 0 caso não seja encontrado */
	public int posicao (T dado) {
	    int cont = 1;
	    No aux;

	    /* Lista vazia */
	    if (vazia()) {
	        return -1;
	    }

	    /* Percorre a lista do inicio ao fim até encontrar o elemento*/
	    aux = cabeca;
		while (aux != null) {
	        /* Se encontrar o elemento, retorna sua i n;*/
	        if (aux.getConteudo().equals(dado)){
	            return cont;
	        }

	        /* modifica "aux" para apontar para o proximo elemento da lista */
	        aux = aux.getProx();
	        cont++;
	    }

	    return -1;
	}

	/** Insere nó em lista vazia */
	private boolean insereInicioLista(T valor) {
	    // Aloca memoria para novo no 
	    No novoNo = new No();
	    
	    // Insere novo elemento na cabeca da lista
	    novoNo.setConteudo(valor);
	    novoNo.setProx(cabeca);
	    cabeca = novoNo;
	    tamanho++;
	    return true;
	}

	/** Insere nó no meio da lista */
	private boolean insereMeioLista(int pos, T dado){
	    int cont = 1;

	    // Aloca memoria para novo no
	    No novoNo = new No();
	    novoNo.setConteudo(dado);

	    // Localiza a pos. onde será inserido o novo nó
	    No aux = cabeca;
	    while ((cont < pos-1) && (aux != null)){
	          aux = aux.getProx();
	          cont++;
	    }

	    if (aux == null) {  // pos. inválida 
	    		return false;
	    }

	    // Insere novo elemento apos aux
	    novoNo.setProx(aux.getProx());
	    aux.setProx(novoNo);

	    tamanho++;
	    return true;
	}

	/** Insere nó no fim da lista */
	private boolean insereFimLista(T dado){
	    // Aloca memoria para novo no 
	    No novoNo = new No();
	    novoNo.setConteudo(dado);

	    // Procura o final da lista 
	    No aux = this.cabeca;
	    while(aux.getProx() != null){
	        aux = aux.getProx();
	    }

	    novoNo.setProx(null);
	    aux.setProx(novoNo);

	    this.tamanho++;
	    return true;
	}

	/**Insere um elemento em uma determinada posição
	    Retorna true se conseguir inserir e 
	    false caso contrario */
	public boolean insere(int pos, T dado) {
		if ((vazia()) && (pos != 1)){
	        return false; /* lista vazia mas i inv*/
	    }

	 	/* inserção no início da lista (ou lista vazia)*/
	    if (pos == 1){
	        return insereInicioLista(dado);
	    }
	    /* inserção no fim da lista */
	    else if (pos == tamanho+1){
	        return insereFimLista(dado);
	   }
	   /* inserção no meio da lista */
	   else{
	        return insereMeioLista(pos, dado);
	   }
	}

	/** Remove elemento do início da lista */
	private T removeInicioLista(){
	    No p = cabeca;

	    // Dado recebe o dado removido
	    T dado = p.getConteudo();

	    // Retira o 1o elemento da lista (p)
	    cabeca = p.getProx();
	    tamanho--;

	    // Sugere ao garbage collector que libere a memoria
	    //  da regiao apontada por p
	    p = null;

	    return dado;
	}

	/** Remove elemento no meio da lista */
	private T removeNaLista(int pos){
	     No atual = null, antecessor = null;
	     T dado = null;
	     int cont = 1;

	     /* Localiza o nó que será removido*/
	     atual = cabeca;
	     while((cont < pos) && (atual != null)){
	           antecessor = atual;
	           atual = atual.getProx();
	           cont++;
	     }

	     if (atual == null) { /* pos. inválida */
	        return null;
	     }

	    /* retira o elemento da lista */
	    dado = atual.getConteudo();
	    antecessor.setProx(atual.getProx());
	    tamanho--;

	    /* sugere ao garbage collector que libere a memoria
	     *  da regiao apontada por p*/
	    atual = null;
	    return dado;
	}

	/**Remove um elemento de uma determinada posição
	    Retorna o valor a ser removido. 
	    null se a posição for inválida ou a lista estiver vazia*/
	public T remove(int pos) {
		// Lista vazia 
	    if (vazia()) {
	    		return null;
	    }

	    // Remoção do elemento da cabeça da lista 
	    if (pos == 1){
	        return removeInicioLista();
	    }
	    // Remoção em outro lugar da lista
	    else{
	        return removeNaLista(pos);
	    }
	}	
    }

    public static void main(String[] arguments){
        Scanner entrada = new Scanner(System.in);
        String tamanhos_com_espacos;
        String[] tamanhos_sem_espacos;
        LSEGen<String> afazeres = new LSEGen<String>();
        LSEGen<String> consultas = new LSEGen<String>();
        boolean repete_na_palavra;
        int[] repeticoes;
        int n, q;
        
        tamanhos_com_espacos = entrada.nextLine();
        tamanhos_sem_espacos = tamanhos_com_espacos.split(" ");
        
        n = Integer.parseInt(tamanhos_sem_espacos[0]);
        q = Integer.parseInt(tamanhos_sem_espacos[1]);
        
        repeticoes = new int[q];
        
        //Insere palavras de cada linha N na lista de afazeres
        for(int posicao = 1; posicao <= n; posicao++){
            afazeres.insere(posicao, entrada.nextLine());
        }
        
        //Insere as palavras de cada linha Q na lista de consultas
        for(int posicao = 1; posicao <= q; posicao++){
            consultas.insere(posicao, entrada.nextLine());
        }
        
        // Checa se cada existe alguma repetição de conjunto de caracteres da lista de consultas
        // na lista de afazeres.
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= q; j++){
                int tamanho_da_palavra_afazer   = afazeres.elemento(i).length();
                int tamanho_da_palavra_consulta = consultas.elemento(j).length();
                String prefixo;
                
                //Se o tamanho do elemento da consulta for maior que o do afazer, isso significa
                // que é impossível a palavra possuir aquele prefixo que é a consulta, pois a propria
                // palavra do afazer é menor do que aquela que se pode consultar.
                if(tamanho_da_palavra_consulta <= tamanho_da_palavra_afazer){
                    prefixo = afazeres.elemento(i).substring( 0, consultas.elemento(j).length());
                    
                    //  contains retorna um boolean dado após checar se uma determinada sequência de caracteres pertence
                    //   ao String.
                    repete_na_palavra = prefixo.contains(consultas.elemento(j));
                    
                }else{
                    repete_na_palavra = false;
                }
                    

                //v-v-v---{ Bem vindo ao Lado Obscuro dos Códigos de programação }---v-v-v//
                //
                // repete_na_palavra = (consultas.elemento(j).length() <= afazeres.elemento(i).length()) ?
                //   afazeres.elemento(i).substring( 0, consultas.elemento(j).length()).contains(consultas.elemento(j)) : false;
                //
                //v-v-v------------------{ Obrigado, volte sempre }-----------------v-v-v//
                
                
                //Se há repetição o número inteiro no array de repeticoes irá ser incrementado
                // OBS.: Arrays começam com todos os valores padrões em 0, logo basta incrementar esses
                //       valores na posição desejada, marcada como j-1, pois j começa em 1 e não 0.
                if(repete_na_palavra){
                    repeticoes[j-1] = repeticoes[j-1] + 1;
                }
            }
        }
        
        for(int posicao = 0; posicao < repeticoes.length; posicao++){
            System.out.println( repeticoes[posicao] );
        }
    }
}
