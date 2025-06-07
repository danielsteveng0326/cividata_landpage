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

# Inicializar Reflex
RUN reflex init

# Railway asigna el puerto dinámicamente
EXPOSE 8080

# Configurar variables de entorno para Reflex
ENV BACKEND_PORT=$PORT
ENV BACKEND_HOST=0.0.0.0

# Comando simplificado - Reflex usará las variables de entorno
CMD reflex run --env prod --backend-only