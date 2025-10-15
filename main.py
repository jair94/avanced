import math  # Necesario para la función de raíz cuadrada

# Funciones para las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

def raiz(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: No se puede calcular la raíz de un número negativo."

def potencia(base, exponente):
    return base ** exponente

# Programa principal
print("Bienvenido a la calculadora")

while True:
    print("\nElige una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Potencia")
    print("7. Salir")

    opcion = input("Ingresa el número de la operación: ")

    if opcion == "7":
        print("¡Hasta luego!")
        break

    if opcion in ["1", "2", "3", "4", "6"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))
        elif opcion == "6":
            print("Resultado:", potencia(num1, num2))

    elif opcion == "5":
        num = float(input("Ingresa el número: "))
        print("Resultado:", raiz(num))
    
    else:
        print("Opción no válida, intenta de nuevo.")
