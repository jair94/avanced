#Calcular númerosuna cantidad X de Pares
import sys

def pares_normal(num):
    numeros = []
    for i in range(1, num + 1):
        numeros.append(i * 2)
    return numeros

pares_generados= pares_normal(10000)
#print(pares_generados)
print("Memoria usada por la función generar_pares:", sys.getsizeof(pares_generados), "bytes")

#|---------------------------------------------------------------|
#Usando Generadores
def pares_generador(num):
    for i in range(1, num + 1):
        yield i * 2
pares_generados= pares_generador(10000)
#print(pares_generados)
#print(list(pares_generados))
print("Memoria usada por la función generar_pares:", sys.getsizeof(pares_generados), "bytes")