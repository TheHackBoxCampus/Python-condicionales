#Ejercicio 8
#Escriba un bloque cualquiera de código en Python en donde utilice 2 condicionales (if) anidados.

nombre = input("Ingrese su nombre: ")
edad = int(input("Escribe tu edad: "))

if len(nombre) <= 2:
    print("Ingrese un nombre que corresponda")    
else:
    if edad > 15:
       print("Hola {} Puedes entrar a la montaña rusa".format(nombre))
   
    else: 
        print("Hola {} No puedes entrar a la montaña rusa.".format(nombre))