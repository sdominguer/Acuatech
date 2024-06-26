# Generated by Django 5.0.1 on 2024-03-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('ciudad_residencia', models.CharField(max_length=100)),
            ],
        ),
    ]
