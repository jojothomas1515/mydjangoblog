from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from django.contrib.messages import success, error
from django.urls import reverse

from .forms import SignupForm, LoginForm
from .isauth import is_authenticated


# Create your views here.
def Logout(request):
    logout(request)
    return redirect('login')

@is_authenticated
def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                error(request, message='Invalid username or password')
                return render(request, 'signupandlogin/Login.html')
        else:
            error(request, message='invalid inputs')
            return render(request, 'signupandlogin/Login.html')

    return render(request, 'signupandlogin/Login.html')

@is_authenticated
def signupPage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(form.data)
        print(form.data['password1'] != form.data['password2'])

        if form.is_valid():
            form.save()
            success(request, message="User Created Successfully, Login Now")
            return redirect('login')
        else:
            error(request, message=form.errors)
            return render(request, 'signupandlogin/signup.html')

    return render(request, 'signupandlogin/signup.html')

