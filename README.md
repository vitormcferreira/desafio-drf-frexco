# desafio-drf-frexco

## Iniciar a API
Projeto criado usando Django e Django Rest Framework.

```
# Clona o repositório para a pasta atual
git clone https://github.com/vitormcferreira/desafio-drf-frexco.git

# Entra na pasta do repositório
cd desafio-drf-frexco

# Inicia o ambiente virtual e instala as dependências
pipenv install

# Entra no ambiente virtual
pipenv shell

# faz as migrações
python manage.py migrate

# inicia o servidor
python manage.py runserver
```

Para acessar a documentação da API acesse http://localhost:8000/api/docs/



## Desafio Tech (Python)

- Criar uma API usando a linguagem Python, frameworks: Django e Django Rest 
  Framework.
- A API deverá realizar a comunicação com um banco de dados SQL qualquer (pode 
  ser SQLite)
- O banco deverá ter pelo menos duas tabelas: 
    - Uma tabela chamada “Region” que conterá apenas uma coluna “name” com 
      informação dos nomes das regiões do Brasil ( Norte, Nordeste, etc.)
    - Uma tabela chamada “Fruit” que conterá colunas “name” (o nome da fruta) 
      e uma coluna de associação por chave estrangeira (foreign key) com a 
      tabela “Region” associando cada fruta a uma região existente na primeira 
      tabela.
- Para cada tabela, a API deve conter os quatro métodos GET, POST, PUT e 
  DELETE.
