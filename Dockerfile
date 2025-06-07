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

# Copiar requirements primero para mejor cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Inicializar Reflex
RUN reflex init

# Crear script de inicio mejorado
RUN echo '#!/bin/bash\n\
export BACKEND_PORT=${PORT:-3000}\n\
export BACKEND_HOST=0.0.0.0\n\
echo "Starting Reflex on port $BACKEND_PORT"\n\
exec reflex run --env prod --backend-only --loglevel info' > start.sh && \
chmod +x start.sh

EXPOSE 3000

CMD ["./start.sh"]