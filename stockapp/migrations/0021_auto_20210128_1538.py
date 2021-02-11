# Generated by Django 3.1.5 on 2021-01-28 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0020_auto_20210127_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders5',
            options={'ordering': ['-date_time'], 'verbose_name': 'الطلب', 'verbose_name_plural': 'الطلبات'},
        ),
        migrations.AddField(
            model_name='prodect',
            name='new',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockapp.orders5', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='orders5',
            name='date2',
            field=models.DateField(auto_now_add=True, help_text='الامتار', verbose_name='وقت العملية '),
        ),
    ]