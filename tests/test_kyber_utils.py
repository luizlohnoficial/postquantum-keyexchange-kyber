"""Testes unitarios para o modulo kyber_utils."""

# Importa o modulo pytest para as assercoes
import pytest
import sys
import os

# Ajusta o caminho para que seja possivel importar o pacote local
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importa as funcoes que serao testadas
from src import kyber_utils


def test_geracao_par_chaves():
    """Verifica se a geracao de chaves retorna strings nao vazias."""
    public, secret = kyber_utils.gerar_par_chaves()
    assert isinstance(public, str)
    assert isinstance(secret, str)
    assert public != ""
    assert secret != ""


def test_encapsulamento_decapsulamento():
    """Garante que o segredo decapsulado eh igual ao original."""
    public, secret = kyber_utils.gerar_par_chaves()
    shared_a, ciphertext = kyber_utils.encapsular_segredo(public)
    shared_b = kyber_utils.decapsular_segredo(ciphertext, secret)
    assert shared_a == shared_b
