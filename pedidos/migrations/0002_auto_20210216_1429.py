# Generated by Django 3.1.3 on 2021-02-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complement',
            field=models.CharField(blank=True, max_length=250, verbose_name='Complemento'),
        ),
    ]
