FROM python:3.11

WORKDIR /app

# Instalar Node.js 18 (requerido por Reflex)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Inicializar Reflex
RUN reflex init

# Puerto que Railway asignará
EXPOSE 3000

# Comando directo sin script
CMD reflex run --env prod --frontend-port ${PORT:-3000} --backend-port ${PORT:-3000} --host 0.0.0.0