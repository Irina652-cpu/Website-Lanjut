# Generated by Django 3.1.14 on 2022-12-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buah', '0011_auto_20221210_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='deskripsi',
        ),
        migrations.AlterField(
            model_name='produk',
            name='harga',
            field=models.TextField(),
        ),
    ]
