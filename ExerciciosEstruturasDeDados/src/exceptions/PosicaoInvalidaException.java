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
public class PosicaoInvalidaException extends Exception {
    public PosicaoInvalidaException(){
        super("A posição pedida não está dentro dos limites da estrutura");
    }
}
