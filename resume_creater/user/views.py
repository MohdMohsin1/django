from django.shortcuts import render,redirect
from .form import UserForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            remember_me = request.POST.get('remember_me')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if remember_me:
                    request.session.set_expiry(2592000)  # Expiry time of 30 days
            return redirect( '/')
        else:
            form.add_error('Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'user/login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully !!!')
    else:
        messages.error(request, "Something wrong here, it may be that you already have account!")
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})
