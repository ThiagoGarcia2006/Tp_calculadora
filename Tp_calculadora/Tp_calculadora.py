from funciones_calculadora import *

A = None
B = None

while True:
    print("\nMENU:")
    print("1. Ingresar 1er operando (A={})".format(A if A is not None else "x"))
    print("1. Ingresar 2do operando (B={})".format(B if B is not None else "y"))
    print("3. Calcular todas las operaciones")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        A = int(input("Ingrese el valor para A: "))
    elif opcion == "2":
        B = int(input("Ingrese el valor para B: "))
    elif opcion == "3":
        if A is None or B is None:
            print("Debe ingresar ambos operandos primero.")
        else:
            resultado_suma = suma(A, B)
            resultado_resta = resta(A, B)
            resultado_division = dividir(A, B)
            resultado_multiplicacion = multiplicar(A, B)
            factorial_A = factorial(A)
            factorial_B = factorial(B)

            print("Resultados de todas las operaciones: ")  
            print(f" {A} + {B} = {resultado_suma}")
            print(f" {A} - {B} = {resultado_resta}") 
            print(f" {A} / {B} = {resultado_division}") 
            print(f" {A} * {B} = {resultado_multiplicacion}")
            print(f" Factorial de {A} = {factorial_A}") 
            print(f" Factorial de {B} = {factorial_B}")
    elif opcion == "4":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")  
        
                 



