"""
URL configuration for workwave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workwaveapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('registration/', views.registration),
    path('submit_registration/', views.submit_registration, name = "submit_registration"),
    path('login/', views.login, name="login"),
    path('submit_login/', views.submit_login, name="submit_login"),
    path('logout/', views.logout, name = "logout"),
    path('CL_application/', views.cl_application, name="CL_application"),
    path('add_cl/', views.add_cl, name = "add_cl"),
    path('<int:uid>/my_record/', views.my_record, name = "my_record"),
    path('approver_page/', views.approver_page, name = "approver_page"),
    path('approver_page/approve/', views.approver_page_approve, name = "approver_page_approve"),
    path('approver_page/reject/', views.approver_page_reject, name = "approver_page_reject"),
    
]
