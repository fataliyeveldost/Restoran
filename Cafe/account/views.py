from django.shortcuts import redirect, render
from.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from cafe import urls
# Create your views here.


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # user=CustomUser.objects.get(username=username)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('menyu')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')