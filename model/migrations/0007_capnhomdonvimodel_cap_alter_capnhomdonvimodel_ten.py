# Generated by Django 5.1 on 2024-08-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_remove_capnhomdonvimodel_cap_capnhomdonvimodel_ten'),
    ]

    operations = [
        migrations.AddField(
            model_name='capnhomdonvimodel',
            name='Cap',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='capnhomdonvimodel',
            name='Ten',
            field=models.CharField(max_length=20),
        ),
    ]
