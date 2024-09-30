# Generated by Django 5.1 on 2024-09-25 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0046_khachqncnmodel_trathekhach_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qncnmodel',
            old_name='NhomSQ',
            new_name='NhomQNCN',
        ),
        migrations.RenameField(
            model_name='qncnmodel',
            old_name='TinhTrang',
            new_name='TrangThai',
        ),
        migrations.RenameField(
            model_name='vienchucqpmodel',
            old_name='NgayBatDauLamViec',
            new_name='NgayBDLamViec',
        ),
        migrations.AlterField(
            model_name='thoigianquyenmodel',
            name='Thu',
            field=models.IntegerField(choices=[(0, 'Thứ 2'), (1, 'Thứ 3'), (2, 'Thứ 4'), (3, 'Thứ 5'), (4, 'Thứ 6'), (5, 'Thứ 7'), (6, 'Chủ nhật')]),
        ),
    ]
