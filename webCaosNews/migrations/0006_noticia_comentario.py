# Generated by Django 3.2.4 on 2021-06-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webCaosNews', '0005_noticia_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='comentario',
            field=models.TextField(default='-'),
        ),
    ]
