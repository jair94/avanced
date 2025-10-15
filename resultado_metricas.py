import numpy as np

def analizar_metricas(valores):
    promedio = np.mean(valores)
    maximo = np.max(valores)
    desviacion = np.std(valores)
    
    return {
        'promedio': promedio,
        'maximo': maximo,
        'desviacion': desviacion
    }
# Ejemplo de uso
resultado = analizar_metricas([10, 20, 30])
print(resultado)