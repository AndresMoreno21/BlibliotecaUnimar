# Generated by Django 2.1.3 on 2018-11-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0002_auto_20181116_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='imagen',
            field=models.ImageField(upload_to='Biblioteca/BibliotecaUnimar/templates/static/'),
        ),
    ]