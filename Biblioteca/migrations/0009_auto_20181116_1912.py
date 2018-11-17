# Generated by Django 2.1.3 on 2018-11-17 00:12

import Biblioteca.models
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0008_auto_20181116_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='editorial',
        ),
        migrations.AddField(
            model_name='editorial',
            name='libros',
            field=multiselectfield.db.fields.MultiSelectField(default=1, max_length=200, verbose_name=Biblioteca.models.Libro),
            preserve_default=False,
        ),
    ]
