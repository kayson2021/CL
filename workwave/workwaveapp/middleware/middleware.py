from django.shortcuts import redirect, HttpResponse

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path_info == '/login/' or 'submit_login/':
            return self.get_response(request)

        info_dict = request.session.get("info")
        print(info_dict)
        if info_dict:
            return self.get_response(request) 
        return redirect('/login/')


        
"""
    def process_response(self, request, response):
        pass
    
        #return redirect('CL_application/')
"""
