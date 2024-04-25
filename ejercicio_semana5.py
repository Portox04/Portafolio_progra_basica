#Ejercicio  1

print()
print("Ejercicio #1")
print()

for i in range(20,40,2):
    print(i," y su raiz es", i**0.5)

#Ejercicio  2

print()
print("Ejercicio #2")
print()

add_estudiantes = input("Vamos a evaluar algunos estudiantes para comenzar coloca Y/N: ")
notas_aprobados = int(0)
notas_reprobados = int(0)
nota_mayor = int(0)
nota_menor = int(100)

while add_estudiantes=="Y":
    nota_estudiante= input("Ingresa la nota del estudiante: ")
    nota_estudiante = int(nota_estudiante)
    if nota_estudiante>=70:
        notas_aprobados=notas_aprobados+1
        if nota_estudiante>nota_mayor:
            nota_mayor= nota_estudiante
        elif nota_estudiante<nota_menor:
            nota_menor= nota_estudiante
    else:
        notas_reprobados=notas_reprobados+1
        if nota_estudiante<nota_menor:
            nota_menor= nota_estudiante
    add_estudiantes = input("Quieres agregar otro estudiante?(Y/N): ")
print("La nota mas alta es ",nota_mayor," y la mas baja es ",nota_menor)
print("Hay ",notas_aprobados,"aprobados y ",notas_reprobados," reprobados")
print("Es todo por hoy gracias!")

#Ejercicio  1.2

print()
print("Ejercicio #1.2")
print()

salario_empleado = float(0)
salario_total = float(0)

print("Empezaremos con el calculo de los calculos de los salarios de los 9 empleados")

for i in range (0,9):
    salario_empleado = input("Coloca el salario del empleado:")
    salario_empleado = float(salario_empleado)
    salario_total = salario_total+(salario_empleado*1.09)
    
print("El salario total con el 9% de cargas sociales serian ", salario_total)

#Ejercicio 2.2

print()
print("Ejercicio #2.2")
print()

pares = int(0)

for x in range (0,10):
    numero = input("Ingresa el valor:")
    numero = int(numero)

    if numero%2==0:
        pares += numero

print("La suma de los numeros pares es:", pares)
