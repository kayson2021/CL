from django.shortcuts import redirect, HttpResponse
from workwaveapp import models


class AppUser(object):

    def __init__(self):
        self.user = None


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):

        request.appUser = AppUser()

        if request.path_info in ('/login/', '/submit_login/'):
            return self.get_response(request)
        
        info_dict = request.session.get("info")
        print({"info_dict":info_dict})
        if info_dict is not None:
            user_id = info_dict['id']
            user_object = models.UserRegistration.objects.filter(id=user_id).first()
            print({"user_object":user_object})
            request.appUser.user = user_object.email
            print({"request.appUser.user":request.appUser.user})
            return self.get_response(request) 
        
        return redirect('/login/')

