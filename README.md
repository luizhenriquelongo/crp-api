# CRP API

Api desenvolvida para validar o número de registro de profissionais do ramo da psicologia junto ao Conselho Federal de Psicologia.

## Problemática:

Com a necessidade de validar o CRP e sem encontrar APIs que fizessem isso, resolvi criar uma API que utiliza o [Selenium]('https://selenium-python.readthedocs.io/') para verificar se o profissional possui um CRP válido. Utilizando seu Numero de Registro(CRP) e seu CPF é possível validar esta informação.

## Instalando o Projeto:

### Pré requisitos:

- [Python 3.8](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Pipenv](https://pypi.org/project/pipenv/)

Instale os pacotes utilizando o comando:

```bash
$ pipenv install
```

Em seguida, no diretório do projeto, execute o comando:

```bash
$ pipenv run uvicorn main:app
```

Aplicação ficará disponivel na url `http://0.0.0.0:8000/`

## Uso da API:

> `http://0.0.0.0:8000/docs`

## Autor

- [Luiz Henrique Longo](https://linkedin.com/in/luizhenriquelongo)
