# Generated by Django 2.1.3 on 2018-11-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
