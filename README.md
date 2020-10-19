## Aula 1
 - Alteramos a estrutura da url para que o arquivo raiz _urls.py_ import a urp da app usando ```
from clientes import urls as clients_urls``` e dentro das urlpatterns adicionou o campo ``` path('person/', include(clients_urls)),``` que irá chamar o url do app cliente
 - O app cliente terá uma urlpattern em _clientes/urls.py_ chamada ```path('list/', person_list),``` que irá chamar a função da view person_list. Assim a url para a app será ```localhost:8000/person/list```
 - para recuperar os dados basta chamar o model a ser analisado  ```from .models import Cliente``` e excuar a query, no caso ```
    clientes = Cliente.objects.all()```
    
## Aula 2
 - Para lidar com inserção de usuarios é usado o django forms, disponível [aqui](https://docs.djangoproject.com/en/3.1/topics/forms/)
 - Para cirar um usuario é preciso ter um formulario válido que valide os  dados, então é criado o arquivo _forms.py_ que contém os campos do formulário e os seus dados são validados de acordo com o banco de dados
 - o formulário é então injetado no template com os parâmetros ```form = PersonForm(request.POST, request.FILES, None)``` onde o POST indica que só aeitará post e request.FILES indica que ele aceita arquivos
 
## Aula 3
 - Para aplicar o update basta criar uma url com o padrão ```cliente = get_object_or_404(Cliente, pk=id)``` de resto igual a classe person_new
 - Assim ao acessar a url de edição do cliente será prenchido com os dados do cliente, caso contrário será inserido novo usuario
 
