import random
# Solicitar al usuario si desea ingresar los valores manualmente o generar una matriz automáticamente
while True:
    opcion = input("¿Desea ingresar los valores manualmente (M) o generar una matriz automáticamente (A)? ").strip().upper()
    if opcion == "M":
        tamanio = int(input("Ingrese el número para el tamaño de filas y columnas (entre 5 y 15): "))
        if 5 <= tamanio <= 15:
            break
        else:
            print("El tamaño debe estar entre 5 y 15. Intente nuevamente.")
    elif opcion == "A":
        tamanio = int(input("Ingrese el número para el tamaño de filas y columnas (entre 5 y 15): "))
        if 5 <= tamanio <= 15:
            # Generar una matriz automáticamente con valores aleatorios 0 o 1
            matriz = [[random.randint(0, 1) for _ in range(tamanio)] for _ in range(tamanio)]
            break
        else:
            print("El tamaño debe estar entre 5 y 15. Intente nuevamente.")
    else:
        print("Opción no válida. Por favor, ingrese 'M' para ingresar manualmente o 'A' para generar automáticamente.")

# Crear la matriz vacía
matriz = []

# Llenar la matriz con valores proporcionados por el usuario o generados automáticamente
for i in range(tamanio):
    fila = []
    for j in range(tamanio):
        if opcion == "M":
            while True:
                valor = int(input(f"Ingrese el valor para la posición ({i+1},{j+1}): "))
                if valor == 0 or valor == 1:
                    break
                else:
                    print("El valor debe ser 0 o 1. Intente nuevamente.")
        else:
            valor = random.randint(0, 1)  # Generar valores aleatorios 0 o 1 automáticamente
        fila.append(valor)
    matriz.append(fila)
# Imprimir la matriz
print("La matriz original es:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea después de cada fila
    
# Modificar la matriz: poner 1 en la diagonal principal (x=y)
for i in range(tamanio):
    matriz[i][i] = 1

# Imprimir la matriz modificada
print("Paso 1: colocar 1 en la diagonal principal")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea después de cada fila
    
# Proceso de ajustar las filas según las relaciones
for i in range(tamanio):
    for j in range(tamanio):
        if i != j and matriz[i][j] == 1:
            # Si matriz[i][j] es 1, ajustar la fila i usando fila j
            for k in range(tamanio):
                if matriz[j][k] == 1:
                    matriz[i][k] = 1

# Agregar una columna en la posición 0 con números del 1 hasta la cantidad de filas
for i in range(tamanio):
    matriz[i].insert(0, i + 1)

# Agregar una fila en la posición 0 con números del 1 hasta la cantidad de columnas
matriz.insert(0, [x for x in range(0, tamanio + 1)])

# Colocar una 'x' en la posición (0, 0)
matriz[0][0] = 'x'

# Imprimir la matriz con las filas y columnas adicionales
print("Paso 2: ")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea después de cada fila

# Función para contar los 1 en una fila sin contar la columna 0
def contar_unos_en_fila(fila):
    return sum(fila[1:])

# Contar la cantidad de 1 en cada fila (sin contar la columna 0)
cantidad_unos_fila = [contar_unos_en_fila(fila) for fila in matriz]

# Crear una lista de tuplas que contienen la cantidad de 1 y el índice de la fila
filas_con_cantidad = [(cantidad, indice) for indice, cantidad in enumerate(cantidad_unos_fila)]

# Ordenar la lista de filas en función de la cantidad de 1 de mayor a menor
filas_con_cantidad.sort(reverse=True, key=lambda x: x[0])

# Crear la matriz ordenada en el nuevo orden
matriz_ordenada = [matriz[indice] for cantidad, indice in filas_con_cantidad]

# Imprimir la matriz ordenada
print("Paso 4: Ordenar filas por cantidad de 1 ")
for fila in matriz_ordenada:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea después de cada fila

# Función para contar los 1 en una columna sin contar la fila 0
def contar_unos_en_columna(matriz, columna):
    return sum(1 for fila in matriz[1:] if fila[columna] == 1)

# Encontrar las columnas con más unos y ordenarlas de mayor a menor
columnas_con_mas_unos = sorted(range(1, tamanio+1), key=lambda columna: contar_unos_en_columna(matriz_ordenada, columna))

# Crear una lista con las columnas ordenadas por cantidad de unos
columnas_ordenadas = [0] + [matriz_ordenada[0][col] for col in columnas_con_mas_unos]

# Imprimir todas las columnas en vertical en el nuevo orden
print("Paso 5: Ordenar columnas por cantidad de 1 ")
for fila in matriz_ordenada:
    columnas_texto = " ".join(str(fila[col]) for col in columnas_ordenadas)
    print(columnas_texto)
