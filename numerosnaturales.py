def generar_numeros(inicio, fin):
    numeros = []
    if inicio > fin:
        for numero in range(100, 1, -1):  # paso -1 para ir hacia abajo
            numeros.append(numero)
    else:
        for numero in range(inicio, fin + 1):  # paso +1 para ir hacia arriba
            numeros.append(numero)
    return numeros  

inicio = int(input("Ingresa el valor inicial: "))
fin = int(input("Ingresa el valor final: "))   
numeros_generados = generar_numeros(inicio, fin)
print("Números generados:", numeros_generados)