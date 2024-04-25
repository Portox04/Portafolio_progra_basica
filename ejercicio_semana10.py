#Ejercicio 1

botonera = [[1,2,3],
            [4,5,6],
            [7,8,9]]


def recorrer_matriz(matriz):
    boton = int(input("Indique el # de boton que quieres colocar del 1 al 9: "))
    numero_filas = len(matriz)
    for fila in range(numero_filas):
        numero_columnas = len(matriz[fila])
        for columna in range(numero_columnas):
            elemento_en_matriz = matriz[fila][columna]
            if elemento_en_matriz == boton:
                print(f"El boton esta ubicado en la fila {fila}, y columna {columna}")


recorrer_matriz(botonera)
            
        
# Ejercicio 2

nota =[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

def colocacion_notas(notas):
    numero_fila = len(notas)
    for filas in range(numero_fila):
        numero_columna = len(notas[filas])
        for columnas in range(numero_columna):
            print(f"Coloque la nota del estudiante {filas+1}, de la actividad {columnas+1}: ")
            notas[filas][columnas] = int(input())

def nota_final():
    notas_finales = []  
    for fila in nota:
        suma_notas = sum(fila)  
        notas_finales.append(suma_notas)  
    for i in range(len(notas_finales)):
        print(f"La nota final del estudiante {i + 1} es de: {notas_finales[i]}")

colocacion_notas(nota)
nota_final()



