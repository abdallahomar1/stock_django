# Generated by Django 3.1.5 on 2021-01-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم المنتج')),
                ('cwan', models.BooleanField(verbose_name='عدد الموجود من المنتج')),
                ('brice', models.BooleanField(verbose_name='عدد الامتار في الكرتونة')),
                ('price', models.BooleanField(verbose_name='سعر شراء المنتج ')),
                ('buybrice', models.BooleanField(verbose_name=' سعر بيع المنتج للعملاء العاديين')),
                ('jomlprice', models.BooleanField(verbose_name=' سعر بيع المنتج لعملاء الجملى')),
            ],
        ),
    ]
