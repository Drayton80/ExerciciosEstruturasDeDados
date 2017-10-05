package SPOJ;

import java.util.Scanner;

public class Exercicio4 {
    //Classe Pilha Encadeada feita em sala de aula.
    private static class PilhaEnc<Tipo> {
        class No{
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
        }
        
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

	    return topo.getConteudo();
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
	    Tipo valor = p.getConteudo();

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
      
    //Classe Aplicação:
    public static void main(String[] arguments){
        Scanner scan = new Scanner(System.in);
        int linhas = Integer.parseInt(scan.nextLine());
        String[] exprecoes = new String[linhas];
        
        for(int i = 0; i < linhas; i++){
            exprecoes[i] = scan.nextLine();
            PilhaEnc<String> parenteses_e_operadores = new PilhaEnc();
            String operacao_polonesa = "";
            
            for(int j = 0; j < exprecoes[i].length(); j++){
                if(exprecoes[i].charAt(j) == '(' || exprecoes[i].charAt(j) == '+' || 
                   exprecoes[i].charAt(j) == '-' || exprecoes[i].charAt(j) == '*' || 
                   exprecoes[i].charAt(j) == '/' || exprecoes[i].charAt(j) == '^' ){
                    
                    char caractere_da_posicao = exprecoes[i].charAt(j);
                    String operador_ou_parentese = String.valueOf(caractere_da_posicao);
                    
                    parenteses_e_operadores.push(operador_ou_parentese);
                    
                }else if(exprecoes[i].charAt(j) == ')'){                    
                    while(true){                        
                        // Quando o caractere da expreção for igual a "(", significa que o ")" encontrou
                        // o parenteses que ele fecha, então o while pode ser parado. Enquanto isso não
                        // ocorrer, o for corre como se não houvesse amanhã
                        if(parenteses_e_operadores.top().equals("(")){
                            parenteses_e_operadores.pop();
                            break;
                            
                        // Enquanto o for não encontrar sua condição de parada, os operadores vão sendo
                        // desempilhados e adicionados na operação polonesa
                        }else{
                            operacao_polonesa = operacao_polonesa + parenteses_e_operadores.pop();
                        }
                    }                    
   
                }else{
                    char caractere_da_posicao = exprecoes[i].charAt(j);
                    String operador_ou_parentese = String.valueOf(caractere_da_posicao);
                    
                    operacao_polonesa = operacao_polonesa + operador_ou_parentese;
                }
                
            }
            
            exprecoes[i] = operacao_polonesa;         
        }
        
        for(int i = 0; i < linhas; i++){
            System.out.println(exprecoes[i]);
        } 
    }
}
