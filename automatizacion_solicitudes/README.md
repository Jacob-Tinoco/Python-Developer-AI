# **Automatización de Clasificación de Solicitudes**

## Autores

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)
---
## Bienvenida
¡Hola! 👋 Bienvenido al repositorio **Python Developer AI**. Este proyecto contiene codigos y pseudocodigos para resolver dos problemas propuestos:
- 1. Detección de errores en prendas con visión por ordenador y streaming.
- 2. Automatización de alto volumen de solicitudes en Atención al Cliente.

así como un código simple en Python demostrativo de seguimiento e identificación de personas con un modelo preentrenado.

# Automatización de alto volumen de solicitudes en Atención al Cliente.

## **Descripción**
Este proyecto tiene como objetivo automatizar la clasificación de solicitudes de clientes utilizando un modelo de Procesamiento de Lenguaje Natural (NLP). El script procesa solicitudes de texto, las clasifica en categorías específicas y las guarda en un archivo de registro "respuestas_YYMMDD_##.

El enfoque principal es garantizar que las interacciones o dudas de los clientes sean correctamente clasificadas como **"Duda del cliente"**, **Factura**, **Dañado**, **satisfecho**, **envío producto**, **pago**, **duda**. Y de manera objetiva si la interacción del cliente respecto al servicio/produtco es **POSITIVE**, **NEGATIVE** o en su defecto es una interacción donde el cliente tiene alguna **DUDA**

---

## **Estructura del Proyecto**

```
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
```

---

## **Requisitos**

### **Software**
- Python 3.8 o superior.
- Bibliotecas requeridas (ver sección de instalación).

### **Modelo NLP**
- Modelo preentrenado: `distilbert-base-uncased-finetuned-sst-2-english` de Hugging Face.

---

## **Instalación**

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Jacob-Tinoco/Python-Developer-AI/tree/main/automatizacion_solicitudes
   cd la/ruta/local/aqui/mi/estimado
   ```

2. **Crear un entorno virtual (opcional, aunque recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Sobre la estructura de carpetas: datos de entrada, salida**:
   - Asegúrate de que la carpeta `data` contenga un archivo llamado `solicitudes.txt` o algun dataset con las solicitudes a procesar.
   - La carpeta `results` se creará automáticamente si no existe.

---

## **Uso**

### **Ejecutar el script**
Para procesar las solicitudes, ejecuta el siguiente comando:
```bash
python main.py
```

### **Entrada**
El archivo de entrada `solicitudes.txt` debe contener una solicitud por línea. Ejemplo:
```
¿Pueden ayudarme con una factura que no recibí?
El producto llegó dañado y quiero devolverlo.
Estoy satisfecho con el servicio.
```

### **Salida**
El script generará un archivo en la carpeta `results` con el siguiente formato y encabezado:
```
ID | Fecha | Hora Solicitud (UTC) | Hora Respuesta (UTC) | Clasificación | Positivo/Negativo | ID Solicitud | Solicitud Procesada
```

Ejemplo:
```
1 | 2025-03-25 | 01:48:46 | 01:48:46 | Facturación | Duda del cliente | 1 | ¿Pueden ayudarme con una factura que no recibí?
2 | 2025-03-25 | 01:48:50 | 01:48:50 | Insatisfacción del Producto | Negativa | 2 | El producto llegó dañado y quiero devolverlo.
3 | 2025-03-25 | 01:48:55 | 01:48:55 | Satisfacción del Producto | Positiva | 3 | Estoy satisfecho con el servicio.
```

---

## **Características**

1. **Clasificación Específica**:
   - Las solicitudes se clasifican en las siguientes categorías:
     - **Facturación**
     - **Insatisfacción del Producto**
     - **Satisfacción del Producto**
     - **Preguntas de Envío**
     - **Preguntas del Producto**
     - **Preguntas de Métodos de Pago**
     - **Duda del cliente**
     - **General**

2. **Manejo de Preguntas**:
   - Las solicitudes que contienen palabras clave como "duda", "pregunta" o terminan con un signo de interrogación (`?`) se clasifican como **"Duda del cliente"**.

3. **Detección de Baja Confianza**:
   - Si el modelo devuelve una puntuación de confianza menor al 60%, la solicitud se registra en el archivo `baja_confianza.txt` para revisión manual.

4. **Generación Automática de Resultados**:
   - Los resultados se guardan en un archivo único dentro de la carpeta `results` con un nombre basado en la fecha y un contador.

---

## **Archivos Generados**

1. **Archivo de Resultados**:
   - Se encuentra en la carpeta `results/`.
   - Contiene las solicitudes procesadas y clasificadas.

2. **Archivo de Baja Confianza**:
   - Se genera un archivo `baja_confianza.txt` en la raíz del proyecto para registrar solicitudes cuya clasificación tiene baja confianza.

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



