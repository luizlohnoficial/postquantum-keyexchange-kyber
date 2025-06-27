# Imagem base utilizando Python 3.10 slim
FROM python:3.10-slim

# Atualiza o sistema e instala dependencias da liboqs
RUN apt-get update && \
    apt-get install -y liboqs-dev && \
    rm -rf /var/lib/apt/lists/*

# Define o diretorio de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY .. /app

# Instala as dependencias do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["python", "-m", "kyber_key_exchange.src.api_server"]
