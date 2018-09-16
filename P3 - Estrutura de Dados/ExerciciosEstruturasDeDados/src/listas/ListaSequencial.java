package listas;

/**
 *  tentativa de implementação da Lista Sequencial, Está incompleta e dando erro
 *      Nota: refazer ela toda do inicio
 * @author drayton80
 */
public class ListaSequencial {
    private int tamanho_maximo;
    private int[] elementos;
    private int final_da_lista = 0;
    
    //Construtores:
    public ListaSequencial(){
        tamanho_maximo = 100;
        elementos = new int[tamanho_maximo];
    }
    
    public ListaSequencial(int tamanho){
        tamanho_maximo = tamanho;
        elementos = new int [tamanho_maximo];
    }
    
    //Métodos:   
    public int tamanho(){
        return final_da_lista;
    }
    
    public int posicao(int valor){
        for(int i = 0; i < final_da_lista; i++){
            if(elementos[i] == valor){
                return (i+1);
            }
        }
        
        return -1;
    }
    
    public boolean lista_vazia(){
        if(final_da_lista == 0){
            return true;
        }else{
            return false;
        }
    }
     
    public boolean adicionar(int elemento, int posicao){
        if(final_da_lista == tamanho_maximo){
            return false;
        }
        
        if(posicao == 1 && final_da_lista == 0){
            elementos[posicao - 1] = elemento;
            final_da_lista++;
            
            return true;
        }
        
        if(posicao <= 0 || final_da_lista < posicao){
            return false;
        }else{
            for(int i = (posicao - 1); i < final_da_lista; i++){
                elementos[i+1] = elementos[i];
            }
            
            elementos[posicao - 1] = elemento;
            final_da_lista++;
            
            return true;
        }
    }
    
    //public boolean adicionar_no_final(int elemento){
    //    if(final_da_lista == tamanho){
    //        return false;
    //    }else{
    //        lista[final_da_lista] = elemento;
    //        final_da_lista++;
    //        return true;
    //    }
    //}
    
    public int elemento(int posicao){
        if(posicao < 0 || final_da_lista < posicao){
            return -1;
        }
        
        return elementos[posicao-1];
    }
    
    public int remover(int posicao){
        int auxiliar;
        
        if(posicao <= 0 || final_da_lista < posicao){
            return -1;
        }else{
            auxiliar = elementos[posicao-1];
            
            for(int i = (final_da_lista - 1); i > (posicao - 1); i--){
                elementos[i-1] = elementos[i];
            }
          
            final_da_lista--;
            
            return auxiliar;
        }
    }
}
