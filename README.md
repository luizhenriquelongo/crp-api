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
$ pipenv run python wsgi.py
```

Aplicação ficará disponivel na url `http://0.0.0.0:5000/`

## Uso:

- #### Endpoint:

> `http://0.0.0.0:5000/api/crp`

- #### Request Method:

> GET

- #### Body:

```json
{
  "cpf": "12345678901",
  "crp": "123456"
}
```

## To do:

- Testes, testes e testes;
- Persistir dados retornados pela API para evitar consultas via selenium;
- Reestruturar aplicação utilizando Django e Django REST Framework;
- Documentar API;
- Dockerizar aplicação;
- Fazer deploy no Heroku;

## Autor

- [Luiz Henrique Longo](https://linkedin.com/in/luizhenriquelongo)
