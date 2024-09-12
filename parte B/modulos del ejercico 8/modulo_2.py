'''En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.'''

def calcular_salario (horas : float, años : float) -> float:
    sueldo_por_hr = horas * 10 
    incremento_anual = años * 0.03  #se calcula el incremento por años de antiguedad
    sueldo_total = sueldo_por_hr * (1 + incremento_anual) #se le aplica el incremento al sueldo por hr
    return sueldo_total

'''También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo. '''

def calculo_productividad (cantidad : int, horas_trabajadas : float):
    if horas_trabajadas == 0:  #para evitar el caso de la division por 0 y el programa colapse
        return 0
    produccion = cantidad / horas_trabajadas
    return produccion

'''En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad'''

def reporte_empleado (nombre : str, edad : int , salario : float, produccion : float):
    print (f"""el nombre del empleado es: {nombre} su edad es de: {edad} años
           su salario es de: {salario}
           su productividad es de: {produccion} 
           """)