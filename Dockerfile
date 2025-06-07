FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unzip \
    git \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inicializar y construir el frontend
RUN reflex init
RUN reflex export --frontend-only

# Script de inicio para modo producción completo
RUN echo '#!/bin/bash\n\
export PORT=${PORT:-3000}\n\
echo "Starting Reflex on port $PORT"\n\
exec reflex run --env prod --port $PORT --host 0.0.0.0' > start.sh && \
chmod +x start.sh

EXPOSE 3000

CMD ["./start.sh"]