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