# =========================
# MISIÓN 1 – Decorador de seguimiento
# =========================

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


# =========================
# MISIÓN 2 – Validar eventos
# =========================

def validar_eventos(func):
    def wrapper(eventos):
        if not eventos:  # Lista vacía o None
            raise ValueError("No se pueden registrar eventos vacíos")
        return func(eventos)
    return wrapper

@validar_eventos
def procesar_eventos(eventos):
    for evento in eventos:
        print(f"Evento registrado: {evento}")


# =========================
# MISIÓN 3 – Analizar métricas con NumPy
# =========================

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


# =========================
# MISIÓN 4 – Procesar registros con pandas
# =========================

import pandas as pd

def procesar_registros(registros):
    df = pd.DataFrame(registros)
    filtrados = df[df['duracion'] > 10]
    return filtrados['duracion'].mean()


# =========================
# MISIÓN 5 – Pruebas automáticas
# =========================

def probar_funciones():
    # 1. Prueba de saludar
    assert saludar() == "Hola, desarrollador", "Error en saludar()"
    
    # 2. Prueba de analizar_metricas
    resultado_metricas = analizar_metricas([10, 20, 30])
    assert resultado_metricas['promedio'] == 20.0, "Error en analizar_metricas()"
    
    # 3. Prueba de procesar_registros
    datos = {
        'evento': ['a', 'b', 'c', 'd'],
        'duracion': [5, 12, 20, 8]
    }
    assert procesar_registros(datos) == 16.0, "Error en procesar_registros()"
    
    print("Pruebas completadas exitosamente.")

# Ejecutar pruebas
probar_funciones()
