# Generated by Django 4.2.4 on 2023-08-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workwaveapp', '0002_login_alter_userregistration_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=32, verbose_name='電郵'),
        ),
    ]
