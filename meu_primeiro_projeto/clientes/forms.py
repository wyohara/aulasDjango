from django.forms import ModelForm
from .models import Cliente


class PersonForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
