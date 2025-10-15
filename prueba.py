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

# Ejemplo de uso
eventos = ["Concierto de Rock", "Exposición de Arte", "Feria de Tecnología"]
procesar_eventos(eventos)
