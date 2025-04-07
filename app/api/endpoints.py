from fastapi import APIRouter, UploadFile, HTTPException
from ..models.mnist_model import mnist_model

router = APIRouter()

@router.post("/predict")
async def predict_digit(file: UploadFile):
    """
    Endpoint para predecir el dígito a partir de una imagen.
    
    Args:
        file: Archivo de imagen enviado desde el frontend
        
    Returns:
        dict: Predicción del modelo con el dígito y probabilidades
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")
    
    try:
        contents = await file.read()
        result = mnist_model.predict(contents)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}") 