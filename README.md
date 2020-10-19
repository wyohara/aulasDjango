# Aulas de django

## Aula 1
 - Estrutura do lifecycle do django [aqui](/imagens_adicionais/lifecycle.png)
 - Para iniciar projeto ```django-admin startproject meu_primeiro_projeto``` e será criado uma subpasta com as configurações
    - obs se digitar ```django-admin startproject meu_primeiro_projeto. ``` todos os arquivos de configuração ficarão na pasta raiz
 - Para rodar o servidor localmente ```python manage.py runserver```
 
 Estrutura do django:
- ```manage.py```
- ```settings.py``` configurações do django. É o mais usado
   - OBS.: dentro do ```settings.py``` adicionar o campo ```STATIC_URL='/static/'``` para definir a url dos arquivos estáticos
- ```wsgi.py``` é o startpoint do django, é a partir dele que começa o serviço web


## Aula 2
 - Estrutura de [urls do Django](https://docs.djangoproject.com/en/3.1/topics/http/urls/)

## Aula 3
 - Criando uma app para uma funcionalidade específica ```python manage.py startapp clientes```
 - As novas apps são registradas em INSTALLED_APPS dentro do arquivo ```settings.py```
 - A estrutura de models do django pode ser vista [aqui](https://docs.djangoproject.com/en/3.1/topics/db/models/)
 - Dentro da pasta base do projeto em ```settings.py``` existe o campo ```DATABASES``` que define o banco de dados. por padrão se usa  sqlite3
 - O banco de dados é criado na forma de migrations, assim para criar uma migration é usado o comando ```python manage.py makemigrations``` e para aplicar as migrations é usado ```python manage.py migrate```

## Aula 4
 - Para criar um superadmin no django usa-se ```python manage.py createsuperuser``` que é acesso pela url _/admin_
 - para registrar os models criados em uma app basta acessar o arquivo _admin.py_ e registrar o model com ```admin.site.register(Cliente)```
 
 ## Aula 5
 