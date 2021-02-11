# Generated by Django 3.1.5 on 2021-01-27 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0015_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم العميل')),
                ('num', models.IntegerField(verbose_name='رقم الفاتورة')),
                ('count', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='العدد المطلوب')),
                ('date_time', models.DateTimeField(null=True, verbose_name='وقت عملية الشراء')),
                ('date2', models.DateField(auto_now_add=True, help_text='الامتار', verbose_name='وقت عملية الشراء')),
                ('prodects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='stockapp.prodect', verbose_name='المنتج')),
            ],
            options={
                'verbose_name': 'الطلب',
                'verbose_name_plural': 'الطلبات',
            },
        ),
    ]
