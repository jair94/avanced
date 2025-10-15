#uso de pandas
#1 Importar la librería
import pandas as pd

#2 Leer o declarar los datos
estudiantes = {
    "nombre": ["Luis", "Ana", "Marta", "Carlos", "Lucía"],
    "materias": ["Python", "Java", "Analisis", "Base de Datos", "Arquitectura"],
    "edad": [20, None, 22, 23, 20],
    "notas": [5.0, 4.5, 3.0, 4.0, 2.5]
}

#3 crear un DataFrame
df = pd.DataFrame(estudiantes)

#4 Visualizar los metadatos
#print(df)
#print(df.info())
#print(df.describe())

#5 Limpiar los datos
# Contar valores nulos
print(df.isnull().sum())
df.dropna(inplace=True)
print(df)

#6 datos duplicados
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)    
print(df)

#7 Filtrar datos
# Filtrar estudiantes con notas mayores a 3.0
filtro_notas = df['notas'] >= 3.0
estudiantes_aprobados = df[filtro_notas]    
print(estudiantes_aprobados)

# Filtrar estudiantes pierden el año (notas < 3.0)
filtro_reprobados = df['notas'] < 3.0
estudiantes_reprobados = df[filtro_reprobados]    
print(estudiantes_reprobados)

# Filtar estudiantes con la nota mas baja
#nota_minima = df['notas'].min()
#filtro_nota_minima = df['notas'] == nota_minima
#estudiante_nota_minima = df[filtro_nota_minima]
#print(estudiante_nota_minima)
print(df[df['notas'] == df['notas'].min()])
# Filtar estudiantes con la nota mas alta
#nota_maxima = df['notas'].max()
#filtro_nota_maxima = df['notas'] == nota_maxima
#estudiante_nota_maxima = df[filtro_nota_maxima]
#print(estudiante_nota_maxima)
print(df[df['notas'] == df['notas'].max()])