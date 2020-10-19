## Aula 1
 - Alteramos a estrutura da url para que o arquivo raiz _urls.py_ import a urp da app usando ```
from clientes import urls as clients_urls``` e dentro das urlpatterns adicionou o campo ``` path('person/', include(clients_urls)),``` que irá chamar o url do app cliente
 - O app cliente terá uma urlpattern em _clientes/urls.py_ chamada ```path('list/', person_list),``` que irá chamar a função da view person_list. Assim a url para a app será ```localhost:8000/person/list```
 - para recuperar os dados basta chamar o model a ser analisado  ```from .models import Cliente``` e excuar a query, no caso ```
    clientes = Cliente.objects.all()```
    
