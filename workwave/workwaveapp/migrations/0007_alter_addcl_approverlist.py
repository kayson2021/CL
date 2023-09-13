# Generated by Django 4.2.4 on 2023-08-24 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workwaveapp', '0006_alter_addcl_approverlist_alter_userregistration_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcl',
            name='ApproverList',
            field=models.ForeignKey(blank=True, limit_choices_to={'isApprover': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workwaveapp.userregistration', to_field='name', verbose_name='Approver姓名'),
        ),
    ]
