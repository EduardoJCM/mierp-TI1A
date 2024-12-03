# Generated by Django 5.1.1 on 2024-11-27 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoinventario',
            name='pedido',
            field=models.ForeignKey(blank=True, help_text='Referencia al pedido que originó este movimiento, si aplica.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.pedido'),
        ),
    ]