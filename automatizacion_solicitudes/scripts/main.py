import os
from datetime import datetime
from utils import leer_solicitudes, escribir_resultados, clasificar_solicitud
from transformers import pipeline

# Configuración principal
def main():
    # Definir rutas
    ruta_solicitudes = os.path.join("data", "solicitudes.txt")
    ruta_resultados = os.path.join("results", "resultados.txt")

    # Verificar si las carpetas existen
    if not os.path.exists("data"):
        print("Error: La carpeta 'data' no existe.")
        return
    if not os.path.exists("results"):
        os.makedirs("results")
        print("La carpeta 'results' no existía, pero ha sido creada.")

    # Cargar modelo de clasificación
    try:
        clasificador = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    except Exception as e:
        print(f"Error al cargar el modelo de clasificación: {e}")
        return

    # Leer solicitudes
    solicitudes = leer_solicitudes(ruta_solicitudes)
    if not solicitudes:
        print("No se encontraron solicitudes para procesar.")
        return

    # Procesar solicitudes
    resultados = []
    for idx, solicitud in enumerate(solicitudes, start=1):
        # Registrar hora de la solicitud
        hora_solicitud = datetime.utcnow().strftime("%H:%M:%S")
        fecha_solicitud = datetime.utcnow().strftime("%Y-%m-%d")

        # Clasificar solicitud
        clasificacion, categoria = clasificar_solicitud(solicitud, clasificador)

        # Registrar hora de la respuesta
        hora_respuesta = datetime.utcnow().strftime("%H:%M:%S")

        # Formatear resultado
        resultado = [
            str(idx),
            fecha_solicitud,
            hora_solicitud,
            hora_respuesta,
            clasificacion,
            "Positiva" if categoria == "POSITIVE" else "Negativa"
        ]
        resultados.append(resultado)

    # Escribir resultados en archivo
    escribir_resultados(ruta_resultados, resultados)
    print(f"Resultados guardados en: {ruta_resultados}")

if __name__ == "__main__":
    main()