package estruturasDeDados.listas;

/**
 *
 * @author drayt
 */
public class ListaSequencial {
    private int tamanho_maximo;
    private int[] elementos;
    private int final_da_lista = 0;
    
    //Construtores:
    //public ListaSequencial(){
    //    tamanho = 100;
    //    lista = new int[tamanho];
    //}
    
    public ListaSequencial(int tamanho){
        tamanho_maximo = tamanho;
        elementos = new int [tamanho_maximo];
    }
    
    //Métodos:   
    public int get_final_da_lista(){
        return final_da_lista;
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
    
    public boolean remover(int posicao){
        if(posicao <= 0 || final_da_lista < posicao){
            return false;
        }else{
            for(int i = (final_da_lista - 1); i > (posicao - 1); i--){
                elementos[i-1] = elementos[i];
            }
          
            final_da_lista--;
            
            return true;
        }
    }
}
