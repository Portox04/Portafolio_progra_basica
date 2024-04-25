#Ejercicio Ejemplo 1

print("Ejercicio Ejemplo #1")

precio = input("Ingrese el precio del producto: ")
precio = int(precio)

cantidad = input("Ingrese la cantidad de producto comprado: ")
cantidad = int(cantidad)

if cantidad>=12:
    precio = precio*0.8

total = precio*cantidad

print("El total de los productos comprados: ", total)

#Ejercicio Ejemplo 2

print()
print("Ejercicio Ejemplo #2")
print()

salario_usuario = input("Ingrese su salario: ")
salario_usuario = float(salario_usuario)

if salario_usuario<=1000:
    salario_usuario = salario_usuario*1.15

print("Su salario es de:", salario_usuario)

#Ejercicio Ejemplo 3

print()
print("Ejercicio Ejemplo #3")
print()

nota = input("Ingrese la nota del estudiante: ")
nota = float(nota)

if nota>=70:
    print("El estudiante ha aprobado")

else:
    print("El estudiante ha reporbado")
print("Siempre pasa por aqui")

#Ejercicio Ejemplo 4

print()
print("Ejercicio Ejemplo #4")
print()

salario = input("Ingrese su salario: ")
salario = float(salario)

if salario>=1000:
    salario = salario*1.15
else:
    salrio = salario*1.2

print("Su salario es de:", salario)

#Ejercicio Ejemplo 5

print()
print("Ejercicio Ejemplo #5")
print()

salario_empleado = input("Ingrese su salario: ")
salario_empleado = float(salario_empleado)
Categoria = input("Ingrese su categoria:")

if Categoria=="1":
    salario_empleado = salario_empleado*1.1
elif Categoria=="2":
    salario_empleado = salario_empleado*1.12
elif Categoria=="3":
    salario_empleado = salario_empleado*1.15
elif Categoria=="4":
    salario_empleado = salario_empleado*1.2

print("Su salario es de:", salario_empleado)

#Ejercicio Ejemplo 6

print()
print("Ejercicio Ejemplo #6")
print()

nota_estudiante = input("Ingrese nota del estudiante: ")
nota_estudiante = float(nota_estudiante)

if nota_estudiante>=90:
    print("Aprobado y descatado")
elif nota_estudiante>=70:
    print("Aprobado ")
elif nota_estudiante>60:
    print("Aplazado ")
else:
    print("Reprobamos")

print("Nos vemos!...")

#Ejercicio 1

print()
print("Ejercicio #1")
print()

numero_1 = input("Ingrese el primer numero:")
numero_2 = input ("Ingrese el segundo numero:")
numero_3 = input("Ingrese el tercer numero:")
numero_4 = input ("Ingrese el cuarto numero:")
numero_1 = int (numero_1)
numero_2 = int (numero_2)
numero_3 = int (numero_3)
numero_4 = int (numero_4)

if numero_1>numero_2:
    print("El numero ", numero_1, " es mayor ")
else:
    print("El numero ", numero_2, " es mayor ")

if numero_3>numero_4:
    print("El numero ", numero_3, " es mayor ")
else:
    print("El numero ", numero_4, " es mayor ")

#Ejercicio 2

print()
print("Ejercicio #2")
print()

num_1 = input("Ingrese el primer numero:")
num_2 = input ("Ingrese el segundo numero:")
num_3 = input("Ingrese el tercer numero:")
num_1 = int (num_1)
num_2 = int (num_2)
num_3 = int (num_3)

numeros = [num_1, num_2, num_3]
numeros.sort(reverse=True)

print("Losnúmeros ordenados de forma descendente son :", numeros)

#Ejercicio 3

print()
print("Ejercicio #3")
print()

year_born = input("Ingrese el año de nacimiento:")
year_born = int(year_born)

if(year_born % 4 == 0 and year_born % 100 != 0) or (year_born % 400 == 0):
    print("El año ingresado si es bisiesto")
else:
    print("El año ingresado no es bisiesto")

#Ejercicio ejemplo 1.2

print()
print("Ejercicio Ejemplo #1.2")
print()

monto = input("Ingrese su monto total de compra: ")
monto = float(monto)

if monto>=1000:
    monto = monto*0.85
    print("Su monto total es de ",monto , "se realizo un 15% de descuento")
else:
    print("Su monto total es de:", monto)

#Ejercicio 2.2 ya se realizo es el mismo ejemplo #5

#Ejercicio  1.2

print()
print("Ejercicio #1.2")
print()

dia_dieta = input("Ingrese el dia que quieras saber de tu dieta: ")


if dia_dieta=="Lunes":
    print("El dia Lunes te toca comer Avena y frutas tropicales")
elif dia_dieta=="Martes":
    print("El dia Martes te toca comer Yogurt y frutas secas")
elif dia_dieta=="Miercoles":
    print("El dia Miercoles te toca tomar Café y galletas saladas")
elif dia_dieta=="Jueves":
    print("El dia Jueves te toca comer Barra energética y jugo de naranja")
else:
    print("No es un dia o caracter valido")

#Ejercicio  2.2

print()
print("Ejercicio #2.2")
print()

print ("Completa los siguientes 5 retos para seguir al siguiente nivel")
reto_1 = input("Cuanto es 2+2?")
reto_1 = int(reto_1)
if reto_1 == 4:
    print("Bien hecho siguiente reto!")
    reto_2 = input("Cuantos dias tiene un año normalmente: ")
    reto_2 = int(reto_2)
    if reto_2 == 365:
        print("Bien hecho siguiente reto!")
        reto_3 = input("Cuantas horas tiene un dia: ")
        reto_3 = int(reto_3)
        if reto_3 == 24:
            print("Bien hecho siguiente reto!")
            reto_4 = input("Cuantas segundos tiene un minuto: ")
            reto_4 = int(reto_4)
            if reto_4 == 60:
                print("Bien hecho siguiente reto!")
                reto_5 = input("Cuantos huesos tiene el cuerpo: ")
                reto_5 = int(reto_5)
                if reto_5 == 206:
                    print("Bien hecho, Siguiente Nivel!")
                else:
                    print("Realice de nuevo el reto #5")
            else:
                print("Realice de nuevo el reto #4")
        else:
            print("Realice de nuevo el reto #3")
    else:
        print("Realice de nuevo el reto #2")
else:
    print("Realice de nuevo el reto #1")


#Ejercicio  3.2

print()
print("Ejercicio #3.2")
print()

repuesto = input("Ingrese cual repuesto necesita 1.Motor 2.Accesorio 3.Limpieza del auto 4.Frenos: ")
precio_repuesto = input("Ingrese el precio del repuesto: ")
precio_repuesto = float(precio_repuesto)


if repuesto=="1":
    precio_repuesto = precio_repuesto*0.85
    print("El precio del repuesto de Motor es de ",precio_repuesto , "se realizo un 15% de descuento")
elif repuesto=="2":
    precio_repuesto = precio_repuesto*0.9
    print("El precio del repuesto de Accesorio es de ",precio_repuesto , "se realizo un 10% de descuento")
elif repuesto=="3":
    precio_repuesto = precio_repuesto*0.95
    print("El precio del repuesto de Limpieza de auto es de ",precio_repuesto , "se realizo un 5% de descuento")
elif repuesto=="4":
    precio_repuesto = precio_repuesto*0.97
    print("El precio del repuesto de Frenos es de ",precio_repuesto , "se realizo un 3% de descuento")
else:
    print("No es un dia o caracter valido")






