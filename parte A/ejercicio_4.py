'''Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en
sus 4 combinaciones.
restar1(int, int)->int:
restar2()->int:
restar3(int, int):
restar4():      '''

def restar1 (a: int, b: int) -> int:
    return a-b
def restar2 () -> int:
    num1 = 4
    num2 = 10
    return num2 - num1
def restar3 (a : int, b : int):
    resultado = a - b
    print (f"el resultado de la resta de {a} y {b} es : {resultado}")
def restar4 ():
    num1 = 20
    num2 = 10
    resultado = num1 - num2
    print (f"la resta de {num1} y {num2} es : {resultado}")

resultado_1 = restar1 (10,5)
print (f"el resultado de la resta es: {resultado_1} ")

resultado_2 = restar2 ()
print (f"el resultado de la resta es {resultado_2}")

resultado_3 = restar3 (20,10)

resultado_4 = restar4 ()

