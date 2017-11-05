package arvores.arvbin;

public class TesteArvBin {

	public static void main(String args[]){
		System.out.println("Arvores Binarias!");

		ArvBin arv = new ArvBin();
		arv.insereRaiz(2);

		arv.insereEsq(2, 4); /* insere 4 a esq do 2*/
		arv.insereDir(2, 6);

		arv.insereEsq(4, 8);
		arv.insereDir( 4, 10);

		arv.insereEsq(6, 12);
		arv.insereEsq(10, 14);
		arv.insereDir(10, 16);

		arv.insereEsq(14, 18);
		arv.insereDir(14, 20);


		No no = arv.busca(14);
		if (no != null){
			System.out.println("No existe, conteudo = " + no.getConteudo());
		}

		System.out.println("Pre-ordem");
		arv.exibePreOrdem();

		System.out.println("\nIn-ordem");
		arv.exibeInOrdem();

		System.out.println("\nPos-ordem");
		arv.exibePosOrdem();

		return;
	}
}
