# Usar Python 3.10
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /code

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar los requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
