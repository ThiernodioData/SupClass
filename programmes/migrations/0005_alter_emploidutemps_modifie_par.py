# Generated by Django 5.1.4 on 2024-12-18 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0004_utilisateur_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emploidutemps',
            name='modifie_par',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programmes.utilisateur'),
        ),
    ]
