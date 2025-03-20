# Usar una imagen base con Python
FROM python:3.9-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY app.py /app/
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear un volumen para almacenar el modelo
VOLUME [ "/mnt/model" ]

# Exponer el puerto que usará la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

