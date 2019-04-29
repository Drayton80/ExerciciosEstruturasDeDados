#lang racket

;; Neste Exercise o objetivo é repetir aquilo que foi feito no
;; Exercise 2 e 3 substituindo as funções para utilizarem Tail Recursion
(require rackunit rackunit/text-ui)

;; --- EXERCISE II ---------------------------------------------------------------------
;; --- Exercício 1 -----------------------------------------------------
;; Crie uma função (mult m n) que multiplica os dois números
;; naturais m e n, usando apenas a operação de soma.

(define (mult m n [acc 0])
  ;; Caso algum dos valores chegue a 0, retorna acc:
  (if (or (= m 0) (= n 0))
    ;; Retorna o acumulador:
    acc
    ;; Caso contrário, acumula:
    (if (> m n)
      (mult (- m 1) n (+ acc n))
      (mult m (- n 1) (+ acc m))
    )
  )
)

(define-test-suite testes-mult
  (test-equal? "3 * 4"  (mult 3 4)    12)
  (test-equal? "5 * 0"  (mult 5 0)    0)
  (test-equal? "0 * 5"  (mult 0 5)    0)
  (test-equal? "13 * 1" (mult 13 1)   13)
  (test-equal? "1 * 13" (mult 1 13)   13))


;; --- Exercício 2 -----------------------------------------------------
;; Crie uma função (sub m n) que calcula a subtração de m por n,
;; usando apenas as funções add1 e sub1. Pode ser assumido que
;; m >= n, mas não é difícil escrever uma função que funcione mesmo
;; quando m < n.

;; Sua versão passada já era Tail Recursive:
(define (sub m n)
  (if (= n 0)
     m
    (sub (sub1 m) (sub1 n))
  )
)

(define-test-suite testes-sub
  (test-equal? "42 - 0"  (sub 42 0)   42)
  (test-equal? "32 - 16" (sub 32 16)  16)
  (test-equal? "42 - 42" (sub 42 42)  0)
  (test-equal? "11 - 10" (sub 11 10)  1))


;; --- Exercício 3 ---------------------------------------------------------------
;; Crie uma função (par n) que retorna #t se n é par e #f se n é ímpar. Em seguida,
;; crie uma função (impar n) que retorna #t se n é ímpar e #f se n é par. Pense em
;; como definir uma usando a outra (ver observações nas notas de aula).

;; Sua versão passada já era Tail Recursive:
(define (par n)
  (if (= n 0)
    #t
    (if (= n 1)
      #f
      (par (- n 2))
    )
  )
)

;; Sua versão passada já era Tail Recursive:
(define (impar n)
  (if (= n 1)
    #t
    (if (= n 0)
      #f
      (impar (- n 2))
    )
  )
)

  1
(define-test-suite testes-par-impar
  (test-true "2 é par"         (par 2))
  (test-true "0 é par"         (par 0))
  (test-true "42 é par"        (par 42))
  (test-false "3 não é par"    (par 3))
  (test-false "111 não é par"  (par 111))
  (test-false "12 não é ímpar" (impar 12))
  (test-false "0 não é ímpar"  (impar 0))
  (test-true "7 é ímpar"       (impar 7))
  (test-true "353 é ímpar"     (impar 353)))


;; --- Exercício 4 --------------------------------------------------------------
;; Altere a definição de lista-ex4, abaixo, para que ela contenha os números
;; de 1 a 5, em ordem crescente, usando apenas cons e a lista vazia

;; Não é uma função, logo não é preciso alterá-la:
(define lista-ex4 (cons 1 (cons 2 (cons 3 (cons 4 (cons 5 '()))))))

;; para não entregar a resposta no teste, vamos construir a resposta de outra forma...
(define-test-suite teste-ex4
  (test-equal? "numeros de 1 a 5" lista-ex4 (range 1 6)))


;; --- Exercício 5 --------------------------------------------------------------
;; Altere a definição de lista-ex5, abaixo, para que ela contenha os números
;; de 1 a 5, em ordem crescente, usando a notação com apóstrofo ou a função list

;; Não é uma função, logo não é preciso alterá-la:
(define lista-ex5 '(1 2 3 4 5))

(define-test-suite teste-ex5
  (test-equal? "numeros de 1 a 5" lista-ex5 (range 1 6)))



;; --- Exercício 6 --------------------------------------------------------------
;; Considere a lista6, a seguir
(define lista6 (list 11 22 33 44 55 66))

;; Altere a definição da variável elem3-lista6, abaixo, para que ele tenha
;; o valor do terceiro elemento de lista6, usando apenas as funções first e rest

;; Não é uma função, logo não é preciso alterá-la:
(define elem3-lista6 (first (rest (rest lista6))))

(define-test-suite teste-ex6
  (test-equal? "elem3-lista6 deve ser 33" elem3-lista6 33))


;; --- Exercício 7 --------------------------------------------------------------
;; Escreva a função terceiro-elemento, abaixo, que retorna sempre o terceiro
;; elemento da lista l. Suponha que l sempre tenha 3 elementos ou mais.

;; Não é recursiva:
(define (terceiro-elemento l)
  (first (rest (rest l)))
)

(define-test-suite testes-terceiro-elemento
  (test-equal? "3o de '(1 2 3)" (terceiro-elemento (list 1 2 3))   3)
  (test-equal? "3o de '(4 8 15 16 23 42)"
               (terceiro-elemento (list 4 8 15 16 23 42))
               15))


;; --- Exercício 8 --------------------------------------------------------------
;; Crie uma função recursiva soma-lista (abaixo) que, dada uma lista de números,
;; calcula a soma dos números contidos

(define (soma-lista l [acc 0])
  (if (empty? l)
     acc
    ( soma-lista (rest l) (+ (first l) acc) )
  )
)

(define-test-suite testes-soma-lista
  (test-equal? "soma da lista vazia"                (soma-lista '())                  0)
  (test-equal? "soma de um número apenas"           (soma-lista '(13))                13)
  (test-equal? "soma de vários números"             (soma-lista (list 5 4 3 2 1))     15)
  (test-equal? "soma de números em ordem diferente" (soma-lista (list 1 2 3 4 5))     15)
  (test-equal? "soma de lista com zero"             (soma-lista (list 1 0 2 0 13 0))  16))


;; --- Exercício 9 ------------------------------------------------------------------
;; Crie uma função recursiva mult-lista (abaixo) que, dada uma lista de números,
;; calcula o produto dos números contidos (a lista vazia deve ter produto igual a 1)
(define (mult-lista l [acc 1])
  (if (empty? l)
    acc
    ( mult-lista (rest l) (* (first l) acc) )
  )
)

(define-test-suite testes-mult-lista
  (test-equal? "produto da lista vazia"            (mult-lista '())                  1)
  (test-equal? "produto de lista com zero"         (mult-lista (list 1 0 2 0 13 0))  0)
  (test-equal? "produto de um número"              (mult-lista '(55))                55)
  (test-equal? "produto de vários números"         (mult-lista (list 1 2 3 4 5))     120)
  (test-equal? "produto de números em outra ordem" (mult-lista (list 2 5 1 4 3))     120))


;; --- Exercício 10 ---------------------------------------------------------------------
;; Crie uma função recursiva max-lista (abaixo) que, dada uma lista de números naturais,
;; calcula o maior número entre os presentes na lista. Use (max-lista '()) = 0.
;; Supondo que a lista não irá possuir números negativos
(define (max-lista l [max 0])
  (if (empty? l)
    max
    (if (> (first l) max)
      (max-lista (rest l) (first l) )
      (max-lista (rest l)  max      )
    )
  )
)

(define-test-suite testes-max-lista
  (test-equal? "maximo da lista vazia"       (max-lista '())                     0)
  (test-equal? "maximo de lista unitaria"    (max-lista '(22))                   22)
  (test-equal? "maximo de lista com numeros" (max-lista (list 8 55 13 24 45))    55)
  (test-equal? "maximo não muda com ordem"   (max-lista (list 45 13 8 55 24))    55)
  (test-equal? "maximo de lista com zeros"   (max-lista (list 1 0 13 0 356 0))   356))


;; --- Exercício 11 -------------------------------------------------------------
;; Crie uma funcao elemento-n (abaixo) que, dada uma lista (que pode conter
;; números ou outros tipos de elementos) e um número n, retorna o n-ésimo
;; elemento da lista, contando a partir de zero. Se n é maior ou igual ao
;; tamanho da lista, a função deve retornar #f (veja os testes para exemplos

;; Sua versão passada já era Tail Recursive:
(define (elemento-n lista n)
  (if (empty? lista)
    #f
    (if (= n 0)
      (first lista)
      (elemento-n (rest lista) (sub1 n))
    )
  )
)

;; usando '() ao inves de #f pois #f é um valor de retorno válido
(define-test-suite testes-elemento-n
  (test-equal? "elemento de lista vazia" (elemento-n '() 0)                #f)
  (test-equal? "elemento 0"              (elemento-n (list 1 2 3 4 5) 0)    1)
  (test-equal? "elemento 3"              (elemento-n (list 1 2 3 4 5) 3)    4)
  (test-equal? "ultimo elemento"         (elemento-n (list 1 2 3 4 5) 4)    5)
  (test-equal? "indice fora da lista"    (elemento-n (list 1 2 3 4 5) 7)    #f))


;; --- Exercício 12 -----------------------------------------------------------
;; Muitas vezes precisamos transformar os elementos de uma lista da mesma
;; maneira. Escreva a função quadrado-lista (abaixo) que, dada uma lista de
;; números, obtém uma lista contendo o quadrado de cada número da lista
;; original (nas mesmas posições)
(define (quadrado-lista l [aux-list '()])
  (if (empty? l)
    ;; É necessário usar o reverse pois a lista vem ao contrário:
    ( reverse aux-list )
    ( quadrado-lista (rest l) (cons (* (first l) (first l)) aux-list) )
  )
)

(define-test-suite testes-quadrado-lista
  (test-equal? "quadrado da lista vazia"  (quadrado-lista '())        '())
  (test-equal? "quadrado de um número"    (quadrado-lista '(5))       '(25))
  (test-equal? "quadrado de números"
               (quadrado-lista (list 2 5 12 25))
               (list 4 25 144 625)))


;; --- Exercício 13 -----------------------------------------------------------------
;; Agora vamos selecionar itens em uma lista. Crie uma função filtra-par (abaixo)
;; que, dado uma lista de números naturais, retorna uma outra lista contendo apenas
;; os números pares da lista original. Use a função par definida no exercício 3
(define (filtra-par l [aux-list '()])
  (if (empty? l)
    (reverse aux-list)
    (if (par (first l))
      (filtra-par (rest l) (cons (first l) aux-list))
      (filtra-par (rest l) aux-list)
    )
  )
)

(define-test-suite testes-filtra-par
  (test-equal? "filtragem da lista vazia"     (filtra-par '())                  '())
  (test-equal? "filtragem de lista sem pares" (filtra-par (list 1 3 5 7 9))     '())
  (test-equal? "filtragem de lista com pares" (filtra-par (list 1 2 3 4 5))     (list 2 4))
  (test-equal? "filtragem com todos os itens pares"
               (filtra-par (list 2 4 22 144))
               (list 2 4 22 144)))

;; --- Executa todos os testes ----------------------------------------------------
(run-tests
 (test-suite "todos os testes"
             testes-mult
             testes-sub
             testes-par-impar
             teste-ex4
             teste-ex5
             teste-ex6
             testes-terceiro-elemento
             testes-soma-lista
             testes-mult-lista
             testes-max-lista
             testes-elemento-n
             testes-quadrado-lista
             testes-filtra-par))




;; --- EXERCISE III ---------------------------------------------------------------------
;; --- Questão 1 ----------------------------
;; Escreva uma função remove-primeiro tal que
;; (remove-primeiro x lst) remove a primeira ocorrência do elemento x
;; na lista lst (se houver), retornando uma nova lista com o resultado.
;; Veja os testes para exemplos.
(define (remove-primeiro x lst [aux-lst '()])
  (cond
    [(empty? lst) (reverse aux-lst)                                                        ]
    ;; Essa condição serve para que o resto da lista seja percorrida sem que hajam remoções
    ;; de outros elementos, pois, como foi definido, apenas o primeiro deve ser removido.
    ;; Só entra nela quando x é igual a aux-lst, ou seja, aux-lst é definido como um valor
    ;; que representa que o primeiro elemento já foi encontrado e removido da lista
    [(equal? x aux-lst) (remove-primeiro aux-lst (rest lst) (cons (first lst) aux-lst))    ]
    ;; Caso x seja igual ao primeiro retorna x como sendo aux-lst (para demarcar que não se
    ;; deve mais remover valores na lista, ou seja, não há mais x's a serem retirados), lst
    ;; como rest lst para poder varrer a lista até o final e aux-lst como aux-lst pois isso
    ;; indica que o first lst (elemento removido) não será adicionado à aux
    [(equal? x (first lst)) (remove-primeiro aux-lst (rest lst) aux-lst)                   ]
    ;; Entra nessa condição enquanto o elemento primeiro elemento não for encontrado e a
    ;; lista não estiver vazia (condição de parada representada pelo primeiro item de cond.
    [(not (equal? x (first lst))) (remove-primeiro x (rest lst) (cons (first lst) aux-lst))]
  )
)

(define-test-suite test-remove-primeiro
  (test-equal? "lista vazia"
               (remove-primeiro 5 '())              '())
  
  (test-equal? "uma ocorrência"
               (remove-primeiro 5 '(1 3 5 7))       '(1 3 7))
  
  (test-equal? "múltiplas ocorrências"
               (remove-primeiro 5 '(1 3 5 7 5 9))   '(1 3 7 5 9))
  
  (test-equal? "nenhuma ocorrência"
               (remove-primeiro 3 '(11 7 23 55 42)) '(11 7 23 55 42)))


;; --- Questão 2 ----------------------------

;; Escreva uma função remove-todos tal que
;; (remove-todos x lst) remove todas as ocorrencias do elemento x
;; na lista lst (se houver), retornando uma nova lista com o resultado.
(define (remove-todos x lst)
  (if (empty? lst)
    lst
    (if (= x (first lst))
      (remove-todos x (rest lst))
      (cons (first lst) (remove-todos x (rest lst)))
    )
  )
)

(define-test-suite test-remove-todos
  (test-equal? "lista vazia"           (remove-todos 5 '())              '())
  (test-equal? "uma ocorrência"        (remove-todos 5 '(1 3 5 7))       '(1 3 7))
  (test-equal? "múltiplas ocorrências" (remove-todos 5 '(1 3 5 7 5 9))   '(1 3 7 9))
  (test-equal? "nenhuma ocorrência"    (remove-todos 3 '(11 7 23 55 42)) '(11 7 23 55 42)))


;; --- Questão 3 ----------------------------

;; As funções remove-primeiro e remove-todos, acima, funcionam apenas para
;; listas de números, ou também funcionam para listas de outros tipos de
;; elementos, como strings? Funciona com listas heterogêneas (com elementos
;; de tipos diferentes na mesma lista)? Faça alguns testes que demonstram se
;; funcionam ou não. 
(define-test-suite test-validacao-remove-primeiro-todos
  (test-equal? "remove-primeiro - lista strings"  (remove-primeiro "um" '("um" "dois" "tres" "quatro"))
                                                 '("dois" "tres" "quatro"))
  (test-equal? "remove-todos - lista strings"     (remove-todos "um" '("um" "dois" "tres" "quatro" "um"))
                                                 '("dois" "tres" "quatro" "um"))
  (test-equal? "remove-primeiro - lista strings"  (remove-primeiro "um" '("um" 2 3 "quatro"))
                                                 '(2 3 "quatro"))
  (test-equal? "remove-todos - lista strings"     (remove-todos "um" '("um" 2 3 "quatro" "um"))
                                                 '(2 3 "quatro" "um"))
)

;; Resposta: Pelos testes executados acima, fica percetível que remove-primeiro e remove-todos funcionam apenas para números
;;           pois a função "(= n m)" apenas aceita números, gerando o ERROR 'contract violation' se for usada com outros valores


;; --- Questão 4 ----------------------------

;; Listas podem ser usadas como base para a criação de várias outras estruturas
;; de dados. Embora raramente uma implementação baseada em listas seja a mais
;; rápida, pode ser utilizada para conjuntos de dados pequenos e é fácil de criar
;; em uma linguagem funcional.

;; Uma estrutura de dados que pode ser construída em cima das listas são conjuntos.
;; Conjuntos são similares às listas, mas podem ter apenas uma ocorrência de cada
;; elemento. Algumas operações normalmente usadas com conjuntos são a união,
;; intersecção, diferença de conjuntos e teste de pertencimento.

;; Para o teste de pertencimento podemos continuar usando a receita recursiva baseada
;; na estrutura das listas:

;; Escreva uma função pertence? tal que
;; (pertence? x lst) retorna #t se o elemento x aparece na lista (conjunto) lst
(define (pertence? x lst)
  (if (empty? lst)
    #f
    (if (= x (first lst))
      #t
      (pertence? x (rest lst))
    )
  )
)

(define-test-suite test-pertence?
  (test-false "lista vazia"    (pertence? 5 '()))
  (test-true  "3 pertence"     (pertence? 3 '(1 2 3 4 5)))
  (test-false "9 não pertence" (pertence? 9 '(1 2 3 4 5)))
  (test-true  "5 pertence"     (pertence? 5 '(1 2 3 4 5))))


;; --- Questão 5 ----------------------------
;; Para praticar a ideia primeiro, escreva uma função combine tal que
;; (combine l1 l2) retorna uma lista de pares (listas de dois elementos) onde o primeiro
;; elemento de cada par vem de l1 e o segundo de l2. O número de pares deve ser igual ao
;; tamanho da menor lista. Veja os testes para exemplos.
(define (combine l1 l2)
  (if (empty? l1)
    l1
    (if (empty? l2)
      l2
      (cons (list (first l1) (first l2))
            (combine (rest l1) (rest l2))
      )
    )
  )
)

(define-test-suite test-combine
  (test-equal? "listas de mesmo tamanho"
               (combine '(1 2 3) '(10 20 30))  '((1 10) (2 20) (3 30)))
  
  (test-equal? "listas de tamanho diferente"
               (combine '(1)     '(55 33 11))  '((1 55)))
  
  (test-equal? "primeira lista vazia"
               (combine '()      '(1 2 3))     '())
  
  (test-equal? "segunda lista vazia"
               (combine '(1 2 3) '())          '())
  
  (test-equal? "segunda lista menor"
               (combine '(4 5 6) '(22 33))     '((4 22) (5 33))))


;; --- Questão 6 ----------------------------

;; Antes de trabalhar com conjuntos, é interessante ter algumas funções de apoio.

;; Além da falta de itens duplicados, outra característica dos conjuntos é a
;; ausência de ordem. As listas (1 2 3), (3 1 2), (2 3 1) etc todas representam
;; o mesmo conjunto. Por isso, não podemos usar equal? para testar igualdade de
;; conjuntos.

;; Mesmo nos testes, podemos ter diferentes implementações das operações de conjuntos,
;; ambas corretas, mas que retornam os elementos em uma ordem diferente (por
;; exemplo (uniao '(1 2 5) (2 5 3)) pode retornar (1 2 3 5) ou (3 2 1 5), ambos
;; os resultados corretos).

;; Escreva uma função conjunto=? tal que
;; (conjunto=? c1 c2) retorna #t se c1 e c2 contêm os mesmos elementos, não
;; necessariamente na mesma ordem, e #f caso exista algum elemento que pertence
;; a um mas não a outro.
(define (conjunto=? c1 c2)
 (if (empty? c2)
    (conjunto=? (rest c1) c2)
    #f
  )
)

(define-test-suite test-conjunto=?
  (test-true  "conjuntos vazios"        (conjunto=? '() '()))
  (test-false "vazio e unitário"        (conjunto=? '() '(1)))
  (test-true  "conjs. unitários"        (conjunto=? '(1) '(1)))
  (test-true  "iguais, mesma ordem"     (conjunto=? '(1 2 3) '(1 2 3)))
  (test-true  "iguais, ordem diferente" (conjunto=? '(1 2 3) '(1 3 2)))
  (test-true  "ordem diferente"         (conjunto=? '(2 1 3) '(2 3 1)))
  (test-false "(1 2 3) e (1 2 5)"       (conjunto=? '(1 2 3) '(1 2 5)))
  (test-false "(3 2 1) e (1 3 7)"       (conjunto=? '(3 2 1) '(1 3 7))))


;; --- Questão 7 ----------------------------

;; Outra função de apoio que pode ser útil é uma que, dada uma
;; lista qualquer (podendo conter itens duplicados) retorna uma lista válida como
;; conjunto, sem itens duplicados. Podemos chamar essa função remove-duplicatas.

;; Escreva a função remove-duplicatas tal que
;; (remove-duplicatas lst) retorna uma lista com os mesmos elementos de lst mas
;; sem que nenhum item ocorra mais de uma vez.
(define (remove-duplicatas lst)
  (if (empty? (rest lst))
    (first lst)
    (if (= (first lst) (remove-duplicatas (rest lst)))
      (remove-duplicatas (rest lst))
      (cons (first lst) (remove-duplicatas (rest lst)))
    )
  )
)

;; Um outro nome para a mesma função poderia ser lista->conjunto, enfatizando a
;; sua aplicação na criação de conjuntos a partir de listas. Nesse caso podemos
;; definir um sinônimo para a mesma função acima
(define lista->conjunto remove-duplicatas)

;; Note que usamos conjunto=? nos testes, caso contrário funções que retornassem
;; elementos em ordens diferentes não passariam
(define-test-suite test-remove-duplicatas
  (test-true "sem duplicatas"
             (conjunto=? (remove-duplicatas '(1 2 3 4 5)) '(1 2 3 4 5)))
  
  (test-true "lista vazia"
             (conjunto=? (remove-duplicatas '()) '()))
  
  (test-true "várias duplicatas"
             (conjunto=? (remove-duplicatas '(1 2 3 2 3 5)) '(1 2 3 5)))
  
  (test-true "apenas um elemento"
             (conjunto=? (lista->conjunto   '(5 5 5 5 5 5)) '(5)))
  
  (test-true "mais repetições"
             (conjunto=? (lista->conjunto '(1 2 3 1 2 3 1 2 3 1 2 3)) '(1 2 3))))

  
;; --- Questão 7 ----------------------------

;; Agora vamos implementar as operações de conjuntos implementados com listas.

;; Escreva a função uniao tal que
;; (uniao c1 c2) retorna um conjunto contendo os elementos de c1 e c2, sem duplicações.
(define (uniao c1 c2)
  '())

;; Dica: com o que vimos até agora tem pelo menos duas maneiras de escrever essa função.
;; Uma forma é uma função recursiva que tem que eliminar itens duplicados a cada passo.
;; Outra forma seria combinar os dois conjuntos primeiro e remover as duplicatas só no
;; final. É interessante (mas opcional) tentar fazer das duas formas.

(define-test-suite test-uniao
  (test-true "Vazio é elemento neutro 1"
             (conjunto=? (uniao '() '(1 2 3))  '(1 2 3)))
  
  (test-true "Vazio é elemento neutro 2"
             (conjunto=? (uniao '(4 5 6) '())  '(4 5 6)))
  
  (test-true "União de vazios"
             (conjunto=? (uniao '() '())  '()))
  
  (test-true "Sem elementos em comum"
             (conjunto=? (uniao '(1 2 3) '(4 5 6))  '(1 2 3 4 5 6)))
  
  (test-true "Com elementos em comum"
             (conjunto=? (uniao '(1 4 5) '(4 5 6))  '(1 4 5 6))))


;; --- Questão 8 -----------------------

;; Escreva uma função interseccao tal que
;; (interseccao c1 c2) retorna um conjunto contendo os elementos que ocorrem
;; em ambos c1 e c2
(define (interseccao c1 c2)
  '())

(define-test-suite test-interseccao
  (test-equal? "Conjuntos vazios"        (interseccao '()      '())      '())
  (test-equal? "Intersecção com vazio 1" (interseccao '(1 2 3) '())      '())
  (test-equal? "Intersecção com vazio 2" (interseccao '()      '(11 22)) '())
  (test-equal? "Sem elementos comuns"    (interseccao '(1 2 3) '(11 22)) '())

  (test-true "Um elemento em comum"
             (conjunto=? (interseccao '(1 2 3) '(11 1 121))  '(1)))

  (test-true "Vários elementos em comum"
             (conjunto=? (interseccao '(1 3 5 7 9 11)
                                      '(11 3 1 13 17))
                         '(1 3 11)))

  (test-true "Mesmo conjunto"
             (conjunto=? (interseccao '(1 2 3 4 5) '(5 4 3 2 1))
                         '(1 2 3 4 5))))


;; --- Questão 9 -----------------------

;; Escreva uma função diferenca tal que
;; (diferenca c1 c2) retorna um conjunto que tem todos os elementos de c1 que
;; não pertencem a c2. Por exemplo, (diferenca '(1 3 5 7) '(3 7)) deve retornar
;; '(1 5) (não necessariamente nesta ordem).
(define (diferenca c1 c2)
  '())

;; Para esta função, escreva também um conjunto de testes, e adicione a suite de 
;; testes criados à execução de todos os testes, abaixo. Você pode escrever os
;; testes antes ou depois de implementar a função.


;; --- Executa todos os testes ---------
(run-tests
 (test-suite "todos os testes"
             test-remove-primeiro
             test-remove-todos
             test-pertence?
             test-combine
             ;;test-conjunto=?
             ;;test-remove-duplicatas
             ;;test-uniao
             ;;test-interseccao
             ;;test-validacao-remove-primeiro-todos
  )
)

