from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Cargar el modelo entrenado
model = YOLO('runs/detect/train/weights/best.pt')

# Función para detección
def detect(image_path):
    img = cv2.imread(image_path)
    results = model.predict(source=img, conf=0.5)

    # Dibujar las cajas
    for result in results[0].boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        color = (0, 255, 0) if class_id == 0 else (0, 0, 255)
        label = 'Azul' if class_id == 0 else 'Rojo'
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(img, f"{label} {score:.2f}", (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Mostrar la imagen
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Prueba con una imagen
detect('data/images/test_image.jpg')
