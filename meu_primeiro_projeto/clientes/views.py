from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente


def person_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'crud_person.html', {'clientes':clientes})