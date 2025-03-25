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

def leer_solicitudes(ruta_archivo):
    """
    Lee las solicitudes desde un archivo de texto.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines() if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        return []

def escribir_resultados(ruta_archivo, resultados):
    """
    Escribe los resultados procesados en un archivo de texto.
    """
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("ID | Fecha | Hora Solicitud (UTC) | Hora Respuesta (UTC) | Clasificación | Positivo/Negativo/Duda | ID Solicitud | Solicitud Procesada\n")
            for resultado in resultados:
                archivo.write(" | ".join(resultado) + "\n")
    except Exception as e:
        print(f"Error al escribir en el archivo {ruta_archivo}: {e}")

def clasificar_solicitud(solicitud, clasificador):
    """
    Clasifica una solicitud en categorías específicas y en positiva/negativa.
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
            clasificacion = "Duda del cliente"
            categoria = "Duda" 
        else:
            clasificacion = "General"

        return clasificacion, categoria
    except Exception as e:
        print(f"Error al clasificar la solicitud: {e}")
        return "Error", "NEGATIVE"
        
def generar_nombre_archivo(base_carpeta):
    """
    Genera un nombre único para el archivo de resultados en la carpeta 'results'.
    """
    fecha_actual = datetime.now(timezone.utc).strftime("%y%m%d")
    contador = 1
    
    while True:
        nombre_archivo = f"respuestas_{fecha_actual}_{contador:02d}.txt"
        ruta_completa = os.path.join(base_carpeta, nombre_archivo)
        if not os.path.exists(ruta_completa):
            return ruta_completa
        contador += 1

def main():
    """
    Función principal que coordina la lectura, clasificación y escritura de las solicitudes.
    """
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

    try:
        clasificador = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    except Exception as e:
        print(f"Error al cargar el modelo de clasificación: {e}")
        return

    solicitudes = leer_solicitudes(ruta_solicitudes)
    if not solicitudes:
        print("No se encontraron solicitudes para procesar. Asegúrate de que el archivo no esté vacío.")
        return

    resultados = []
    for idx, solicitud in enumerate(solicitudes, start=1):
        hora_solicitud = datetime.now(timezone.utc).strftime("%H:%M:%S")
        fecha_solicitud = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        clasificacion, categoria = clasificar_solicitud(solicitud, clasificador)
        hora_respuesta = datetime.now(timezone.utc).strftime("%H:%M:%S")

        resultado = [
            str(idx),
            fecha_solicitud,
            hora_solicitud,
            hora_respuesta,
            clasificacion,
            "Positiva" if categoria == "POSITIVE" else "Duda" if categoria == "Duda" else "Negativa",
            str(idx),  
            solicitud  
        ]
        resultados.append(resultado)

    escribir_resultados(ruta_resultados, resultados)
    print(f"Resultados guardados en: {ruta_resultados}")

if __name__ == "__main__":
    main()
