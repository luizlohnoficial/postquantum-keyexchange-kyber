# Projeto de Troca de Chaves Kyber

Este projeto demonstra uma implementacao simples de troca de chaves pos-quantica utilizando o algoritmo Kyber em Python.

## Estrutura

```
/src
  __init__.py
  kyber_utils.py
  api_server.py
  quantum_engine.py
/tests
  test_kyber_utils.py
/docker
  Dockerfile
requirements.txt
README.md
.gitlab-ci.yml
```

## Como Executar

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Rode os testes unitarios:

```bash
pytest
```

3. Inicie a API:

```bash
python -m src.api_server
```

A API ficara disponivel em `http://localhost:5000`.

## Endpoints

- `POST /generate` - gera um novo par de chaves
- `POST /encapsulate` - encapsula um segredo a partir da chave publica
- `POST /decapsulate` - decapsula o segredo a partir do ciphertext

## Conexao com o Google Quantum Engine

O arquivo `quantum_engine.py` apresenta um exemplo de circuito executado no Google Cloud utilizando a biblioteca Cirq. Para usar:

1. Crie um projeto no Google Cloud e ative o Quantum Engine.
2. Defina as variaveis de ambiente `GOOGLE_CLOUD_PROJECT` e `GOOGLE_APPLICATION_CREDENTIALS` com seu ID de projeto e caminho para a chave de servico.
3. Execute o script:

```bash
python -m src.quantum_engine
```

O resultado do circuito sera exibido no terminal.

## Logs

Todas as etapas do processo de troca de chaves e da execucao do circuito
quantico sao registradas em logs no console. Esses logs auxiliam no
acompanhamento da geracao de chaves, encapsulamento, decapsulamento e
conexao ao Google Quantum Engine.

## Docker

Para construir a imagem Docker execute:

```bash
docker build -t kyber_exchange -f docker/Dockerfile .
```

## Pipeline CI/CD

O arquivo `.gitlab-ci.yml` contem as etapas de build, test, docker e deploy.
Um workflow equivalente para o GitHub Actions esta disponivel em
`.github/workflows/ci.yml`.

## Referencias

- https://github.com/Argyle-Software/kyber
- https://github.com/fisherstevenk/kyberJCE
- https://github.com/antontutoveanu/crystals-kyber-javascript
