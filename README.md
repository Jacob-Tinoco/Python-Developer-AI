# **Repositorio: Python Developer AI**

### **README General del Repositorio**

## **Autores**

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)

---

## **Bienvenida**

¡Hola! 👋 Bienvenido al repositorio **Python Developer AI**. Este repositorio contiene dos proyectos principales diseñados para abordar problemas técnicos mediante el uso de Python con AI y automatización de procesos. Ambos proyectos están orientados a resolver desafíos específicos y proporcionar soluciones prácticas mediante el uso de herramientas modernas como modelos preentrenados y algoritmos de aprendizaje automático.

Los proyectos incluidos son:

1. **Detección de errores en prendas con visión por ordenador y streaming.**
2. **Automatización de alto volumen de solicitudes en Atención al Cliente.**

Cada proyecto incluye una estructura organizada, scripts funcionales y pseudocódigos para facilitar la comprensión y personalización de las soluciones.

---

## **Proyectos**

### **1. Detection_anomalies**
Este proyecto aborda la **detección de anomalías en prendas** mediante visión por ordenador. Se utiliza un modelo de detección basado en YOLO para identificar prendas válidas y defectuosas. Incluye scripts para entrenamiento de modelos, detección en tiempo real y generación de etiquetas.

---

### **2. automatización_solicitudes**
Este proyecto se enfoca en la **automatización de la clasificación de solicitudes de clientes** utilizando un modelo de Procesamiento de Lenguaje Natural (NLP). Permite procesar solicitudes en texto, clasificarlas en categorías específicas y registrar los resultados de manera estructurada.

---

## **Estructura del Repositorio**

A continuación, se presenta la estructura general del repositorio, con carpetas separadas para cada proyecto:

```
Python_Developer_AI/
│
├── Detection_anomalies/          # Proyecto 1: Detección de anomalías en prendas
│   ├── data/                     # Carpeta para almacenar datos de entrada (imágenes, etiquetas, etc.)
│   ├── models/                   # Carpeta para almacenar modelos preentrenados
│   ├── scripts/                  # Scripts principales para entrenamiento y detección
│   ├── README.md                 # Instrucciones específicas del proyecto
│   ├── runs/detect/              # Modelos entrenados
│   ├── requirements.txt          # Archivo con las dependencias del proyecto
│   ├── Dockerfile
│   ├── docker-compose.yml (opcional)
│   ├── Informe_Detection_anomalies_240325_JT.pdf
│   ├── .dockerignore
│
├── Automatizacion_solicitudes/   # Proyecto 2: Automatización de solicitudes de clientes
│   ├── data/                     # Carpeta para almacenar datos de entrada (solicitudes en texto)
│   ├── results/                  # Carpeta para almacenar resultados generados
│   ├── models/                   # Carpeta para almacenar modelos preentrenados (opcional)
│   ├── scripts/                  # Scripts principales para procesamiento y clasificación
│   ├── README.md                 # Instrucciones específicas del proyecto
│   ├── requirements.txt          # Archivo con las dependencias del proyecto
│   ├── Indorme_automatización_solicitudes_240325_JT.pdf
│   ├── baja_confianza.txt
│   ├── main.py
│
└── README.md                     # Este archivo, con la descripción general del repositorio
```

---

## **Requisitos**

### **Software**
- Python 3.11 o superior.
- Dependencias específicas para cada proyecto (ver los archivos `requirements.txt` en las carpetas respectivas).

### **Modelos**
- **YOLO**: Modelo preentrenado para detección de anomalías (Proyecto 1).
- **NLP**: Modelo preentrenado para clasificación de texto (Proyecto 2).

---

## **Cómo Usar Este Repositorio**

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Jacob-Tinoco/Python_Developer_AI.git
   ```
2. Navega a la carpeta del proyecto que deseas explorar:
   ```bash
   cd Detection_anomalies  # Para el Proyecto 1
   cd Automatizacion_solicitudes  # Para el Proyecto 2
   ```
3. Sigue las instrucciones específicas de cada proyecto en su archivo `README.md`.

---

## **Contribuciones**
Si deseas contribuir a este proyecto, por favor abre un **Pull Request** o crea un **Issue** en el repositorio, no olvides la mención al autor en su uso :´v.


¡Gracias por visitar este repositorio! 🎉

## Actualizaciones
Posteriormente actualizaré este archivo README para proporcionar más detalles sobre el proyecto.

**Fecha de última actualización:** 23/03/25

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto
Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jacob-t-329675258/) o en [Instagram](https://www.instagram.com/jknc.0/).

