document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const clearButton = document.getElementById('clearButton');
    const predictButton = document.getElementById('predictButton');
    const predictionResult = document.getElementById('predictionResult');
    const confidenceFill = document.querySelector('.confidence-fill');
    const confidenceValue = document.getElementById('confidenceValue');

    // Configuración inicial del canvas
    function initCanvas() {
        // Establecer el tamaño del canvas
        canvas.width = 280;
        canvas.height = 280;
        
        // Configuración del contexto
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 15;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        
        // Fondo blanco
        ctx.fillStyle = '#fff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }

    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

    // Inicializar canvas
    initCanvas();

    // Eventos del mouse
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);

    // Eventos táctiles
    canvas.addEventListener('touchstart', handleTouch);
    canvas.addEventListener('touchmove', handleTouch);
    canvas.addEventListener('touchend', stopDrawing);

    function startDrawing(e) {
        isDrawing = true;
        const coords = getCoordinates(e);
        lastX = coords.x;
        lastY = coords.y;
    }

    function draw(e) {
        if (!isDrawing) return;
        e.preventDefault();

        const coords = getCoordinates(e);
        const currentX = coords.x;
        const currentY = coords.y;

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(currentX, currentY);
        ctx.stroke();

        lastX = currentX;
        lastY = currentY;
    }

    function stopDrawing() {
        isDrawing = false;
    }

    function getCoordinates(e) {
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;

        if (e.type.includes('touch')) {
            return {
                x: (e.touches[0].clientX - rect.left) * scaleX,
                y: (e.touches[0].clientY - rect.top) * scaleY
            };
        } else {
            return {
                x: (e.clientX - rect.left) * scaleX,
                y: (e.clientY - rect.top) * scaleY
            };
        }
    }

    function handleTouch(e) {
        e.preventDefault();
        if (e.type === 'touchstart') {
            startDrawing(e);
        } else if (e.type === 'touchmove') {
            draw(e);
        }
    }

    // Limpiar canvas
    clearButton.addEventListener('click', () => {
        ctx.fillStyle = '#fff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        predictionResult.querySelector('.digit').textContent = '-';
        confidenceFill.style.width = '0%';
        confidenceValue.textContent = '0%';
    });

    // Realizar predicción
    predictButton.addEventListener('click', async () => {
        try {
            // Convertir el canvas a blob
            const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/png'));
            
            // Crear FormData y añadir la imagen
            const formData = new FormData();
            formData.append('file', blob, 'digit.png');

            // Enviar la imagen al backend
            const response = await fetch('/api/v1/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Error en la predicción');
            }

            const result = await response.json();
            
            // Actualizar la UI con la predicción
            predictionResult.querySelector('.digit').textContent = result.digit;
            const confidence = (result.probability * 100).toFixed(1);
            confidenceFill.style.width = `${confidence}%`;
            confidenceValue.textContent = `${confidence}%`;

        } catch (error) {
            console.error('Error:', error);
            alert('Error al realizar la predicción. Por favor, intenta de nuevo.');
        }
    });
}); 