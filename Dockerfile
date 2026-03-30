FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Rodar o bot
CMD ["python", "main.py"]