#Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:", i)

    resultado = 0
    for i in mi_lista:
        resultado += i

        print(f"El resultado de la suma de mi lista es: {resultado}")

        for i in range(2, 9):
             print(i)

    mi_lista_2 = ["Lunes" , "Martes", "Miercoles", "Jueves", "Viernes"]

for i in mi_lista_2:
    if i != "Lunes":
            print(f"Feliz{i}!")

# While loop
i = 0

while i < 5:
     i += 1
     if i == 3:
          continue
     print(i)
     if i == 4:
          break
     
else:
     print("i es ahora mayor o igual a 5")

     #practica
     # Dada la lista mi_lista_2 = ["Lunes" , "Martes", "Miercoles", "Jueves", "Viernes"]
# Imprime cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
# Pista: Usalos dos tipos loops while y for en el mismo programa para lograrlo
# Resultado:
# martes
# miercoles
# jueves 
# viernes 
# martes
# miercoles 
# jueves
# viernes
# martes
# miercoles
# jueves
# viernes
mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# Inicializamos un contador para el bucle while
repeticiones = 0

# El bucle while se encargará de repetir todo el proceso 3 veces
while repeticiones < 3:
    # El bucle for recorre cada elemento de la lista
    for dia in mi_lista_2:
        # Usamos un condicional para saltarnos el "lunes"
        if dia != "lunes":
            print(dia)
    
    # Incrementamos el contador para no crear un bucle infinito
    repeticiones += 1 