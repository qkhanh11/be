# Generated by Django 5.1 on 2024-09-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0043_qncn_cvmodel_qncn_dvmodel_vc_dvmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thekhachmodel',
            name='SoThe',
            field=models.CharField(max_length=5),
        ),
    ]
