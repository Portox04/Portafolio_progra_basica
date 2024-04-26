#Semana 8
#Ejercicio 1
def convertir_binario(numero):
    resultado_binario = ""
    while numero > 0:
        resultado_binario = str(numero % 2) + resultado_binario
        numero //= 2
    print("El número en binario es:", resultado_binario)

def convertir_octal(numero):
    resultado_octal = ""
    while numero > 0:
        resultado_octal = str(numero % 8) + resultado_octal
        numero //= 8
    return resultado_octal

def convertir_hexadecimal(numero):
    resultado_hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            resultado_hexadecimal = str(residuo) + resultado_hexadecimal
        else:
            resultado_hexadecimal = chr(ord('A') + residuo - 10) + resultado_hexadecimal
        numero //= 16
    return resultado_hexadecimal

def mostrar_conversiones(numero):
    print("Número:", numero)
    convertir_binario(numero)
    print("Número en octal:", convertir_octal(numero))
    print("Número en hexadecimal:", convertir_hexadecimal(numero))

# Programa principal
numero = int(input("Ingrese un número entero: "))
mostrar_conversiones(numero)
