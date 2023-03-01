#Ejercicio 7
#Cuál es la diferencia entre un condicional simple y un condicional compuesto?
def simple():
    if 5 > 3:
        return "True"

def compuesto():
     if 5 > 10:
        return "True"
     else: 
        return "False"

simpleExample = simple()
compuestoExample = compuesto()

print(
    f"""
    -----------------------------------------------------
    El condicional simple solo puede dar true
    Mientras que uno compuesto puede dar las dos opciones
    true or false:
    ----------------------------    
    simple: {simpleExample}
    compuesto: {compuestoExample}
    -----------------------------------------------------
    """)