# Usar una imagen base con Python
FROM python:3.9-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar el archivo comprimido y luego extraerlo
COPY deepseek-r1-model.tar.gz /app
RUN tar -xvzf deepseek-r1-model.tar.gz && rm deepseek-r1-model.tar.gz

# Copiar el resto del código
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

