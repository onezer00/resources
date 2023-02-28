# API de Recursos
Uma API RESTful que permite que os usuários criem, leiam, atualizem e excluam recursos. A implementação foi feita utilizando django-rest-framework com autenticação e documentação personalizada.

## Configuração
Antes de executar a API, é necessário configurar o ambiente de desenvolvimento. Recomendamos utilizar o Poetry ou o Pyenv para gerenciar as dependências do projeto.
### Instalação das dependências com o Poetry
Caso opte por utilizar o Poetry, primeiro instale-o seguindo as instruções da [documentação oficial](https://python-poetry.org/docs/#installing-with-the-official-installer). Em seguida, na raiz do projeto, execute o comando abaixo para instalar as dependências:
```poetry install```

### Instalação das dependências com o Pyenv
Caso opte por utilizar o Pyenv, primeiro instale-o seguindo as instruções da [documentação oficial](https://github.com/pyenv/pyenv#installation). Em seguida, crie um ambiente virtual para o projeto e instale as dependências:
```py
# Criação do ambiente virtual
pyenv virtualenv 3.9.0 myenv
pyenv local myenv

# Instalação das dependências
pip install -r requirements.txt
```
### Configuração do VSCode
Para editar o código fonte, recomendamos utilizar o Visual Studio Code. Para configurar o ambiente de desenvolvimento no VSCode, crie um ambiente virtual utilizando o Poetry ou o Pyenv e abra a pasta do projeto no VSCode.

Em seguida, abra o arquivo `settings.json` no VSCode (pressione `Ctrl+Shift+P`, digite "Preferences: Open User Settings" e pressione Enter) e adicione as seguintes linhas ao final do arquivo:
```json
{
    "python.pythonPath": "/path/to/your/virtualenv/bin/python",
    "python.autoComplete.extraPaths": [
        "./resources"
    ]
}
```
Substitua o caminho em `"python.pythonPath"` pelo caminho para o executável do Python dentro do seu ambiente virtual. Certifique-se também de adicionar o caminho para a pasta resources em `"python.autoComplete.extraPaths"`, para que o VSCode possa encontrar as definições das classes.
### Execução dos comandos do Django
```sh
# Criação das migrações
python manage.py makemigrations

# Execução das migrações
python manage.py migrate

# Caso não tenha a variável de ambiente DJANGO_SETTINGS_MODULE configurada, execute o comando abaixo

# Criação das migrações
python manage.py makemigrations --settings=app.settings

# Execução das migrações
python manage.py migrate --settings=app.settings
```
PS: `Certifique-se de que o ambiente virtual está ativado antes de executar esses comandos.`

## Rodando a API
Para rodar a API, basta executar o comando abaixo na raiz do projeto:

```python manage.py runserver```
Isso iniciará um servidor de desenvolvimento em http://127.0.0.1:8000/.

## Documentação
A documentação da API pode ser encontrada em http://127.0.0.1:8000/docs/. Essa página foi gerada automaticamente a partir das views criadas no Django e fornece informações sobre como usar cada endpoint da API, bem como exemplos de requisições e respostas.

Também é possível acessar o schema da API em http://127.0.0.1:8000/api_schema/. Esse schema é compatível com a especificação OpenAPI e pode ser usado para gerar código cliente em diversas linguagens de programação.

## Endpoints
A API possui os seguintes endpoints:

## GET /
Endpoint principal da API. Retorna uma mensagem de boas-vindas.

## POST /user/create/
Cria um novo usuário. Recebe como parâmetros um nome de usuário (`username`), um e-mail (`email`) e uma senha (`password`).

## POST /user/login/
Autentica um usuário e gera um token de autenticação que pode ser usado para acessar endpoints protegidos. Recebe como parâmetros um nome de usuário (`username`) e uma senha (`password`).

## POST /user/logout/
Invalida o token de autenticação de um usuário, obrigando-o a se autenticar novamente para acessar endpoints protegidos.

## GET /recursos/
Lista todos os recursos cadastrados na API. É necessário estar autenticado para acessar esse endpoint.

## POST /recursos/
Cria um novo recurso. Recebe como parâmetros um nome (nome) e uma descrição (descricao). É necessário estar autenticado para acessar esse endpoint.

## GET /recursos/:id/
Retorna os detalhes de um recurso específico identificado pelo seu ID. É necessário estar autenticado para acessar esse endpoint.

## PUT /recursos/:id/
Atualiza um recurso específico identificado pelo seu ID. Recebe como parâmetros um nome (`nome`) e uma descrição (`descricao`). É necessário estar autenticado para acessar esse endpoint.

## DELETE /recursos/:id/
Exclui um recurso específico identificado pelo seu ID. É necessário estar autenticado para acessar esse endpoint.

Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.