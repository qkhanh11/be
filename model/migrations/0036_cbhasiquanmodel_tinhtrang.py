# Generated by Django 5.1 on 2024-09-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0035_capbacmodel_tinhtrang'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbhasiquanmodel',
            name='TinhTrang',
            field=models.BooleanField(default=True),
        ),
    ]
