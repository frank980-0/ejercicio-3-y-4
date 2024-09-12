'''Crear una función que permita determinar si un número es par o no. La función retorna
“True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
realizando la invocación o llamada.'''

def par (numero):
    if numero % 2 == 0:
        print(f"el numero dado es {True} de par")
    else:
        print(f"el numero dado es {False} (no es par)")
par (4)
par (3)