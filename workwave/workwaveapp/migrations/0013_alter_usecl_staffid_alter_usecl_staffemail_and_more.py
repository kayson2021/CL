# Generated by Django 4.2.4 on 2023-09-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workwaveapp', '0012_alter_addcl_totalothour_usecl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usecl',
            name='StaffID',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usecl',
            name='Staffemail',
            field=models.EmailField(max_length=32, verbose_name='電郵'),
        ),
        migrations.AlterField(
            model_name='usecl',
            name='Staffname',
            field=models.CharField(max_length=50, verbose_name='英文姓名'),
        ),
    ]
