FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema que Reflex necesita
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inicializar Reflex
RUN reflex init

EXPOSE 8000

# Comando corregido con --backend-port
CMD reflex run --env prod --backend-only --backend-port ${PORT:-8000} --backend-host 0.0.0.0