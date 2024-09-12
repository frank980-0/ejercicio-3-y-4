'''Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente.'''
#respuesta: le faltaba dividir las funciones en fragmentos mas chicos para poder darle una facil lectura,
#mantenimiento, y documentar bien que hace cada funcion

#---------------IVA--------------------------------
def calcular_IVA (valor_ventas_nacionales, iva):
    resultado_nacional = valor_ventas_nacionales * (1 / (1 + (iva / 100)))
#                   calcular el valor neto de las ventas nacionales despues de aplicar el iva
    return resultado_nacional
#----------RETENCIONES-----------------------------
def calcular_retenciones (valor_exportaciones, retenciones):
    resultado_exportaciones = valor_exportaciones * (1 - (retenciones / 100))
#                    calcula el valor neto de las importaciones despues de aplicar las retenciones
    return resultado_exportaciones
#------------IMPUESTOS TOTALES---------------------
def calcular_impuestos (valor_ventas_nacionales, valor_exportaciones, iva = 21, retenciones = 15):
    resultado_nacional = calcular_IVA (valor_ventas_nacionales, iva)
    resultado_exportaciones = calcular_retenciones (valor_exportaciones, retenciones)
# calcula el valor total del IVA y de las retenciones por exportacion y los suma todos para sacar el 
# impuesto total
    resultado_final = resultado_nacional + resultado_exportaciones
    return resultado_final
