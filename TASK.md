# Tareas del Proyecto de Reconocimiento de Dígitos MNIST

## Tareas Activas
- [ ] Configurar el entorno de desarrollo
  - [ ] Instalar dependencias necesarias para Python (TensorFlow, Flask/FastAPI, etc.)
  - [ ] Preparar estructura de carpetas del proyecto

- [ ] Desarrollo Backend
  - [ ] Crear API REST básica
  - [ ] Implementar endpoint para procesar imágenes
  - [ ] Cargar y probar el modelo mnist_cnn_model.h5
  - [ ] Desarrollar función de preprocesamiento de imágenes

- [ ] Desarrollo Frontend
  - [ ] Crear estructura HTML básica
  - [ ] Implementar canvas para dibujo
  - [ ] Desarrollar lógica de captura de imágenes
  - [ ] Diseñar interfaz de usuario
  - [ ] Implementar comunicación con la API

- [ ] Integración y Pruebas
  - [ ] Conectar frontend y backend
  - [ ] Probar con diferentes tipos de dígitos manuscritos
  - [ ] Ajustar preprocesamiento según resultados

- [ ] Optimización
  - [ ] Mejorar rendimiento del canvas
  - [ ] Optimizar tiempos de respuesta
  - [ ] Ajustar UX/UI

- [ ] Despliegue
  - [ ] Preparar la aplicación para producción
  - [ ] Desplegar backend
  - [ ] Desplegar frontend
  - [ ] Configurar CORS y seguridad

## Tareas Pendientes (Backlog)
- [ ] Añadir funcionalidad para guardar imágenes
- [ ] Implementar historial de predicciones
- [ ] Añadir estadísticas de precisión
- [ ] Implementar retroalimentación del usuario para mejorar el modelo
- [ ] Soporte para dispositivos móviles (eventos táctiles)
- [ ] Opción para cambiar el grosor del pincel
- [ ] Modo oscuro/claro

## Descubrimientos y Notas
- Asegurarse de que el preprocesamiento coincida exactamente con el formato de entrada del modelo
- Puede ser necesario invertir los colores dependiendo de cómo se entrenó el modelo
- Tener en cuenta diferentes resoluciones de pantalla para la experiencia de dibujo
