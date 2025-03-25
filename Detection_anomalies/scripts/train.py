"""
Script para la automatización de solicitudes
Autor: Jacob Tinoco
Fecha: 23/03/2025
Derechos Reservados. Este script está protegido por derechos de autor. 
Uso permitido únicamente para fines personales o educativos.
© 2025. Todos los derechos reservados. Este script está protegido por derechos de autor (Jacob Tinoco).
Uso no autorizado está prohibido.

"""
from ultralytics import YOLO

print("© 2025. Todos los derechos reservados. Este script está protegido por derechos de autor (Jacob Tinoco). El uso no autorizado está prohibido.")

try:
    modelo = YOLO("Dirección/PATH/de/modelo/preentrenado")  
except Exception as e:
    print("Error: No se pudo cargar el modelo. Verifica la ruta o el archivo.")
    print(f"Detalles del error: {e}")
    exit() 

try:
    resultados = modelo.train(data="Dirección/PATH/etiquetas/coco", epochs=1, imgsz=640)  # Ajustar parámetros según necesidad
    print("Entrenamiento completado con éxito.")
except Exception as e:
    print("Error: Falló el entrenamiento. Verifica los datos o parámetros.")
    print(f"Detalles del error: {e}")
    exit()

print("Ejecución completada. Jacob Tinoco © 2025. Todos los derechos reservados.")
