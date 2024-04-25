#Semana 9

#Ejercicio #1

print("Ejercicio #1")
days = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado", "Domingo"]
km = [0,0,0,0,0,0,0]
total_km = 0

def record_km():
    global total_km
    for x in range (len(days)):
        print("Introduce los KM que hiciste el dia", days[x])
        new_km = int(input())
        km[x] = new_km
        total_km+= new_km


record_km()
for y in range (len(days)):
    print("El dia",days[y], "hiciste ", km[y], "KM")
print("El total de la semana es de ", total_km, "KM")

print()
print("Ejercicio #2")
print()

name_butaca = ["","","","","","","","","",""]


def record_name():
    for butaca in range(len(name_butaca)):
        print("Indique el nombre de la persona que le toca la butaca", butaca+1)
        name = input()
        name_butaca[butaca] = name

record_name()
for butacas in range (len(name_butaca)):
    print("La butaca",butacas+1, "es de ", name_butaca[butacas])

print()
print("Ejercicio #3")
print()


palabra = input("Ingrese la palabra que quieres darle vuelta letra por letra")

cantidad = len(palabra)

while cantidad>0:
    print(palabra[cantidad-1])
    cantidad-=1

print()
print("Ejercicio #4")
print()

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado", "Domingo"]
earnings = [0,0,0,0,0,0,0]
low_money = float('inf')
day_low = None

def record_money():
    global low_money
    global day_low
    for dia in range (len(dias)):
        print("Introduce el monto que hiciste el dia", dias[dia])
        earn = int(input())
        earnings[dia] = earn
        if low_money >= earn:
            low_money = earn
            day_low = dias[dia]
            
record_money()
for dia_index in range (len(dias)):
    print("El dia",dias[dia_index], "hiciste ", earnings[dia_index] )
print("El dia",day_low , "fue el dia que hiciste menos e hiciste ",low_money)
