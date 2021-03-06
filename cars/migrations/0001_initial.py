# Generated by Django 3.2 on 2022-03-11 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombres')),
                ('price', models.PositiveIntegerField(verbose_name='Precio')),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='codigo')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyers.buyer', verbose_name='Comprador')),
            ],
        ),
    ]
