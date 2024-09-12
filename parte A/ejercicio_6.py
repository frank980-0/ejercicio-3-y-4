'''6 -Realizar un programa que: asigne a las variables numero1 y numero2 los valores
solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el
valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
a través de una función. Mostrar el resultado por pantalla.'''

numero_1 = int (input ("ingrese un numero 1 (entre 10 y 100): "))
while True:
    if 10 < numero_1 < 100:
        break
    else:
        numero_1 = int (input ("recorda que el rango tiene que ser entre 10 y 100, volver a intentar: "))
#--------------numero 2-------------------------------------------------------       
numero_2 = int (input ("ingrese el numero 2 (entre 10 y 100): "))
while True:
    if 10 < numero_2 < 100:
        break
    else:
        numero_2 = int (input ("recorda que el rango tiene que ser entre 10 y 100, volver a intentar: "))
#-------------operacion------------------------------------------------------
operacion = input("escriba 's' para sumar o 'r' para restar: ").lower()
while True :
    if operacion in ("s","r"):
        break
    else :
        operacion = input ("el dato ingresado es invalido, volver a intentar: ").lower()
#-----------funcion----------------------------------------------------------------
def realizar_operacion (opciones, num1, num2):
    if opciones == "s":
        return num1 + num2
    elif opciones == "r":
        return num1 - num2
    else:
        return None

resultado = realizar_operacion (operacion, numero_1, numero_2)
print (f"el resultado de la opercion es: {resultado}")
