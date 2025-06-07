FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Reflex
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Inicializar Reflex (importante para generar los archivos necesarios)
RUN reflex init

# Exponer el puerto (Railway lo sobrescribirá con $PORT)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD reflex run --env prod --backend-only --port ${PORT:-8000} --host 0.0.0.0