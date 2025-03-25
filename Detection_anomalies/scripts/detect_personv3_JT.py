"""
Script para la automatización de solicitudes
Autor: Jacob Tinoco
Fecha: 23/03/2025
Derechos Reservados. Este script está protegido por derechos de autor. 
Uso permitido únicamente para fines personales o educativos.
© 2025. Todos los derechos reservados. Este script está protegido por derechos de autor (Jacob Tinoco).
Uso no autorizado está prohibido.

"""
import cv2
import numpy as np
from ultralytics import YOLO  

def Yolo11(model_path, classes_file):
    model = YOLO(model_path)
    with open(classes_file, 'r') as f:
        classes = f.read().strip().split('\n')
    
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    
    return model, classes, colors

def detect(model, classes, colors, cap):
    """
    Detecta objetos en tiempo real utilizando YOLO y muestra los resultados en una ventana.
    """
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el video. Verifica la cámara.")
            break

        results = model.predict(frame, stream=True, verbose=False)
        
        for result in results:
            boxes = result.boxes
            
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
                class_id = int(box.cls[0].cpu().numpy())
                confidence = box.conf[0].cpu().numpy()

                if classes[class_id] == "person":
                    print(f"Persona detectada con {confidence:.2f} de confianza.")
                    color = tuple(map(int, colors[class_id]))  
                    label = f"{classes[class_id]}: {confidence:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Mostrar el frame en una ventana
        cv2.imshow("Detección de Personas", frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def main():
    """
    Función principal del script.
    """
    model_path = "models/yolo11m.pt"  
    classes_file = "data/coco.names"  
    model, classes, colors = Yolo11(model_path, classes_file)

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    print("Cámara iniciada. Presiona 'q' para salir.")

    try:
        # Detectar y mostrar resultados en tiempo real
        detect(model, classes, colors, cap)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
