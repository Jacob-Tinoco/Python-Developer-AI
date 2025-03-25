"""
Script para la automatización de solicitudes
Autor: Jacob Tinoco
Fecha: 2025
Derechos Reservados. Este script está protegido por derechos de autor. 
Uso permitido únicamente para fines personales o educativos.
"""
import os
from datetime import datetime, timezone
from transformers import pipeline

# Función para leer solicitudes desde un archivo
def leer_solicitudes(ruta_archivo):
    """
    Lee las solicitudes desde un archivo de texto.
    
    :param ruta_archivo: Ruta del archivo de texto que contiene las solicitudes.
    :return: Lista de solicitudes leídas.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines() if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        return []

# Función para escribir resultados en un archivo
def escribir_resultados(ruta_archivo, resultados):
    """
    Escribe los resultados procesados en un archivo de texto.
    
    :param ruta_archivo: Ruta del archivo donde se guardarán los resultados.
    :param resultados: Lista de resultados procesados.
    """
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("ID | Fecha | Hora Solicitud (UTC) | Hora Respuesta (UTC) | Clasificación | Positivo/Negativo/Duda | ID Solicitud | Solicitud Procesada\n")
            for resultado in resultados:
                archivo.write(" | ".join(resultado) + "\n")
    except Exception as e:
        print(f"Error al escribir en el archivo {ruta_archivo}: {e}")

# Función para clasificar solicitudes
def clasificar_solicitud(solicitud, clasificador):
    """
    Clasifica una solicitud en categorías específicas y en positiva/negativa.
    
    :param solicitud: Texto de la solicitud.
    :param clasificador: Modelo de clasificación de texto.
    :return: Tupla con la categoría específica y la clasificación positiva/negativa.
    """
    try:
        resultado = clasificador(solicitud)[0]
        categoria = resultado["label"]
        confianza = resultado["score"]

        # Verificar si la confianza es baja
        if confianza < 0.6:
            print(f"Solicitud con baja confianza: {solicitud} (Confianza: {confianza})")
            # Guardar para revisión manual
            with open("baja_confianza.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{solicitud} | Confianza: {confianza}\n")

        # Clasificación específica
        if "factura" in solicitud.lower() or "facturación" in solicitud.lower():
            clasificacion = "Facturación"
        elif "dañado" in solicitud.lower() or "devolución" in solicitud.lower():
            clasificacion = "Insatisfacción del Producto"
        elif "satisfecho" in solicitud.lower() or "excelente" in solicitud.lower():
            clasificacion = "Satisfacción del Producto"
        elif "envío" in solicitud.lower():
            clasificacion = "Preguntas de Envío"
        elif "producto" in solicitud.lower():
            clasificacion = "Preguntas del Producto"
        elif "pago" in solicitud.lower():
            clasificacion = "Preguntas de Métodos de Pago"
        elif "duda" in solicitud.lower() or "pregunta" in solicitud.lower() or solicitud.endswith("?"):
            # Clasificar como "Duda del cliente" si contiene palabras clave o es una pregunta
            clasificacion = "Duda del cliente"
            categoria = "Duda"  # Cambiar la categoría general a "Duda"
        else:
            clasificacion = "General"

        return clasificacion, categoria
    except Exception as e:
        print(f"Error al clasificar la solicitud: {e}")
        return "Error", "NEGATIVE"

# Función para generar un nombre único para el archivo de resultados
def generar_nombre_archivo(base_carpeta):
    """
    Genera un nombre único para el archivo de resultados en la carpeta 'results'.
    
    :param base_carpeta: Carpeta donde se guardarán los resultados.
    :return: Ruta completa del archivo con nombre único.
    """
    fecha_actual = datetime.now(timezone.utc).strftime("%y%m%d")
    contador = 1
    
    while True:
        nombre_archivo = f"respuestas_{fecha_actual}_{contador:02d}.txt"
        ruta_completa = os.path.join(base_carpeta, nombre_archivo)
        if not os.path.exists(ruta_completa):
            return ruta_completa
        contador += 1

# Función principal
def main():
    """
    Función principal que coordina la lectura, clasificación y escritura de las solicitudes.
    """
    # Usar la ruta relativa para el archivo de solicitudes
    ruta_solicitudes = os.path.join(os.path.dirname(__file__), "data", "solicitudes.txt")

    # Verificar si la ruta del archivo es válida
    if not os.path.exists(ruta_solicitudes):
        print(f"Error: No se encontró el archivo de solicitudes en la ruta predeterminada: {ruta_solicitudes}")
        return

    # Crear la carpeta 'results' si no existe
    carpeta_resultados = os.path.join(os.path.dirname(__file__), "results")
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)
        print("La carpeta 'results' no existía, pero ha sido creada.")

    # Generar el nombre único para el archivo de resultados
    ruta_resultados = generar_nombre_archivo(carpeta_resultados)

    # Cargar modelo de clasificación
    try:
        clasificador = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    except Exception as e:
        print(f"Error al cargar el modelo de clasificación: {e}")
        return

    # Leer solicitudes
    solicitudes = leer_solicitudes(ruta_solicitudes)
    if not solicitudes:
        print("No se encontraron solicitudes para procesar. Asegúrate de que el archivo no esté vacío.")
        return

    # Procesar solicitudes
    resultados = []
    for idx, solicitud in enumerate(solicitudes, start=1):
        # Registrar hora de la solicitud
        hora_solicitud = datetime.now(timezone.utc).strftime("%H:%M:%S")
        fecha_solicitud = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        # Clasificar solicitud
        clasificacion, categoria = clasificar_solicitud(solicitud, clasificador)

        # Registrar hora de la respuesta
        hora_respuesta = datetime.now(timezone.utc).strftime("%H:%M:%S")

        # Formatear resultado
        resultado = [
            str(idx),
            fecha_solicitud,
            hora_solicitud,
            hora_respuesta,
            clasificacion,
            "Positiva" if categoria == "POSITIVE" else "Duda" if categoria == "Duda" else "Negativa",
            str(idx),  # ID de la solicitud
            solicitud  # Texto de la solicitud procesada
        ]
        resultados.append(resultado)

    # Escribir resultados en archivo
    escribir_resultados(ruta_resultados, resultados)
    print(f"Resultados guardados en: {ruta_resultados}")

if __name__ == "__main__":
    main()
