# Generated by Django 3.1.5 on 2021-01-27 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0016_orders5'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders5',
            old_name='name',
            new_name='names',
        ),
    ]
