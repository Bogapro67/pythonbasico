print("======== Mi Super Calculadora ==========")

num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

def suma(num_1, num_2):
    return num_1 + num_2

def resta(num_1, num_2):
    return num_1 - num_2

def multiplicacion(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    if num_2 == 0:
        return "Error: No se puede dividir entre cero"
    return num_1 / num_2


if operacion == "+":
    resultado = suma(num_1, num_2)

elif operacion == "-":
    resultado = resta(num_1, num_2)

elif operacion == "*":
    resultado = multiplicacion(num_1, num_2)

elif operacion == "/":
    resultado = division(num_1, num_2)

else:
    resultado = "Operación no válida"

print("Resultado:", resultado)