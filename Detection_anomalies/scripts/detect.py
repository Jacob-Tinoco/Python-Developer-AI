# Pseudocódigo para verificación de conexión y detección de anomalías en playeras

# Importar las bibliotecas necesarias
IMPORTAR YOLO desde ultralytics
IMPORTAR cv2
IMPORTAR datetime
IMPORTAR os

# Función para registrar eventos en un archivo .txt
FUNCIÓN registrar_evento(anomalia, confianza):
    fecha_actual ← datetime.datetime.now()
    nombre_archivo ← f"anomalias_{fecha_actual.strftime('%d%m%y')}_producto.txt"

    SI no EXISTE archivo nombre_archivo:
        CREAR archivo nombre_archivo

    AÑADIR AL archivo nombre_archivo:
        ESCRIBIR f"Fecha: {fecha_actual.strftime('%Y-%m-%d')}, Hora: {fecha_actual.strftime('%H:%M:%S')}, "
        ESCRIBIR "Línea de producción: Línea 1, "
        ESCRIBIR "Nombre del Producto: Playera, "
        ESCRIBIR f"| Fecha (ISO 8601) | Hora (UTC)  | Línea de Producción | Nombre del Producto | Tipo de anomalía: {anomalia} | Confianza: {confianza}%\n"

# Función para enviar notificaciones
FUNCIÓN enviar_notificacion(anomalia):
    MOSTRAR f"Notificación enviada: {anomalia}"
    # Simula envío de correo y mensaje de WhatsApp

# Función principal para detectar anomalías
FUNCIÓN detectar_anomalias(stream_video):
    CARGAR modelo YOLO desde 'dirección/PATH/modelo/preentrenado'

    INTENTAR:
        video ← cv2.VideoCapture(stream_video)
        SI NO video está abierto:
            MOSTRAR "Error: No se pudo acceder a la cámara."
            TERMINAR

        MIENTRAS video está abierto:
            read, frame ← video.read()
            SI leer:
                resultados ← modelo.predecir(fuente=frame, conf=0.5)

                PARA resultado EN resultados.cajas.datos:
                    x1, y1, x2, y2, confianza, clase_id ← resultado
                    anomalía ← ""
                    SI clase_id == 1:
                        anomalía ← "Orificio en tela"
                    SI clase_id == 2:
                        anomalía ← "Mancha"
                    SI clase_id == 3:
                        anomalía ← "Costura incorrecta"

                    SI anomalía != "":
                        registrar_evento(anomalía, confianza * 100)
                        enviar_notificacion(anomalía)

    CATCH Error:
        MOSTRAR "Error durante la detección de anomalías."

# Iniciar el sistema
MOSTRAR "Sistema iniciado."
detectar_anomalias("ruta/a/stream/camara")
