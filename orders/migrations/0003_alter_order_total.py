# Generated by Django 3.2 on 2022-03-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Total'),
        ),
    ]
