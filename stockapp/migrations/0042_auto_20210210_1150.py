# Generated by Django 3.1.5 on 2021-02-10 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0041_auto_20210209_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders5',
            options={'ordering': ['-date_time'], 'verbose_name': 'فاتورة', 'verbose_name_plural': 'اضف او عدل فاتورة'},
        ),
    ]