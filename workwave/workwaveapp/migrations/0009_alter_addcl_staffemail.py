# Generated by Django 4.2.4 on 2023-08-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workwaveapp', '0008_alter_addcl_accumuatedtotalothour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcl',
            name='Staffemail',
            field=models.EmailField(max_length=32, verbose_name='電郵'),
        ),
    ]
