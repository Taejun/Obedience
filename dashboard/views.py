# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, check_password

def main(request):
    return HttpResponse("main page")

def login_view(request):
    t = get_template('login_view.html')
    html = t.render(Context({'message': "login page"}))
    return HttpResponse(html)

def User_Auth(request):
    username = request.GET['username']
    password = request.GET['passkey']
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponse("login ok")
        else: 
            return HttpResponse("login false")
    else :
        return HttpResponse("invalid login")