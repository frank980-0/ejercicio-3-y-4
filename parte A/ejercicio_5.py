'''5 - Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario,
valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una
función llamada realizarDescuento(). Mostrar el resultado por pantalla. Atención: pueden
reutilizarse funciones ya creadas.'''

numero_1 = int (input ("ingrese un numero (entre 10 y 100): "))
while True:
    if 10 < numero_1 < 100:
        break
    else:
        numero_1 = int (input ("recorda que el rango tiene que ser entre 10 y 100, volver a intentar: "))
    
def realizarDescuento (numero):  # es la funcion que aplica el descuento del 5% 
    descuento = 0.05 
    descuento_aplicado = numero * (1-descuento)
    return descuento_aplicado

valor_con_descuento = realizarDescuento (numero_1)
print (f"""el valor sin descuento : {numero_1}
    valor con descuento : {valor_con_descuento} """)        
