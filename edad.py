# Función para validar si una persona es mayor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

# Función para pedir la edad al usuario y validar que sea un numero valido
def pedir_edad():
    while True:
        entrada = input("Ingresa tu edad: ")
        if entrada.isdigit():
            edad = int(entrada)
            return edad
        else:
            print("Entrada no válida. Por favor ingresa un número entero.")

# Programa principal
edad_usuario = pedir_edad()
print(es_mayor_de_edad(edad_usuario))
