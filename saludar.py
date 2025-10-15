def registrar_tiempo(func):
    def wrapper():
        print("Ejecutando función...")
        resultado = func()
        print("Ejecución finalizada")
        return resultado
    return wrapper

@registrar_tiempo
def saludar():
    return "Hola, desarrollador"

# Probando la función
print(saludar())
