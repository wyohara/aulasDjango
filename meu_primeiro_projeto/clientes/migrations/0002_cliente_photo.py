# Generated by Django 3.1.2 on 2020-10-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='client_photos'),
        ),
    ]