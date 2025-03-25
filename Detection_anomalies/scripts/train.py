"""
Script para la automatización de solicitudes
Autor: Jacob Tinoco
Fecha: 23/03/2025
Derechos Reservados. Este script está protegido por derechos de autor. 
Uso permitido únicamente para fines personales o educativos.
© 2025. Todos los derechos reservados. Este script está protegido por derechos de autor (Jacob Tinoco).
Uso no autorizado está prohibido.

"""
# Importar la librería YOLO
from ultralytics import YOLO

# Mostrar mensaje de derechos de autor
print("© 2025. Todos los derechos reservados. Este script está protegido por derechos de autor (Jacob Tinoco). El uso no autorizado está prohibido.")

# Intentar cargar el modelo YOLO
try:
    # Cargar el modelo preentrenado
    modelo = YOLO("Dirección/PATH/de/modelo/preentrenado")  # Reemplazar con la ruta real del modelo
except Exception as e:
    # Mostrar mensaje de error si no se puede cargar el modelo
    print("Error: No se pudo cargar el modelo. Verifica la ruta o el archivo.")
    print(f"Detalles del error: {e}")
    exit()  # Terminar la ejecución del script

# Intentar entrenar el modelo
try:
    # Entrenar el modelo con los parámetros especificados
    resultados = modelo.train(data="Dirección/PATH/etiquetas/coco", epochs=1, imgsz=640)  # Ajustar parámetros según necesidad
    print("Entrenamiento completado con éxito.")
except Exception as e:
    # Mostrar mensaje de error si falla el entrenamiento
    print("Error: Falló el entrenamiento. Verifica los datos o parámetros.")
    print(f"Detalles del error: {e}")
    exit()  # Terminar la ejecución del script

# Mostrar mensaje de finalización
print("Ejecución completada. Jacob Tinoco © 2025. Todos los derechos reservados.")
