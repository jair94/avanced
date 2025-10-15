
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

if numero2 != 0:
    division = numero1 / numero2
    print(f"El resultado de dividir {numero1} entre {numero2} es: {division}")
else:
    print("Error: No se puede dividir entre cero.")