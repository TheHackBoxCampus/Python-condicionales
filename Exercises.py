#Ejercicio 4
#Que son las expresiones regulares
import re

Ejemplo = re.compile('a[3-5]+') # coincide con una letra, seguida de al menos 1 dígito entre 3 y 5

print("""
------------------------------------------------------------
Una expresión regular es una cadena de caracteres que es utilizada para describir o encontrar patrones dentro de otros strings
------------------------------------------------------------
""")