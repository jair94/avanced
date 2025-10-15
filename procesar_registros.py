import pandas as pd

def procesar_registros(registros):
    # 1. Convertir a DataFrame
    df = pd.DataFrame(registros)
    
    # 2. Filtrar eventos con duración > 10
    filtrados = df[df['duracion'] > 10]
    
    # 3. Calcular el promedio de la duración filtrada
    return filtrados['duracion'].mean()

# Ejemplo de uso
data = {
  'evento': ['a', 'b', 'c', 'd'],
  'duracion': [5, 12, 20, 8]
}

print(procesar_registros(data))