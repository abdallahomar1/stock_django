# Generated by Django 3.1.5 on 2021-02-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0030_auto_20210202_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodect',
            name='name',
            field=models.CharField(max_length=50, verbose_name='اسم المنتج'),
        ),
    ]
