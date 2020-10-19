from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from .forms import PersonForm


def person_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'crud_person.html', {'clientes': clientes})


def person_new(request):
    form = PersonForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'form_person.html', {'form': form})
