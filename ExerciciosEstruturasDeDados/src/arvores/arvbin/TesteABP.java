package arvores.arvbin;

public class TesteABP {

	public static void main(String args[]){
		System.out.println("Arvore Binaria de Pesquisa !\n");

	    ABP arv = new ABP();
	    
	    arv.insere(20);
	    arv.insere(30);
	    arv.insere(50);
	    arv.insere(15);
	    arv.insere(8);
	    arv.insere(14);
	    arv.insere(23);
	    arv.insere(3);
	    arv.insere(9);
	    arv.insere(67);
	    arv.insere(35);

	    No aux = arv.busca(20);
	    if (aux != null){
	    		System.out.println("No = " + aux.getConteudo());
	    		System.out.println("No.esq = " + aux.getEsq().getConteudo());
	    		System.out.println("No.dir = " + aux.getDir().getConteudo());
		 }else
			 System.out.println("No nao encontrado");

	    aux = arv.busca(50);
	    if (aux != null){
    			System.out.println("\nNo = " + aux.getConteudo());
    			System.out.println("No.esq = " + aux.getEsq().getConteudo());
    			System.out.println("No.dir = " + aux.getDir().getConteudo());
	    }else
	    		System.out.println("No nao encontrado");

	    aux = arv.busca(14);
	    if (aux != null){
			System.out.println("\nNo = " + aux.getConteudo());
			if (aux.getEsq() != null)
				System.out.println("\n\nNo.esq = " + aux.getEsq().getConteudo());
			if (aux.getDir() != null)
				System.out.println("\n\nNo.dir = " + aux.getDir().getConteudo());
	    }else
    			System.out.println("No nao encontrado");

	    arv.exibe();

	    return;
	}
}
