#Ejercicio 10
#En su casa le solicitan que realice un algoritmo en Python,
#que permita calcular el valor a pagar por concepto de
#energía eléctrica. Los datos que se conocen son los
#siguientes:
#- Mes de consumo - Valor kw
#-Total kw consumido en el mes - estrato

def calc():
    stratumsValues = [1,233,291,496,583,700] # example values 
    stratus = int(input("De que estrato es: "))
    numberMonth = int(input("Cuantos meses de costo debe: "))
    kwMonth = int(input("Cuanto gasto durante el mes: "))
    value_kw = stratumsValues[stratus]
    consumption = (kwMonth * value_kw) * numberMonth
    result = f"El consumo mensual fue {consumption}, durante {numberMonth} mes/meses"
    return result
    
print(calc())