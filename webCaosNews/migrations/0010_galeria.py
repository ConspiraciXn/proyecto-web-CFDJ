# Generated by Django 3.2.4 on 2021-07-03 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webCaosNews', '0009_auto_20210630_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='galeriaNoticia')),
                ('Noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webCaosNews.noticia')),
            ],
        ),
    ]