"""Servidor HTTP expondo API REST para troca de chaves Kyber."""

# Importa o modulo logging para registrar informacoes de execucao
import logging

# Importa o modulo Flask para criacao da API
from flask import Flask, jsonify, request

# Importa as funcoes utilitarias que implementam o Kyber
from . import kyber_utils

# Configura o logger deste modulo
# Instancia o logger deste modulo
logger = logging.getLogger(__name__)

# Configura o formato padrao de logs
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")

# Instancia a aplicacao Flask
app = Flask(__name__)

@app.post('/generate')
def generate_keys():
    """Endpoint que gera um novo par de chaves."""
    logger.info("Requisicao recebida em /generate")
    # Chama a funcao utilitaria para gerar o par
    public_key, secret_key = kyber_utils.gerar_par_chaves()
    logger.info("Par de chaves gerado e retornado ao cliente")
    # Retorna as chaves em formato JSON
    return jsonify({'public_key': public_key, 'secret_key': secret_key})

@app.post('/encapsulate')
def encapsulate_secret():
    """Endpoint que encapsula um segredo a partir da chave publica."""
    logger.info("Requisicao recebida em /encapsulate")
    # Obtem os dados enviados pelo cliente em formato JSON
    data = request.get_json(force=True)
    # Recupera a chave publica do corpo da requisicao
    public_key = data.get('public_key')
    logger.info("Chave publica recebida para encapsulamento")
    # Encapsula o segredo usando a chave fornecida
    secret, ciphertext = kyber_utils.encapsular_segredo(public_key)
    logger.info("Segredo encapsulado enviado ao cliente")
    # Retorna o segredo e o ciphertext em JSON
    return jsonify({'secret': secret, 'ciphertext': ciphertext})

@app.post('/decapsulate')
def decapsulate_secret():
    """Endpoint que decapsula o segredo a partir do ciphertext."""
    logger.info("Requisicao recebida em /decapsulate")
    # Obtem os dados enviados pelo cliente
    data = request.get_json(force=True)
    # Recupera o ciphertext e a chave secreta do corpo
    ciphertext = data.get('ciphertext')
    secret_key = data.get('secret_key')
    logger.info("Dados recebidos: ciphertext e chave secreta")
    # Decapsula o segredo com as informacoes fornecidas
    secret = kyber_utils.decapsular_segredo(ciphertext, secret_key)
    logger.info("Segredo decapsulado retornado ao cliente")
    # Retorna o segredo decapsulado em formato JSON
    return jsonify({'secret': secret})

if __name__ == '__main__':
    logger.info("Iniciando servidor Flask")
    # Executa o servidor Flask na porta 5000
    app.run(host='0.0.0.0', port=5000)
