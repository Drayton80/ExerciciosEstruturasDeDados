package classesDeOutros;

/**
 * Por dylima, em: http://www.guj.com.br/t/bubble-sort-em-java/75462/2
 */

public class Bolha {
    public void bubbleSort(int v[]) {
        for (int i = v.length; i >= 1; i--) {
            for (int j = 1; j < i; j++) {
                if (v[j - 1] > v[j]) {
                    int aux = v[j];
                    v[j] = v[j - 1];
                    v[j - 1] = aux;
                }
            }
        }
    }
}
