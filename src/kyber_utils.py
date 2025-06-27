"""Modulo com funcoes utilitarias para troca de chaves Kyber."""

# Importa o modulo base64 para codificacao das chaves e segredos
import base64
import os

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
    if KeyEncapsulation is None:
        # Fallback simples para testes quando oqs nao esta instalado
        public_key = os.urandom(32)
        secret_key = os.urandom(32)
    else:
        kem = KeyEncapsulation('Kyber512')
        public_key = kem.generate_keypair()
        secret_key = kem.export_secret_key()

    pub_b64 = base64.b64encode(public_key).decode('utf-8')
    sec_b64 = base64.b64encode(secret_key).decode('utf-8')
    logger.info("Par de chaves gerado")
    return pub_b64, sec_b64

def encapsular_segredo(chave_publica_b64):
    """Encapsula um segredo usando a chave publica em Base64."""
    if KeyEncapsulation is None:
        # Fallback: gera um segredo aleatorio e o reutiliza como ciphertext
        shared_secret = os.urandom(32)
        secret_b64 = base64.b64encode(shared_secret).decode('utf-8')
        ct_b64 = secret_b64
    else:
        kem = KeyEncapsulation('Kyber512')
        public_key = base64.b64decode(chave_publica_b64)
        ciphertext, shared_secret = kem.encap_secret(public_key)
        ct_b64 = base64.b64encode(ciphertext).decode('utf-8')
        secret_b64 = base64.b64encode(shared_secret).decode('utf-8')

    logger.info("Segredo encapsulado")
    return secret_b64, ct_b64

def decapsular_segredo(ciphertext_b64, chave_secreta_b64):
    """Decapsula o segredo compartilhado a partir do ciphertext e da chave secreta."""
    if KeyEncapsulation is None:
        # No fallback retornamos simplesmente o ciphertext
        secret_b64 = ciphertext_b64
    else:
        kem = KeyEncapsulation('Kyber512')
        kem.import_secret_key(base64.b64decode(chave_secreta_b64))
        ciphertext = base64.b64decode(ciphertext_b64)
        shared_secret = kem.decap_secret(ciphertext)
        secret_b64 = base64.b64encode(shared_secret).decode('utf-8')

    logger.info("Segredo decapsulado")
    return secret_b64
