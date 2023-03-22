from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponse,Http404

def Custlogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.POST:
        user_name=request.POST["username"]
        pass_word=request.POST["password"]
        user=authenticate(request,username=user_name,password=pass_word)
        if user is not None:
            login(request,user)
            #messages.success(request,f'logged in as {user_name}')
            return redirect('dashboard')
        else:
            messages.error(request,f"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'Accounts/login.html')
    
def Custlogout(request):
    logout(request)
    return render(request,"Accounts/logout.html")
