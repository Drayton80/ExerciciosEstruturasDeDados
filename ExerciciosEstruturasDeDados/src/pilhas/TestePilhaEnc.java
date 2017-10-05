package pilhas;

public class TestePilhaEnc {
	public static void main(String args[]){
	    int tam = 0, to = 0;

	    System.out.println("Inicio do programa");
	    PilhaEnc pilha = new PilhaEnc();
	    
	    tam = pilha.tamanho();
	    System.out.println("Tamanho inicial da pilha = "+ tam);

	    pilha.push(10);
	    pilha.push(20);
	    pilha.push(30);
	    pilha.push(40);

	    tam = pilha.tamanho();
	    System.out.println("Tamanho atual da pilha = "+ tam);

	    to = pilha.top();
	    System.out.println("Topo da pilha atualmente =  "+ to);

	    to = pilha.pop();
	    System.out.println("Removendo topo da pilha = " + to);

	    to = pilha.pop();
	    System.out.println("Removendo topo da pilha = " + to);

	    pilha.push(50);

	    to = pilha.pop();
	    System.out.println("Removendo topo da pilha = " + to);

	    to = pilha.pop();
	    System.out.println("Removendo topo da pilha = " + to);

	    to = pilha.pop();
	    System.out.println("Removendo topo da pilha = " + to);

	    tam = pilha.tamanho();
	    System.out.println("Tamanho final da pilha = "+ tam);

	    to = pilha.top();
	    System.out.println("Topo da pilha atualmente = "+ to);
	}
}
