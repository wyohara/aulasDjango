# Aulas de django

## Aula 1
 - Estrutura do lifecycle do django [aqui](/imagens_adicionais/lifecycle.png)
 - Para iniciar projeto ```django-admin startproject meu_primeiro_projeto```
 - Para rodar o servidor localmente ```python manage.py runserver```
 
 Estrutura do django:
- ```manage.py```
- ```settings.py``` configurações do django. É o mais usado
   - OBS.: dentro do ```settings.py``` adicionar o campo ```STATIC_URL='/static/'``` para definir a url dos arquivos estáticos
- ```wsgi.py``` é o startpoint do django, é a partir dele que começa o serviço web


## Aula 2
 - Estrutura de [urls do Django](https://docs.djangoproject.com/en/3.1/topics/http/urls/)
