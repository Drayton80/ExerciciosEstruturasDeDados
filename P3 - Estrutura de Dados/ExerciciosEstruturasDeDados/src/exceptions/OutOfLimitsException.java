/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exceptions;

/**
 *
 * @author drayton80
 */
public class OutOfLimitsException extends Exception {
    public OutOfLimitsException(){
        super("Valor escolhido está fora dos limites pré-estabelecidos.");
    }
}
