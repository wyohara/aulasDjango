from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm


def person_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'crud_person.html', {'clientes': clientes})


def person_new(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'form_person.html', {'form': form})


def person_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'form_person.html', {'form': form})
