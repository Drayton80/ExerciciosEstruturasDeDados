#lang racket

;; Questão 1:
(define a 42)


;; Questão 2:
(define b 14)


;; Questão 3:
(+ a b)
(- a b)
(+ a (* 3 b) 7)
(/ (+ a b) 2)
(sqrt (* a b))
(/ 2 (+ (/ 1 a) (/ 1 b)))


;; Questão 4:
(define soma-medias
  (+
    (/ (+ a b) 2)
    (/ 2 (+ (/ 1 a) (/ 1 b)))
  )
)


;; Questão 5:
(if (= soma-medias 49)
    "teste 1 ok"
    "teste 2 ok"
)


;; Questão 6:
(define (quadrado numero)
  (* numero numero)
)

(quadrado 3)


;; Questão 7:
(define (delta a b c)
  (-
    (quadrado b)
    (* 4 a c)
  )
)

(define (raiz-positiva a b c)
  (/ (+ (- b) (sqrt (delta a b c)))
     (* 2 a)))


;; Questão 8:
(define (potencia x y)
  (if (= y 1)
     x
     (* x (potencia x (- y 1)))
  )
)

(potencia 2 1)
(potencia 3 2)
(potencia 4 3)
  
