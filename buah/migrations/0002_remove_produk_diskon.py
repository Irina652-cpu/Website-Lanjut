# Generated by Django 4.1.2 on 2022-10-22 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buah', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='diskon',
        ),
    ]
