'''Especializar la función del punto 1 para que valide el número en un rango determinado
pasado por parámetro “desde”-“hasta”.'''
def parametro (numero : int ,desde : int ,hasta : int):
    return desde <= numero <= hasta
print(parametro (2,   0 ,    10)) #la llamada a la funcion
#               num, desde, hasta            
print(parametro (-3,0,10))