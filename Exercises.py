#Ejercicio 2 
#2. En la jerarquía de operadores, cuáles son los que más
# prioridad tienen cuando el intérprete de Python los evalúa?

def prioridad():
    return print(
    f""" 
    Mayor prioridad
    ---------------
    1 Operaciones entre parentesis \t\t\t\t\t\t () 
    2 Potencia \t\t\t\t\t\t\t\t\t ** 
    3 Multiplicación y División, módulo o residuo, División entenera       *, /, %, // 
    4 Suma y resta \t\t\t\t\t\t\t\t+, -
    --------------
    Menor prioridad
    """)

prioridad()