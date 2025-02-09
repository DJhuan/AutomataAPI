# AUTOMATA API

API para manipulação de AFD, ACP e MT

## Como inicializar

Após clonar o repositório instale os pacotes com:

`pip install -r requirements.txt`

Feito isso, inicie a api:

`fastapi main.py`
ou
`fastapi dev main.py`

## Como utilizar a API

### Rotas para AFD (Autômato Finito Determinístico)

- **Criar um novo AFD**
  - **POST** `/afd/`
  - Corpo da requisição: JSON com a definição do AFD

- **Obter um AFD pelo ID**
  - **GET** `/afd/{id}`

- **Obter a imagem de um AFD pelo ID**
  - **GET** `/afd/image/{id}`

- **Executar um AFD com uma palavra**
  - **POST** `/afd/{id}`
  - Corpo da requisição: JSON com a palavra a ser processada

### Rotas para ACP (Autômato com Pilha)

- **Criar um novo ACP**
  - **POST** `/acp/`
  - Corpo da requisição: JSON com a definição do ACP

- **Obter um ACP pelo ID**
  - **GET** `/acp/{id}`

- **Obter a imagem de um ACP pelo ID**
  - **GET** `/acp/image/{id}`

- **Executar um ACP com uma palavra**
  - **POST** `/acp/{id}`
  - Corpo da requisição: JSON com a palavra a ser processada

### Rotas para MT (Máquina de Turing)

- **Criar uma nova MT**
  - **POST** `/mt/`
  - Corpo da requisição: JSON com a definição da MT

- **Obter uma MT pelo ID**
  - **GET** `/mt/{id}`

- **Executar uma MT com uma palavra**
  - **POST** `/mt/{id}`
  - Corpo da requisição: JSON com a palavra a ser processada

---

### Para exemplos de máquinas procure na pasta `/exemplos