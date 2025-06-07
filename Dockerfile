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
RUN reflex init

# Copiar y hacer ejecutable el script
COPY start.sh .
RUN chmod +x start.sh

# Railway asignará el puerto mediante $PORT
EXPOSE 8080

# Usar el script que maneja correctamente las variables
CMD ["./start.sh"]