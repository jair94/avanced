estudiantes = {
    "nombre": ["Luis", "Ana", "Marta", "Carlos", "Lucía"],
    "materias": ["Python", "Java", "Analisis", "Base de Datos", "Arquitectura"],
    "notas": [5.0, 4.5, 3.0, 4.0, 2.5]

}

for estudiante in estudiantes:
    print(estudiante)

#|---------------------------------------------------------------|
for estudiante in estudiantes:
    print(f"{estudiante}: {estudiantes[estudiante]}")   

#|---------------------------------------------------------------|
# Acceder a los datos de un estudiante en particular
datos = estudiantes["nombre"]
for estudiante in datos:
    index = datos.index(estudiante)
    notas = estudiantes["notas"]
    materias = estudiantes["materias"]

    print(f"Estudiante: {estudiante}, Materia: {materias[index]}, Nota: {notas[index]}")
    print(index)
    
