# Generated by Django 3.1.5 on 2021-02-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0033_auto_20210205_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders5',
            name='num',
        ),
        migrations.AlterField(
            model_name='orders5',
            name='count_5',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='العدد المطلوب'),
        ),
    ]
