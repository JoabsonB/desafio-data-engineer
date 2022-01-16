# Desafio

## Execução do ambiente

Para executar a aplicação, execute o seguinte comando
```sh
docker-compose up --build
```

**Nota importante:** Ao executar o comando, todo o procedimento automático irá acontecer:

1. Download dos Arquivos *.csv
2. Tratamento e inserção dos dados do CSV no banco de dados (MySQL)
3. Inicialização do Jupyter Notebook

Para acessar o Jupyter Notebook, ver a url no log do docker. (token)

## Justificativa
*TODO*

### Comando para pegar o working directory do Jupyter
```python
from pathlib import Path

print(Path.cwd())  # /home/skovorodkin/stack
```