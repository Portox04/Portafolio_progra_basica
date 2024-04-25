#Ejercicio 1
print("Ejercicio #1")
print()
f1_lap_total = float(0)
f1_pit_total = float (0)

for i in range (10):
    f1_time_pit = input("Ingresa el tiempo de la pits: ")
    f1_time_pit = float(f1_time_pit)
    f1_time_lap = input("Ingresa el tiempo de los vuelta: ")
    f1_time_lap = float(f1_time_lap)
    
    f1_lap_total+= f1_time_lap
    f1_pit_total+= f1_time_pit

f1_prom_lap = f1_lap_total/10
f1_prom_pit = f1_pit_total/10

f1_porcentaje = (f1_prom_pit/f1_prom_lap)*100

print("Tiempo promedio por vuelta:", f1_prom_lap)
print("Tiempo promedio en pits:", f1_prom_pit)
print("Porcentaje en los pits por vuelta es", f1_porcentaje, "%")

#Ejercicio 2
print()
print("Ejercicio #2")
print()

n_100 = int(0)
n_100_120 = int(0)
n_121_130 = int(0)
n_131_140 = int(0)
n_140 = int(0)
tall_total = float(0)

cantidad = input("Ingresa la cantidad de niños para comparar alturas:")
cantidad = int(cantidad)

for x in range (cantidad):
    add_kid = input("Cual es la estatura del niño(cm):")
    add_kid = float(add_kid)
    if add_kid<100:
        n_100+=1
    elif add_kid>=100 and add_kid<=120:
        n_100_120+=1
    elif add_kid>=121 and add_kid<=130:
        n_121_130+=1
    elif add_kid>=131 and add_kid<=140:
        n_131_140+=1
    elif add_kid>=141 :
        n_140+=1
    tall_total+=add_kid
       
prom_tall =tall_total/cantidad

print("Hay un promedio de ",prom_tall)
print("Hay",n_100, "niños que mide menos de 100cm")
print("Hay",n_100_120, "niños que mide mas de 100cm y menos de 120cm")
print("Hay",n_121_130, "niños que mide mas de 121cm y menos de 130cm")
print("Hay",n_131_140, "niños que mide mas de 131cm y menos de 140cm")
print("Hay",n_140, "niños que mide mas de 140cm")

#Ejercicio 3
print()
print("Ejercicio #3")
print()

valor = int(0)
numero = input("Ingresa un numero para dividirlo entre si 10 veces:")
numero = int(numero)
while valor==10:
    if numero%numero==0:
        print("La suma de los numeros pares es:", pares)



