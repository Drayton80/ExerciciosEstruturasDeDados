package listas;

public class TesteListaSeqGen {
	public static void main(String args[]){
	    ListaSeqGen<String> minhaLista;
	    boolean ret;
	    String dado;

	    minhaLista = new ListaSeqGen<String>();

	    if (minhaLista.vazia() == true)
	    		System.out.println("Lista inicialmente vazia!");
	    else
	    		System.out.println("Lista criada nao estava vazia!");

	    minhaLista.insere(1, "Maritan");
	    minhaLista.insere(2, "Lincoln");
	    minhaLista.insere(3, "Thaís");
	    minhaLista.insere(4, "Raimundo");

	    minhaLista.insere(3, "Hamilton");
	    minhaLista.insere(5, "Daniela");

	    System.out.println("\nLista apos 1as insercoes");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	    		dado = minhaLista.elemento(i);
	        System.out.println(i+"-esimo elemento da lista = "+ dado);
	    }

	    minhaLista.insere(2, "Margareth");
	    ret = minhaLista.insere(1, "Raoni");
	    System.out.println("Insercao do Raoni na posicao 1 = " + ret);

	    System.out.println("\nLista apos 2o grupo de insercoes");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i);
	        System.out.println(i+"-esimo elemento da lista = "+dado);
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

	    dado = minhaLista.remove(3);
	    System.out.println("\nDado removido = "+ dado+ "\n\n");

	    System.out.println("Lista depois da 1a remocao \n");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i);
	        System.out.println(i+"-esimo elemento da lista = "+dado);
	    }

	    dado = minhaLista.remove(6);
	    System.out.println("\nDado removido = "+ dado+"\n");

	    System.out.println("Lista depois da remocao");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i);
	        System.out.println(i+"-esimo elemento da lista = "+dado);
	    }
	}

}
