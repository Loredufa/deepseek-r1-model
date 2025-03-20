# Usar una imagen base con Python

FROM python:3.9-slim

# Copiar el código y las dependencias
COPY . /app
WORKDIR /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que usará la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
