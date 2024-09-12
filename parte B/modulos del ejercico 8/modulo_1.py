'''Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo. 
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad'''
import modulo_2
salario = modulo_2.calcular_salario (10,1)
produccion = modulo_2.calculo_productividad (10,3)
reporte = modulo_2.reporte_empleado ("frank",18, salario,produccion)