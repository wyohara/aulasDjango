from django.db import models


# Create your models here.
class Cliente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    bio = models.TextField()
    photo = models.ImageField(upload_to="client_photos", null=True, blank=True)

    def __str__(self):  # exibindo um texto no admin do banco de dados
        return f"Cliente {self.first_name} {self.last_name}"
