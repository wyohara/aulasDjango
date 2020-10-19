from django.http import HttpResponse
from django.shortcuts import render

'''
Arquivo contendo as views do site

toda view tem um httpResponse
'''


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse(f"O ano fornecido foi {year}")


def ler_pessoa_banco(nome):
    # simulando resultado no banco de dados
    lista_nomes = [
        {'nome': "ana", "idade": 7},
        {'nome': "joao", "idade": 45},
        {'nome': "maria", "idade": 17},
        {'nome': "carlos", "idade": 22}
    ]
    # listando as pessoas
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa

    return {"nome": "Pessoa não encontrada", "idade": 0}


def find_name(request, nome):
    # pesquisando a pessoa e retornando os dados
    pessoa = ler_pessoa_banco(nome)
    if pessoa['idade'] == 0:
        return render(request, "pessoa.html")
    else:
        return render(request, "pessoa.html", {'idade': pessoa['idade'], "nome": pessoa['nome']})  # passando a url com
        # o json de idade
