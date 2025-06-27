"""Modulo com funcoes utilitarias para troca de chaves Kyber."""

# Importa o modulo base64 para codificacao das chaves e segredos
import base64

# Importa o modulo logging para registrar informacoes e erros
import logging

# Tenta importar a biblioteca oqs utilizada para operacoes post-quantum
try:
    from oqs import KeyEncapsulation  # type: ignore
except ImportError:
    # Caso a biblioteca nao esteja disponivel, definimos um valor nulo
    KeyEncapsulation = None

# Configura o logger deste modulo
# Instancia o logger deste modulo
logger = logging.getLogger(__name__)

# Define o formato padrao de logs para toda a aplicacao
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")

def gerar_par_chaves():
    """Gera um par de chaves Kyber e retorna codificado em Base64."""
    # Verifica se a biblioteca oqs esta carregada
    if KeyEncapsulation is None:
        # Se nao estiver instalada, informamos erro ao usuario
        raise RuntimeError("Biblioteca oqs nao esta instalada")
    # Inicializa o algoritmo Kyber512
    kem = KeyEncapsulation('Kyber512')
    # Gera a chave publica e a chave secreta
    public_key = kem.generate_keypair()
    secret_key = kem.export_secret_key()
    # Codifica a chave publica em Base64
    pub_b64 = base64.b64encode(public_key).decode('utf-8')
    # Codifica a chave secreta em Base64
    sec_b64 = base64.b64encode(secret_key).decode('utf-8')
    # Registra que o par de chaves foi gerado
    logger.info("Par de chaves gerado")
    # Retorna ambas as chaves codificadas
    return pub_b64, sec_b64

def encapsular_segredo(chave_publica_b64):
    """Encapsula um segredo usando a chave publica em Base64."""
    # Verifica se a biblioteca oqs esta disponivel
    if KeyEncapsulation is None:
        # Caso nao esteja instalada, levanta erro
        raise RuntimeError("Biblioteca oqs nao esta instalada")
    # Inicializa o algoritmo Kyber512
    kem = KeyEncapsulation('Kyber512')
    # Decodifica a chave publica de Base64
    public_key = base64.b64decode(chave_publica_b64)
    # Realiza o encapsulamento gerando ciphertext e segredo
    ciphertext, shared_secret = kem.encap_secret(public_key)
    # Codifica o ciphertext em Base64
    ct_b64 = base64.b64encode(ciphertext).decode('utf-8')
    # Codifica o segredo compartilhado em Base64
    secret_b64 = base64.b64encode(shared_secret).decode('utf-8')
    # Registra que o segredo foi encapsulado
    logger.info("Segredo encapsulado")
    # Retorna o segredo e o ciphertext codificados
    return secret_b64, ct_b64

def decapsular_segredo(ciphertext_b64, chave_secreta_b64):
    """Decapsula o segredo compartilhado a partir do ciphertext e da chave secreta."""
    # Confere se a biblioteca oqs esta disponivel
    if KeyEncapsulation is None:
        # Informa ao usuario que nao foi possivel continuar
        raise RuntimeError("Biblioteca oqs nao esta instalada")
    # Inicializa o algoritmo Kyber512
    kem = KeyEncapsulation('Kyber512')
    # Importa a chave secreta decodificada
    kem.import_secret_key(base64.b64decode(chave_secreta_b64))
    # Decodifica o ciphertext recebido
    ciphertext = base64.b64decode(ciphertext_b64)
    # Decapsula o segredo utilizando a chave secreta
    shared_secret = kem.decap_secret(ciphertext)
    # Codifica o segredo resultante em Base64
    secret_b64 = base64.b64encode(shared_secret).decode('utf-8')
    # Registra que o segredo foi decapsulado
    logger.info("Segredo decapsulado")
    # Retorna o segredo compartilhado em Base64
    return secret_b64
