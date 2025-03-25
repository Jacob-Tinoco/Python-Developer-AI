from transformers import pipeline

# Función para leer solicitudes desde un archivo
def leer_solicitudes(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines() if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        return []

# Función para escribir resultados en un archivo
def escribir_resultados(ruta_archivo, resultados):
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("ID | Fecha | Hora Solicitud (UTC) | Hora Respuesta (UTC) | Clasificación | Positivo/Negativo\n")
            for resultado in resultados:
                archivo.write(" | ".join(resultado) + "\n")
    except Exception as e:
        print(f"Error al escribir en el archivo {ruta_archivo}: {e}")

# Función para clasificar solicitudes
def clasificar_solicitud(solicitud, clasificador):
    try:
        # Clasificar en positiva o negativa
        resultado = clasificador(solicitud)[0]
        categoria = resultado["label"]  # Puede ser "POSITIVE" o "NEGATIVE"
        confianza = resultado["score"]

        # Clasificar en categorías específicas del negocio
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
        else:
            clasificacion = "General"

        return clasificacion, categoria
    except Exception as e:
        print(f"Error al clasificar la solicitud: {e}")
        return "Error", "NEGATIVE"