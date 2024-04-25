    # Ejercicio 1

print("Ejercicio #1")
print()
nombre = input("Ingresa tu nombre :")
apellido_1 = input("Ingresa tu primer apellido :") 
apellido_2 = input("Ingresa tu segundo apellido :")

print("Bienvenido, estimado ",nombre ,apellido_1 ,apellido_2)

# Ejercicio 2

print ()
print("Ejercicio #2")
print()

numero_1 = input("Ingrese el primer número: ")
numero_2 = input("Ingrese el segundo número: ")
numero_1 = int(numero_1)
numero_2 = int(numero_2)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

print("El resultado de los numeros es: Suma:", suma, "Resta:", resta, "Multiplicacion:", multiplicacion, "Division:", division)

#Ejercicio 3

print ()
print("Ejercicio #3")
print()
l_cuadrado = input("Coloca el valor del lado del cuadrado para calcular el area y su perimetro:")
l_cuadrado = int(l_cuadrado)

perimetro = l_cuadrado+l_cuadrado+l_cuadrado+l_cuadrado
area = l_cuadrado*l_cuadrado

print("El perimetro del cuadrado es de: ", perimetro, " y el area es de: ", area)

#Ejercicio 4

print ()
print("Ejercicio #4")
print()
edad_luis = input("Coloca la edad de Luis: ")
edad_pedro = input("Coloca la edad de Pedro: ")
edad_luis = int(edad_luis)
edad_pedro = int(edad_pedro)

print("Edades antes del cambio Luis: ",edad_luis, " Pedro: ",edad_pedro)

edad_temp = edad_luis
edad_luis = edad_pedro
edad_pedro = edad_temp

print("Las edades despues del cambio serian Luis tiene: ",edad_luis, " y pedro: ",edad_pedro )

#Ejercicio 5

print ()
print("Ejercicio #5")
print()
primer_num = input("Coloca el numero que quieras elevar: ")
segundo_num = input("Coloca el numero de la potencia:")
primer_num = int(primer_num)
segundo_num = int(segundo_num)

potencia = primer_num**segundo_num
print("El numero ",primer_num," elevado a la ", segundo_num, " es igual a ", potencia)

#Ejercicio 1.2
print ()
print("Ejercicio #1.2")
print()

producto = input("Ingresa el nombre del producto:")
cantidad = input("Ingrese la cantidad del producto:")
precio = input("Ingrese el precio unitario del producto:")
cantidad = int(cantidad)
precio = float (precio)

precio_total = (precio*1.13)*cantidad
print("Haz comprado ",producto," una cantidad de ", cantidad, " con un costo unitario de ", precio, " y todo junto seria un total de ", precio_total, "con iva")

#Ejercicio 2.2
print ()
print("Ejercicio #2.2")
print()

print("Vamos a calcular tu tiempo laborado")
horas_laboradas = input("Ingresa cuantas horas has laborado:")
minutos_laboradas = input("Ingresa cuantos minutos aparte de las horas has laborado:")
segundo_laborados = input("Ingresa cuantos segundos aparte de los minutos has laborado:")
horas_laboradas = int(horas_laboradas)
minutos_laboradas = int(minutos_laboradas)
segundo_laborados = int(segundo_laborados)

segundos_trabajo_total = (horas_laboradas*3600)+(minutos_laboradas*60)+segundo_laborados

print("Haz laborado un total de:", segundos_trabajo_total, "segundos")\

#Ejercicio 3.2
print ()
print("Ejercicio #3.2")
print()

nombre_usuario = input("Ingresa su nombre completo:")
cedula_usuario = input("Ingresa su cedula:")
salario_usuario = input("Ingresa su salario bruto:")
salario_usuario = float(salario_usuario)

ccss = (salario_usuario*0.08)
banco_popular = (salario_usuario*0.01)
deducciones = ccss+banco_popular
salario_total= salario_usuario-deducciones

print("Empleado: ", nombre_usuario)
print("Identificacion: ", cedula_usuario)
print("Salario Bruto: ", salario_usuario)
print("CCSS(8%): ", ccss)
print("Banco Popular(1%): ",banco_popular)
print("Total deducciones:", deducciones)
print("Salario neto: ", salario_total)

#Ejercicio 4.2
print ()
print("Ejercicio #4.2")
print()

producto_comparacion = input("Ingresa el nombre del producto:")
precio_sj = input("Ingrese el precio del producto en San Jose:")
precio_alj = input("Ingrese el precio del producto en Alajuela:")
precio_hrd =input("Ingrese el precio del producto en Heredia:")
precio_sj = int(precio_sj)
precio_alj = int(precio_alj)
precio_hrd = int(precio_hrd)

promedio_producto = (precio_sj+precio_alj+precio_hrd)/3
print("Producto: ", producto_comparacion)
print("Precio en San Jose: ", precio_sj)
print("Precio en Alajuela: ", precio_alj)
print("Precio en Heredia: ", precio_hrd)
print("Precio promedio: ",promedio_producto)

#Ejercicio 5.2
print ()
print("Ejercicio #5.2")
print()

nombre_vendedor = input("Ingresa su nombre completo:")
ventas_cant = input("Ingresa la cantidad de unidades vendidas:")
ventas_precio =input("Ingresa el precio de las unidades vendidas:")
ventas_cant = int(ventas_cant)
ventas_precio = float(ventas_precio)

if(ventas_precio<=20000):
    comision = (ventas_precio*0.03)*ventas_cant
elif(ventas_precio>20000 and 50000):
    comision = (ventas_precio*0.05)*ventas_cant
elif(ventas_precio>=50000):
    comision = (ventas_precio*0.1)*ventas_cant

print("Empleado: ", nombre_vendedor)
print("Unidades vendidas", ventas_cant)
print("Precio del articulo:", ventas_precio)
print("Comision:", comision)


