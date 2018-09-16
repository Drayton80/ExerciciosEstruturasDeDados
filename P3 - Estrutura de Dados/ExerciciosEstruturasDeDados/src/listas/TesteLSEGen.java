package listas;

public class TesteLSEGen {
    static class ListaSimplesmenteEncadeada2<Generico> {
        //Classe Interna Nó:
         class No{
             private Generico conteudo;
             private No proximo;

            //Construtores:
             public No(){
                 set_proximo(null);
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

         public ListaSimplesmenteEncadeada2(){
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

         public Generico elemento(int posicao){
             No auxiliar = cabeca;

             if(vazia()){
                 return null;
             }

             if((posicao < 1) || (tamanho() < posicao)){
                 return null;
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

         public boolean insere(int posicao, Generico valor){

             if(vazia() && posicao != 1){
                 return false;
                 
             }


             if( posicao == 1 ){
                 insere_no_inicio(valor);
                 return true;

             }else{
                 if(posicao < 1 || numero_de_elementos+1 < posicao){
                     return false;
                 }

                 insere_no_meio(posicao, valor);
                 return true;
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

    
	public static void main(String args[]){
	    ListaSimplesmenteEncadeada2<String> minhaLista;
	    boolean ret;
	    String dado;

	    minhaLista = new ListaSimplesmenteEncadeada2<String>();

	    if (minhaLista.vazia() != true)
	        System.out.println("Lista criada nao estava vazia!");
	    else
	    		System.out.println("Lista inicialmente vazia!");

	    minhaLista.insere(1, "Maritan");
	    minhaLista.insere(2, "Lincoln");
	    minhaLista.insere(3, "Thaís");
	    minhaLista.insere(4, "Raimundo");

	    minhaLista.insere(3, "Hamilton");
	    minhaLista.insere(5, "Daniela");

	    System.out.println("\nLista apos 1as insercoes");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	    		dado = minhaLista.elemento(i+1);
                        System.out.println(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+ dado);
	    }

	    minhaLista.insere(2, "Margareth");
	    ret = minhaLista.insere(1, "Raoni");
	    System.out.println("Insercao do Raoni na posicao 1 = " + ret);

	    System.out.println("\nLista apos 2o grupo de insercoes");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    }

	    ret = minhaLista.insere(20, "Guido");
	    System.out.println("Insercao do Guido na posicao 20 = "+ret);

	    System.out.println("Pos do elemento Maritan = " + 
	    				minhaLista.posicao("Maritan"));
	    System.out.println("Pos do elemento Thaís = " + 
	    				minhaLista.posicao("Thaís"));
	    System.out.println("Pos do elemento Raimundo = " + 
	    				minhaLista.posicao("Raimundo"));

	    System.out.println("Tamanho = "+ minhaLista.tamanho());

	    //dado = minhaLista.remove(3);
	    //System.out.println("\nDado removido = "+ dado+ "\n\n");
//
	    //System.out.println("Lista depois da 1a remocao \n");
	    //for (int i = 0; i < minhaLista.tamanho(); i++){
	    //    dado = minhaLista.elemento(i+1);
	    //    System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    //}
//
	    //dado = minhaLista.remove(6);
	    //System.out.println("\nDado removido = "+ dado+"\n");
//
	    //System.out.println("Lista depois da remocao");
	    //for (int i = 0; i < minhaLista.tamanho(); i++){
	    //    dado = minhaLista.elemento(i+1);
	    //    System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    //}
	}

}
