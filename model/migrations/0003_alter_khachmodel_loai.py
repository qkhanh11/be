# Generated by Django 5.1 on 2024-10-02 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_donvimodel_tinhtrang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khachmodel',
            name='Loai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='model.loaikhachmodel'),
        ),
    ]
