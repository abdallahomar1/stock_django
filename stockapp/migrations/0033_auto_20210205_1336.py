# Generated by Django 3.1.5 on 2021-02-05 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0032_prodect_kind2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders5',
            options={'ordering': ['-date_time'], 'verbose_name': 'فاتورة', 'verbose_name_plural': 'الفواتير'},
        ),
    ]
