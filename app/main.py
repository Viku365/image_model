from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .api.endpoints import router as api_router
import os

app = FastAPI(
    title="Digit Recognition API",
    description="API for handwritten digit recognition using MNIST model",
    version="1.0.0"
)

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configurar templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Incluir los endpoints de la API
app.include_router(api_router, prefix="/api/v1", tags=["prediction"])

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Endpoint para servir la página principal."""
    return templates.TemplateResponse("index.html", {"request": request}) 