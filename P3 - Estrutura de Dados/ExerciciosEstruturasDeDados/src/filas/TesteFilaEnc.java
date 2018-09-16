package filas;

public class TesteFilaEnc {
	
	public static void main(String args[]){
	    int tam, valor;

	    System.out.println("Inicio do programa!");

	    FilaEnc f1 = new FilaEnc();
	    tam = f1.tamanho();
	    System.out.println("Tamanho inicial da fila = " + tam);

	    f1.insere(10);
	    f1.insere(20);
	    f1.insere(30);
	    f1.insere(40);

	    tam = f1.tamanho();
	    System.out.println("\n\nTamanho atual da fila = "+ tam);

	    valor = f1.remove();
	    System.out.println("Removido da fila = " + valor);

	    valor = f1.remove();
	    System.out.println("Removido da fila = " + valor);

	    f1.insere(50);

	    valor = f1.remove();
	    System.out.println("Removido da fila = " + valor);

	    valor = f1.remove();
	    System.out.println("Removido da fila = " + valor);

	    valor = f1.remove();
	    System.out.println("Removido da fila = " + valor);
	}
}
