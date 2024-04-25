# Ejercicio 1

print()
print("Ejercicio 1")

a = input("Ingrese el valor de a:")
b = input("Ingrese el valor de b:")
c = input("Ingrese el valor de c:")
d = input("Ingrese el valor de d:")

print (d,c,b,a)

#Ejercicio 2

print()
print("Ejercicio 2")

edad =  input("Coloca tu edad:")

edad = int(edad)
suma = edad + 5

print("Dentro de 5 años, tendrá: ", suma)

#Ejercicio 3

print()
print("Ejercicio 3")

valor_a = input("Ingrese el valor de a:")
valor_b = input("Ingrese el valor de b:")

valor_a = int(valor_a)
valor_b = int(valor_b)

operacion = (valor_a+valor_b)*2/3

print("El resulato de la operacion (A+B)2/3 es =", operacion)

#Ejercicio 4

print()
print("Ejercicio 4")

valor_n = input("Ingrese un numero para calcular el cuadrado y el cubo de este:")
valor_n = int (valor_n)

valor_n_cubo = valor_n**3
valor_n_cuadrado = valor_n**2

print("El cuadrado del numero ingresado es:", valor_n_cuadrado)
print("El cubo del numero ingresado es:", valor_n_cubo)

#Ejercicio 5

print()
print("Ejercicio 5")

altura = input("Ingrese la altura del rectangulo: ")
ancho = input("Ingrese el ancho del rectangulo: ")

ancho = int (ancho)
altura = int (altura)

area = ancho*altura
perimetro = 2*ancho+2*altura

print("El perimetro del rectangulo ingresado:", perimetro)
print("El area del rectangulo ingresado:", area)

#Ejercicio 6

print()
print("Ejercicio 6")

km = input("Ingrese la distancia de su casa a la universidad en km: ")
costo_km = input("Ingrese el costo por km: ")
frecuencia = input("Ingrese la cantidad de dias que va a la U:")

km = int (km)
costo_km = int (costo_km)
frecuencia = int(frecuencia)

costo_viaje = (km*costo_km)*2
viaje_total = ((costo_viaje)*frecuencia)*15

print("El costo por Cuatrimestre es de:", viaje_total)

#Ejercicio 7

print()
print("Ejercicio 7")

print("Acontinuacion coloca la edad de 5 personas para calcular la edad promedio")
edad_1 = input("Ingrese edad de la primera persona:")
edad_2 = input("Ingrese edad de la segunda persona:")
edad_3 = input("Ingrese edad de la tercera persona:")
edad_4 = input("Ingrese edad de la cuarta persona:")
edad_5 = input("Ingrese edad de la quinta persona:")

edad_1 = int(edad_1)
edad_2 = int(edad_2)
edad_3 = int(edad_3)
edad_4 = int(edad_4)
edad_5 = int(edad_5)

edad_promedio = (edad_1 + edad_2 + edad_3 + edad_4 + edad_5)/5

print("El promedio de las edades es:", edad_promedio)

#Ejercicio 8

print()
print("Ejercicio 8")

work_time = input("Cuantas horas semanales trabaja: ")
work_money = input("Cual es el precio por hora: ")

work_time = int (work_time)
work_money = int (work_money)
work_moth_total = (work_time*4.2)*work_money
work_moth_salary = work_moth_total-(work_moth_total*0.105+work_moth_total*0.05)


print("Tu salario mensual es de:", work_moth_total)
print("Tu salario mensual con los rebajos correspondientes es de:", work_moth_salary)


#Ejercicio 9

print()
print("Ejercicio 9")

salary_moth = input("Cuanto es su ingreso mensual: ")
expenses_moth = input("Cuatos son sus gastos mensuales de alimentacion: ")

salary_moth = int (salary_moth)
expenses_moth = int (expenses_moth)
food_moth = (100*expenses_moth)/salary_moth
available_moth = 100-food_moth

print("Haces un gasto de ", food_moth,"% de alimentacion mensual" )

print("Y te queda libre un ", available_moth ,"%" )
