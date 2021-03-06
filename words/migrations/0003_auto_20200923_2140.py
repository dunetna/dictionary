# Generated by Django 3.1.1 on 2020-09-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20200923_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='description',
            field=models.TextField(verbose_name='definition'),
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='word'),
        ),
    ]
