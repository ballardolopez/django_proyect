# Generated by Django 3.2.16 on 2022-10-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20221012_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(max_length=150, null=True, verbose_name='Descripcion'),
        ),
    ]
