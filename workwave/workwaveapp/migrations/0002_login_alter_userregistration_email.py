# Generated by Django 4.2.4 on 2023-08-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workwaveapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='email',
            field=models.EmailField(max_length=32, unique=True, verbose_name='電郵'),
        ),
    ]
