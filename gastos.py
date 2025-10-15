#1 Importar Librerias
import pandas as pd
import matplotlib.pyplot as plt # Libreria para graficos

#2 Leer o declarar los datos
df = pd.read_excel('gastos.xlsx')
print(df)
# borrar datos nulos
df.dropna(inplace=True)
print(df.isnull().sum())
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.info())
#6) procesamiento de datos
print(df)
gastos = df[df['Clase']=="Gastos"]
print(gastos)
ingresos = df[df['Clase']=="Ingresos"]
print(ingresos)