from django.db import models
from django.db.models import UniqueConstraint
from django import forms

# Create your models here.

class UserRegistration(models.Model):
    name = models.CharField(verbose_name='英文姓名', max_length=50, unique=True)
    email = models.EmailField(verbose_name='電郵', unique=True, max_length=32)
    password = models.CharField(verbose_name='密碼', max_length=8)
    isApprover_choices = (
        (1, 'Yes'),
        (2, 'No')
    )
    isApprover = models.SmallIntegerField(verbose_name="是Approver嗎?", choices=isApprover_choices, default=2)

    def __str__(self):
        return self.name


class Login(models.Model):
    email = models.EmailField(verbose_name='電郵', max_length=32)
    password = models.CharField(max_length=8)

"""
    def __str__(self):
        return self.email
"""


class AddCL(models.Model):
    Staffname = models.CharField(verbose_name='英文姓名', max_length=50)
    StaffID = models.CharField(verbose_name='ID', max_length=4, null =True, blank=True)
    Staffemail = models.EmailField(verbose_name='電郵', max_length=32)
    OT_start = models.DateTimeField(verbose_name="OT開始時間")
    OT_end = models.DateTimeField(verbose_name="OT完結時間")
    TotalOTHour = models.DecimalField(verbose_name="OT總時數",max_digits=5, decimal_places=2)
    ApprovedTotalOTHour = models.DecimalField(verbose_name="OT總時數",max_digits=5, decimal_places=2, null =True, blank=True)
    AccumuatedTotalOTHour = models.DecimalField(verbose_name="OT總時數",max_digits=5, decimal_places=2, null =True, blank=True)
    ApproverList = models.ForeignKey(verbose_name='Approver姓名', to="UserRegistration", to_field="name",limit_choices_to={'isApprover': 1}, null =True, blank=True, on_delete=models.SET_NULL )
    ApproverEmail = models.EmailField(verbose_name='Approver電郵',  max_length=32, null =True, blank=True)
    ApprovalStatus = models.CharField(verbose_name='Approval Status',  max_length=32, null =True, blank=True)
    OT_reason = models.CharField(verbose_name="OT原因",max_length=200)
    Remark = models.CharField(verbose_name="Remark",max_length=200)
    Hv_meal_choices = (
        (1, 'Yes'),
        (2, 'No')
    )
    Hv_lunch = models.SmallIntegerField(verbose_name="有午餐?",choices=Hv_meal_choices, default=2)
    Hv_dinner = models.SmallIntegerField(verbose_name="有晚餐?",choices=Hv_meal_choices, default=2)

