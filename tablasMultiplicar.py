# Tablas de multiplicar del 1 al 10

for i in range(1, 11):  
    print(f"\nTabla del {i}")
    print("-" * 15)
    for j in range(1, 11): 
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
