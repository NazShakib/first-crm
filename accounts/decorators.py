from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fun):
    def wapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_fun(request,*args, **kwargs)
    return wapper_fun



def allowed_users(allowed_roles=[]):
    def decorator(view_fun):
        def wapper_fun(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_fun(request,*args, **kwargs)
            else:
                return HttpResponse('You are not allowed')
        return wapper_fun
    return decorator


def admin_only(view_fun):
    def wapper_fun(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
             group = request.user.groups.all()[0].name
        
        if group =='customer':
            return redirect('user')
        
        elif group =='admin':
            return view_fun(request, *args, **kwargs)
    return wapper_fun