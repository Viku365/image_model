# Planificación del Proyecto de Reconocimiento de Dígitos Manuscritos

## Visión General
Desarrollar una aplicación web que permita a los usuarios dibujar un número en una interfaz gráfica y utilizar un modelo pre-entrenado de MNIST (mnist_cnn_model.h5) para predecir qué dígito ha escrito el usuario.

## Arquitectura del Sistema

### Frontend
- **Interfaz de dibujo**: Canvas HTML5 para que el usuario pueda dibujar dígitos
- **Panel de resultados**: Área para mostrar la predicción del modelo
- **Controles adicionales**: Botones para limpiar el canvas, enviar la imagen, etc.

### Backend
- **API REST**: Para recibir la imagen dibujada y devolver la predicción
- **Procesamiento de imágenes**: Preprocesamiento de la imagen para adaptarla al formato que espera el modelo MNIST (28x28 píxeles, escala de grises)
- **Inferencia del modelo**: Carga del modelo pre-entrenado y predicción

## Stack Tecnológico

### Frontend
- **HTML/CSS/JavaScript**: Para la interfaz básica
- **Framework**: Se puede usar React, Vue o simplemente JavaScript vanilla
- **Canvas API**: Para implementar la funcionalidad de dibujo

### Backend
- **Python**: Lenguaje principal para el backend
- **Flask/FastAPI**: Framework web ligero para crear la API
- **TensorFlow/Keras**: Para cargar y utilizar el modelo pre-entrenado
- **NumPy/OpenCV**: Para el procesamiento de imágenes
- **Gunicorn/uWSGI**: Para despliegue en producción (opcional)

## Flujo de Trabajo
1. El usuario dibuja un dígito en el canvas
2. La aplicación web convierte el dibujo en una imagen (generalmente en formato base64)
3. La imagen se envía al backend a través de una petición AJAX/Fetch
4. El backend preprocesa la imagen:
   - Conversión a escala de grises
   - Redimensionamiento a 28x28 píxeles
   - Normalización (valores entre 0 y 1)
   - Inversión si es necesario (MNIST utiliza fondos negros con dígitos blancos)
5. El modelo predice el dígito
6. El backend devuelve la predicción al frontend
7. El frontend muestra el resultado al usuario

## Limitaciones y Consideraciones
- El modelo MNIST está entrenado con dígitos específicos, por lo que puede no funcionar bien con estilos de escritura muy diferentes
- La aplicación necesita realizar el preprocesamiento correcto para que coincida con el formato que espera el modelo
- Consideraciones de rendimiento para dispositivos móviles y diferentes navegadores
- Posible latencia en la predicción según el hosting utilizado

## Herramientas de Desarrollo
- **Editor de código**: VS Code, PyCharm, o similar
- **Control de versiones**: Git/GitHub para seguimiento de cambios
- **Navegador web**: Para pruebas de frontend
- **Herramientas de desarrollo del navegador**: Para depuración

## Plan de Implementación
1. Configurar el entorno de desarrollo
2. Desarrollar el backend primero (API + integración del modelo)
3. Desarrollar el frontend (interfaz de dibujo + comunicación con API)
4. Integrar frontend y backend
5. Probar con diferentes dígitos y ajustar el preprocesamiento si es necesario
6. Optimizar rendimiento
7. Desplegar la aplicación
