# Generated by Django 3.2 on 2022-03-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('total', models.PositiveIntegerField(blank=True, verbose_name='Total')),
                ('total_price', models.PositiveIntegerField(blank=True, verbose_name='Precio Total')),
                ('active', models.BooleanField(default=True, verbose_name='Actividad')),
                ('cars', models.ManyToManyField(to='cars.Car', verbose_name='Carros')),
            ],
        ),
    ]
