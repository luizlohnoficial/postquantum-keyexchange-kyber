# Imagem base utilizando Python 3.10 slim
FROM python:3.10-slim


# A imagem python-slim ja contem o necessario para executar o projeto.
# Para simplificar o build e evitar dependencias extras, nao instalamos o
# pacote `liboqs-dev`, uma vez que a biblioteca `oqs` eh opcional e o
# codigo possui um mecanismo de fallback quando ela nao esta disponivel.

# Define o diretorio de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY .. /app

# Instala as dependencias do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["python", "-m", "src.api_server"]
