# Generated by Django 4.2.4 on 2023-08-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workwaveapp', '0009_alter_addcl_staffemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcl',
            name='ApprovalStatus',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Approval Status'),
        ),
        migrations.AlterField(
            model_name='addcl',
            name='ApproverEmail',
            field=models.EmailField(blank=True, max_length=32, null=True, verbose_name='Approver電郵'),
        ),
    ]