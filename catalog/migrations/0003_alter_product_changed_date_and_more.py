# Generated by Django 4.2.1 on 2023-06-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='changed_date',
            field=models.DateField(verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(verbose_name='Дата создания'),
        ),
    ]