# Generated by Django 5.1 on 2024-09-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0034_cvqncnmodel_tinhtrang_cvsiquanmodel_tinhtrang'),
    ]

    operations = [
        migrations.AddField(
            model_name='capbacmodel',
            name='TinhTrang',
            field=models.BooleanField(default=True),
        ),
    ]
