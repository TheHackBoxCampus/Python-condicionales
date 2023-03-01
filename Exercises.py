#Ejercicio 5
#Enumere 5 tipos de datos en Python y suministre un valor de ejemplo de cada uno.

def tiposDeDatos():
    str = "Miller Nariño"
    int = 10
    float = 9.8
    bool = False
    list = [1, str, int, float, bool]
    dicts = {"nombre": "miller"}
    tuples = (1,2,3,4)

    print(
    f"""
    -----------------------------------------------
    tipo Entero: {int}
    tipo Float: {float}
    tipo Booleano: {bool}
    tipo Cadena: {str}
    tipoLista: {list}
    tipo tupla: {tuples}
    tipo diccionario: {dicts}
    -----------------------------------------------
    """)

tiposDeDatos()