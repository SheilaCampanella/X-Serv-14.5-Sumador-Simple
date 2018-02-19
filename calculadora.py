#!/usr/bin/python3

import sys


def suma(operando1, operando2):
    return operando1 + operando2


def resta(operando1, operando2):
    return operando1 - operando2


def multiplicacion(operando1, operando2):
    return operando1 * operando2


def division(operando1, operando2):
    return operando1 / operando2


def ala(operando1, operando2):
    return operando1 ** operando2

funciones = {
    "sumar": suma,
    "restar": resta,
    "multiplicar": multiplicacion,
    "dividir": division,
    "elevar": ala
}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: [operador][numero1][numero2]")
    _, funcion, op1, op2 = sys.argv
    try:
        numero1 = float(op1)
        numero2 = float(op2)
        solucion = funciones[operacion](numero1, numero2)
        print(str(solucion))
    except ValueError:
        sys.exit("Los tipos deben ser numericos")
