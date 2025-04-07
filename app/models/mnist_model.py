import numpy as np
import tensorflow as tf
from PIL import Image
import io
import cv2
from pathlib import Path

class MNISTModel:
    def __init__(self):
        """Inicializa el modelo MNIST."""
        self.model = None
        self.load_model()

    def load_model(self):
        """Carga el modelo pre-entrenado desde el archivo .h5"""
        model_path = Path(__file__).parent.parent.parent / "mnist_cnn_model.h5"
        try:
            self.model = tf.keras.models.load_model(str(model_path))
        except Exception as e:
            raise RuntimeError(f"Error al cargar el modelo: {str(e)}")

    def preprocess_image(self, image_data: bytes) -> np.ndarray:
        """
        Preprocesa la imagen para que coincida con el formato esperado por el modelo.

        Args:
            image_data: Imagen en formato bytes (desde el frontend)

        Returns:
            np.ndarray: Imagen procesada lista para la predicción
        """
        # Convertir bytes a imagen
        image = Image.open(io.BytesIO(image_data))
        
        # Convertir a escala de grises
        image = image.convert('L')
        
        # Redimensionar a 28x28
        image = image.resize((28, 28))
        
        # Convertir a array numpy
        img_array = np.array(image)
        
        # Normalizar valores a rango [0,1]
        img_array = img_array.astype('float32') / 255.0
        
        # Invertir colores si es necesario (MNIST usa dígitos blancos sobre fondo negro)
        img_array = 1 - img_array
        
        # Añadir dimensiones para batch y canal
        img_array = np.expand_dims(img_array, axis=(0, -1))
        
        return img_array

    def predict(self, image_data: bytes) -> dict:
        """
        Realiza la predicción sobre la imagen proporcionada.

        Args:
            image_data: Imagen en formato bytes

        Returns:
            dict: Diccionario con la predicción y probabilidades
        """
        if self.model is None:
            raise RuntimeError("El modelo no está cargado")

        # Preprocesar imagen
        processed_image = self.preprocess_image(image_data)
        
        # Realizar predicción
        predictions = self.model.predict(processed_image)
        
        # Obtener el dígito predicho y su probabilidad
        digit = np.argmax(predictions[0])
        probability = float(predictions[0][digit])
        
        return {
            "digit": int(digit),
            "probability": probability,
            "probabilities": predictions[0].tolist()
        }

# Instancia global del modelo
mnist_model = MNISTModel() 