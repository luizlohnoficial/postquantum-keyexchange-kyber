"""Exemplo de conexao com o Google Quantum Engine utilizando Cirq."""

# Importa bibliotecas necessarias
import os
import logging
import cirq
from cirq_google.engine import Engine

# Configura o logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def rodar_circuito():
    """Executa um circuito simples no Google Quantum Engine."""
    logger.info("Iniciando execucao do circuito no Quantum Engine")
    # Recupera o ID do projeto configurado em variavel de ambiente
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        raise EnvironmentError("Variavel GOOGLE_CLOUD_PROJECT nao definida")

    # Instancia o engine do Google para o projeto especificado
    logger.info("Conectando ao projeto %s", project_id)
    engine = Engine(project_id=project_id)

    # Define um qubit na posicao (0, 0) da grade
    qubit = cirq.GridQubit(0, 0)

    # Constroi um circuito simples aplicando uma porta Hadamard e medindo
    circuito = cirq.Circuit(
        cirq.H(qubit),
        cirq.measure(qubit, key="m"),
    )

    # Executa o circuito em modo de simulacao no engine
    resultado = engine.run(program=circuito, job_id="exemplo-job", repetitions=1)
    logger.info("Circuito executado")

    # Exibe o resultado obtido
    logger.info("Resultado obtido: %s", resultado)


if __name__ == "__main__":
    rodar_circuito()
