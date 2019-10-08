from django.shortcuts import render
from . import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'blogApp/index.html')

def register(request):
    registered = False

    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            print("validation success")
        else:
            print("validation error")
    else:
        form = forms.FormName()


    return render(request, 'blogApp/registeration.html',{'form':form,
                                                        'registered': registered,})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password=password)

        if user:
            print("user sutheticated")
            if user.is_active:
                login(request,user)
                print("login successfull")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'blogApp/login.html')
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))