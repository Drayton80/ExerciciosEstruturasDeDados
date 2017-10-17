package listas;

public class TesteLSE {

	public static void main(String args[]){
	    LSE minhaLista;
	    boolean ret;
	    int dado;

	    minhaLista = new LSE();
	    	    
	   if (minhaLista.vazia() != true)
	        System.out.println("Lista criada nao estava vazia!");
	    else
	    		System.out.println("Lista inicialmente vazia!");

	    minhaLista.insere(1, 10);
	    minhaLista.insere(2, 20);
	    minhaLista.insere(3, 30);
	    minhaLista.insere(4, 40);

	    minhaLista.insere(3, 25);
	    minhaLista.insere(5, 35);

	    System.out.println("\nLista apos 1as insercoes");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	    		dado = minhaLista.elemento(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+ dado);
	    }

	    minhaLista.insere(2, 2000);
	    ret = minhaLista.insere(1, 101);
	    System.out.println("Insercao do 101 na posicao 1 = " + ret);

	    System.out.println("\nLista apos 2o grupo de insercoes");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    }

	    ret = minhaLista.insere(20, 500);
	    System.out.println("Insercao do 500 na posicao 20 = "+ret);

	    System.out.println("Pos do elemento 10 = " + 
	    				minhaLista.posicao(10));
	    System.out.println("Pos do elemento 30 = " + 
	    				minhaLista.posicao(30));
	    System.out.println("Pos do elemento 40 = " + 
	    				minhaLista.posicao(40));

	    System.out.println("Tamanho = "+ minhaLista.tamanho());

	    dado = minhaLista.remove(3);
	    System.out.println("\nDado removido = "+ dado+ "\n\n");

	    System.out.println("Lista depois da 1a remocao \n");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    }

	    dado = minhaLista.remove(6);
	    System.out.println("\nDado removido = "+ dado+"\n");

	    System.out.println("Lista depois da remocao");
	    for (int i = 0; i < minhaLista.tamanho(); i++){
	        dado = minhaLista.elemento(i+1);
	        System.out.println((i+1)+"-esimo elemento da lista = "+dado);
	    }
 
	}
}
