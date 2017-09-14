package listas;

public class TesteListaSeq {

	public static void main(String args[]){
		ListaSequencial minhaLista;
	    boolean ret;
	    int dado;

	    minhaLista = new ListaSequencial();

	    if (minhaLista.lista_vazia() == true)
	    		System.out.println("Lista inicialmente vazia!");
	    else
	    	 	System.out.println("Lista criada nao estava vazia!");
		   
	    minhaLista.adicionar(1, 10);
	    minhaLista.adicionar(2, 20);
	    minhaLista.adicionar(3, 30);
	    minhaLista.adicionar(4, 40);

	    minhaLista.adicionar(3, 25);
	    minhaLista.adicionar(5, 35);

	    System.out.println("\nLista apos 1as insercoes");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	    		dado = minhaLista.elemento(i);
	        System.out.println((i)+"-esimo elemento da lista = "+ dado);
	    }

	    minhaLista.adicionar(2, 2000);
	    ret = minhaLista.adicionar(1, 101);
	    System.out.println("Insercao do 101 na posicao 1 = " + ret);

	    System.out.println("\nLista apos 2o grupo de insercoes");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i);
	        System.out.println(i+"-esimo elemento da lista = "+dado);
	    }

	    ret = minhaLista.adicionar(20, 500);
	    System.out.println("Insercao do 500 na posicao 20 = "+ret);

	    System.out.println("Pos do elemento 10 = " + 
	    				minhaLista.posicao(10));
	    System.out.println("Pos do elemento 30 = " + 
	    				minhaLista.posicao(30));
	    System.out.println("Pos do elemento 40 = " + 
	    				minhaLista.posicao(40));

	    System.out.println("Pos do elemento 15 = " + 
				minhaLista.posicao(15));

	    System.out.println("Tamanho = "+ minhaLista.tamanho());

	    dado = minhaLista.remover(3);
	    System.out.println("\nDado removido = "+ dado+ "\n\n");

	    System.out.println("Lista depois da 1a remocao \n");
	    for (int i = 1; i <= minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i);
	        System.out.println(i+"-esimo elemento da lista = "+dado);
	    }

	    dado = minhaLista.remover(6);
	    System.out.println("\nDado removido = "+ dado+"\n");

	    System.out.println("Lista depois da remocao");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    }
	}
	
}
