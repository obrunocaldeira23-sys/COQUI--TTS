FROM python:3.10-slim

WORKDIR /app

# Instala dependências básicas
RUN apt-get update && apt-get install -y \
    git espeak-ng libespeak-ng-dev ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia arquivos do projeto
COPY . .

# Instala as dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Porta exposta
EXPOSE 8080

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
