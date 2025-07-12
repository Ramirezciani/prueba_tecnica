FROM python:3.11-slim

# Evita crear archivos .pyc y usa stdout/stderr sin buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo
WORKDIR /app

# Copia e instala las dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de la aplicación
COPY ./app ./app

# Agrega el directorio app al PYTHONPATH
ENV PYTHONPATH=/app

# Ejecuta el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
