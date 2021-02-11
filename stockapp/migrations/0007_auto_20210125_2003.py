# Generated by Django 3.1.5 on 2021-01-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0006_auto_20210125_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prodect',
            options={'verbose_name': 'المنتج', 'verbose_name_plural': 'النتجات'},
        ),
        migrations.AddField(
            model_name='prodect',
            name='count_f',
            field=models.IntegerField(null=True, verbose_name=' عدد البلاط في الكرتونة الواحدة'),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='buybrice',
            field=models.IntegerField(verbose_name=' سعر بيع المتر قطاعي '),
        ),
    ]
