from django.shortcuts import render, HttpResponse,reverse, redirect
from django import forms
from workwaveapp import models
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
import json
from datetime import datetime
from django.db.models import Sum


class BootStrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = "please enter %s" % (field.label)
            else:
                field.widget.attrs = {
                "class":"form-control", 
                "placeholder": field.label
                }


class UserRegistrationForm(BootStrapModelForm):
    class Meta:
        model = models.UserRegistration
        fields = "__all__"


def registration(request):

    form = UserRegistrationForm()
    return render(request, 'registration.html', {'form':form})


@csrf_exempt
def submit_registration(request):
    form = UserRegistrationForm(data=request.POST)

    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        # return JsonResponse({'status':True})
    else:
        print(form.errors)
        return JsonResponse({'status':False, 'error':form.errors})
    

class LoginForm(BootStrapModelForm):
    class Meta:
        model = models.Login
        fields = "__all__"


def login(request):

    form = LoginForm()
    return render(request, 'login.html',{'form':form})


@csrf_exempt
def submit_login(request):
    
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_data = form.cleaned_data
        #{'email': 'abc@test.com', 'password': '123'}
        check_user = models.UserRegistration.objects.filter(**user_data).first()
        print({"check" : check_user})
       
        if not check_user:
            form.add_error("password", "your password is incorrect")
            data_dict = {"status":False, 'error': form.errors}
            return JsonResponse(data_dict)
        request.session['info'] = {"id": check_user.id, 'name':check_user.name, "email":check_user.email}
        
        data_dict = {"status":True}
        return JsonResponse(data_dict)
        

def cl_application(request):
    
    return render(request, 'add_cl.html')


class AddCLForm(BootStrapModelForm):
    class Meta:
        model = models.AddCL
        fields = ['OT_start', 'OT_end', 'ApproverList', 'OT_reason','Remark', 'Hv_lunch', 'Hv_dinner' ]
        widgets = {
            'OT_start':DateTimePickerInput(),
            'OT_end':DateTimePickerInput(range_from='OT_start'),
            'Remark':forms.Textarea(attrs={"class": "form-control"})
        }


@csrf_exempt
def add_cl(request):
    info_dict = request.session['info']
    #print(info_dict) #{'id': 1, 'name': 'kk', 'email': 'abc@test.com'}
    uid = info_dict.get('id')
    username = info_dict.get('name')
    user_email = info_dict.get('email')
    form = AddCLForm()

    if request.method == "GET":
        return render(request,'add_cl.html', {'form':form, "info_dict":info_dict, "uid":uid })

    form = AddCLForm(data=request.POST)
    if form.is_valid():
       
        data_dict = {"status":True,}
        ot_start = form.cleaned_data['OT_start']
        ot_end = form.cleaned_data['OT_end']
        hv_lunch = form.cleaned_data['Hv_lunch']
        hv_dinner = form.cleaned_data['Hv_dinner']
        totalOThour =  ot_end - ot_start
        if (hv_lunch == 1 and hv_dinner == 1):
            form.instance.TotalOTHour = (totalOThour.total_seconds() / 3600) - 1.5
        elif (hv_lunch == 1):
            form.instance.TotalOTHour = (totalOThour.total_seconds() / 3600) - 1 
        elif (hv_dinner == 1):
            form.instance.TotalOTHour = (totalOThour.total_seconds() / 3600) - 0.5
        else:
            form.instance.TotalOTHour = totalOThour.total_seconds() / 3600
        
        #form.instance.TotalOTHour = (totalOThour.seconds/60)/60
        form.instance.Staffname = username
        form.instance.StaffID = uid    
        form.instance.Staffemail = user_email 
        approverName = form.cleaned_data['ApproverList']
        approverEmail = models.UserRegistration.objects.filter(name=approverName).first().email
        form.instance.ApproverEmail = approverEmail
        form.instance.ApprovalStatus = "Pending"
        form.save()
        return JsonResponse(data_dict)
    else:
        print(form.errors)
        data_dict = {"status":False, 'error': form.errors}
        return JsonResponse(data_dict)


def my_record(request,uid):
    #uid = request.session['info'].id
    row_object = models.AddCL.objects.filter(StaffID=uid).all
    print(row_object)

    return render(request, 'my_record.html',{"row_object":row_object})


def approver_page(request):
    
    print({"approver":request.appUser.user})
    row_object = models.AddCL.objects.filter(ApproverEmail=request.appUser.user).all
    
    return render(request, 'approver_page.html', {"row_object":row_object})


def approver_page_approve(request):

    # get the currect object 
    nid = request.GET.get('nid')
    
    # change approval status
    row_object = models.AddCL.objects.filter(id=nid).first()
    row_object.ApprovalStatus = "Approved"
 
    # add accumlated OT hrs as now
    
    accumulated_total = models.AddCL.objects.filter(ApprovalStatus="Approved").aggregate(total=Sum('TotalOTHour')).get('total')
    accumulated_total = accumulated_total or 0
    if row_object:
        row_object.AccumuatedTotalOTHour = accumulated_total + row_object.TotalOTHour
        row_object.save()
    # change approval column to Approved

    return redirect('/approver_page/')


def approver_page_reject(request):

    nid = request.GET.get('nid')
    row_object = models.AddCL.objects.filter(id=nid).first()
    row_object.ApprovalStatus = "Rejected"
    accumulated_total = models.AddCL.objects.filter(ApprovalStatus="Approved").exclude(id=nid).aggregate(total=Sum('TotalOTHour')).get('total')
    if row_object:
        row_object.AccumuatedTotalOTHour = accumulated_total
        row_object.save()

    return redirect('/approver_page/')





    
    




