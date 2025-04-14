# **Detección de errores en prendas con visión por ordenador en streaming.**
---
## Autores

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)
---

## Bienvenido
¡Hola! 👋 Bienvenido al repositorio **Maxima: Python Developer AI**. Este proyecto contiene codigos y pseudocodigos para resolver dos problemas propuestos:
- 1. Detección de errores en prendas con visión por ordenador y streaming.
- 2. Automatización de alto volumen de solicitudes en Atención al Cliente.

así como un código simple en Python demostrativo de seguimiento e identificación de personas con un modelo preentrenado.

**"1. Detection_anomalies"**
Detección de anomalias en Producción, se encuentra un scirpt demostrativo llamado "detect_personv3_JT" para tracking e identificación de personas.
Pseudocodigos para entrenamiento de modelo (detect.py, train.py): Playeras azules son validas, playeras rojas se consideran anomalias. 

Este proyecto utiliza YOLOv11 para detectar anomalías en playeras:
- Playeras azules (válidas)
- Playeras rojas (defectuosas)

## **Estructura del Proyecto**

La estructura del proyecto en la carpeta `Detection_anomalies` podría verse así:

```
Detection_anomalies/
├── data/
│   ├── coco.names                # Archivo con nombres de las clases (COCO)
│   ├── images/                   # Carpeta para imágenes de prueba y etiquetadas
│   │   ├── test_image.jpg        # Imagen de prueba para detección
│   ├── labels/                   # Carpeta para anotaciones en formato YOLO
│   │   ├── test_image.txt        # Etiquetas para test_image.jpg
│   ├── config.yaml               # Archivo de configuración para YOLOv11
├── models/
│   ├── yolo11m.pt                # Modelo preentrenado YOLOV11
├── scripts/
│   ├── train.py                  # Script para entrenamiento
│   ├── detect.py                 # Script para detección de anomalias
│   ├── detect_personv3_JT.py     # Script demostrativo de YOLO para tracking stream de personas funcional
├── results/
│   ├── anomalies.txt             # Archivo txt, estructura de propuesta para el registro de eventos
├── runs/detect/
│   ├── train/...                 # Modelos entrenados 
├── requirements.txt              # Archivo con las dependencias necesarias
├── README.md                     # Documentación básica del proyecto
├── Dockerfile
├── docker-compose.yml (opcional)
├── Informe_Detection_anomalies_240325_JT.pdf
├── .dockerignore
```

---

### **Detalles archivo/carpeta:**

#### **Directorio: `data/`**
- **`coco.names`:** Contiene los nombres de las clases del conjunto de datos COCO para la identificación y clasificación preentrenada.
- **`images/`:** Guarda aquí las imágenes de prueba y las imágenes etiquetadas para entrenamiento y validación.
- **`labels/`:** Contiene las anotaciones de las imágenes en formato YOLO.
- **`config.yaml`:** Archivo de configuración para YOLOv11.
---

#### **Directorio: `models/`**
- **`yolo11m.pt`:** Aquí está el modelo preentrenado.
---

# Detection Anomalies

Este proyecto propone utilizar YOLOv11 para detectar anomalías en playeras:
- Playeras azules (válidas)
- Playeras rojas (defectuosas)

## Estructura del Proyecto
- `data/`: Datos, etiquetas y configuración.
- `models/`: Modelos preentrenados y entrenados.
- `results/`: archivo de registro en formato txt (archivo de propuesta).
- `scripts/`: Scripts de entrenamiento y detección.

## Requisitos

Este proyecto requiere las siguientes herramientas y archivos para funcionar correctamente:

- **Python 3.12.8 o anterior**
- **YOLOV3**: Descarga el modelo YOLO V3 para la detección de objetos.
- **`yolov3.cfg`**: Este archivo de configuración puede encontrarse en las páginas de YOLO.
- **`coco.names`**: Archivo que contiene los nombres de las clases de objetos a identificar. Puedes buscarlo en las páginas de YOLO.
- **torch==2.0.1**: Biblioteca de aprendizaje, utilizada para construir y entrenar modelos de machine learning.
- **ultralytics==8.3.94**: Framework que incluye herramientas avanzadas YOLO, para la detección de objetos.
- **opencv-python==4.11.0**: Librería de visión por computadora para procesamiento de imágenes y videos.
- **matplotlib==3.10.0**: Herramienta de visualización de datos en Python, ideal para gráficos y análisis estadístico.
- **numpy==1.26.4**: Paquete para cálculos numéricos y manejo de matrices en Python.

#### **Archivo: `requirements.txt`**
Lista de las dependencias necesarias para el proyecto. Ejemplo:
```
torch==2.0.1
torchvision==0.15.2
ultralytics==8.3.94
opencv-python==4.11.0
matplotlib==3.10.0
numpy==1.26.4
```

Instálalas con:
```bash
pip install -r requirements.txt
```

---

## **Contribuciones**

Si deseas contribuir a este proyecto, por favor abre un **Pull Request** o crea un **Issue** en el repositorio, no olvides la mención al autor en su uso :´v.

---
## Actualizaciones
Posteriormente actualizaré este archivo README para proporcionar más detalles sobre el proyecto.

**Fecha de última actualización:** 24/03/25

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
Este script está protegido por derechos de autor y se permite su uso únicamente para fines personales o educativos. Para otros usos, contacta al autor.


## Contacto
Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jacob-t-329675258/) o en [Instagram](https://www.instagram.com/jknc.0/).
