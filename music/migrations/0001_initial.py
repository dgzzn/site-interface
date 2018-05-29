# Generated by Django 2.0.5 on 2018-05-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('capa', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
