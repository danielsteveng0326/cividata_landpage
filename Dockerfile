FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inicializar y preparar para producción
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Puerto que Railway asignará
EXPOSE 3000

# Ejecutar en modo producción
CMD reflex run --env prod --loglevel info