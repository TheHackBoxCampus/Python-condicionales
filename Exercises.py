#Ejercicio 1 
#1. Qué operadores utiliza Python en los siguientes casos:

#A. División Modular                %
#B. Exponenciación                  **
#C. División que retorne entero.    //

def operadores():
    numero1 = int(input(f"Digite el primer numero: "))
    numero2 = int(input(f"Digite el segundo numero: "))

    print(f"\nLa división modular de {numero1} % {numero2} = {numero1 % numero2}") 
    print(f"La exponenciación de {numero1} elevado a {numero2} = {numero1 ** numero2}") 
    print(f"La división de enteros es: {numero1} // {numero2} = {numero1 // numero2}") 

operadores()