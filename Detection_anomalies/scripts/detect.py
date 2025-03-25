"""
Script para la automatización de solicitudes
Autor: Jacob Tinoco
Fecha: 23/03/2025
Derechos Reservados. Este script está protegido por derechos de autor. 
Uso permitido únicamente para fines personales o educativos.
© 2025. Todos los derechos reservados. Este script está protegido por derechos de autor (Jacob Tinoco).
Uso no autorizado está prohibido.

"""

# Importar las bibliotecas necesarias
from ultralytics import YOLO
import cv2
import datetime
import os

# Función para registrar eventos en un archivo .txt
def registrar_evento(anomalia, confianza):
    """
    Registra eventos de anomalías en un archivo .txt.
    """
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()
    # Crear el nombre del archivo con la fecha
    nombre_archivo = f"anomalias_{fecha_actual.strftime('%d%m%y')}_producto.txt"

    # Verificar si el archivo no existe y crearlo si es necesario
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Registro de anomalías en la línea de producción\n")

    # Registrar el evento en el archivo
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(
            f"| Fecha (ISO 8601) | Hora (UTC)  | Línea de Producción | Nombre del Producto | Tipo de anomalía: {anomalia} | Confianza: {confianza}%\n"
        )

# Función para enviar notificaciones
def enviar_notificacion(anomalia):
    """
    Simula el envío de una notificación (correo a Control de Calidad o mensaje de WhatsApp al encargado de area).
    """
    print(f"Notificación enviada: {anomalia}")

# Función principal para detectar anomalías
def detectar_anomalias(stream_video):
    """
    Detecta anomalías en un flujo de video utilizando un modelo YOLO.
    """
    # Cargar el modelo YOLO preentrenado
    modelo = YOLO("dirección/PATH/modelo/preentrenado")  # Reemplazar con la ruta real del modelo

    try:
        # Abrir el flujo de video
        video = cv2.VideoCapture(stream_video)
        if not video.isOpened():
            print("Error: No se pudo acceder a la cámara.")
            return

        # Procesar cada cuadro del video
        while video.isOpened():
            read, frame = video.read()
            if read:
                # Realizar predicción con el modelo YOLO
                resultados = modelo.predict(source=frame, conf=0.5)

                # Analizar los resultados de la predicción
                for resultado in resultados.boxes.data:
                    x1, y1, x2, y2, confianza, clase_id = resultado
                    anomalía = ""
                    if clase_id == 1:
                        anomalía = "Orificio en tela"
                    elif clase_id == 2:
                        anomalía = "Mancha"
                    elif clase_id == 3:
                        anomalía = "Costura incorrecta"

                    # Si se detecta una anomalía, registrar y notificar
                    if anomalía != "":
                        registrar_evento(anomalía, confianza * 100)
                        enviar_notificacion(anomalía)

    except Exception as e:
        print(f"Error durante la detección de anomalías: {e}")

# Iniciar el sistema
print("Sistema iniciado.")
detectar_anomalias("ruta/a/stream/camara")  # Reemplazar con la ruta real del stream de la cámara
