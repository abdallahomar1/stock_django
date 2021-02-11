# Generated by Django 3.1.5 on 2021-01-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0007_auto_20210125_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodect',
            name='brice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='عدد الامتار في الكرتونة'),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='buybrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' سعر بيع المتر قطاعي '),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='count_f',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name=' عدد البلاط في الكرتونة الواحدة'),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='cwan',
            field=models.DecimalField(decimal_places=2, help_text='اكتب عدد الكراتين الموجودة من هذا المنتج', max_digits=5, verbose_name='عدد المشترى من المنتج'),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='jomlprice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' سعر بيع المتر لعملاء الجملة'),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='سعر شراء المنتج '),
        ),
    ]