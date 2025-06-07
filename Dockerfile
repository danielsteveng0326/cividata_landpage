FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inicializar Reflex y compilar el frontend
RUN reflex init

# Compilar los assets del frontend para producción
RUN reflex export --frontend-only --no-zip

EXPOSE 3000
EXPOSE 8000

# Ejecutar Reflex en modo producción (sirve frontend Y backend)
CMD reflex run --env prod --backend-host 0.0.0.0 --frontend-port ${PORT:-3000} --backend-port 8000