from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from accounts.forms import Loginform, RegisterForm


# Create your views here.


def login_view(request):
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('courses:index')
            else:
                messages.add_message(request,
                                     messages.EROR,
                                     'Invalid login')

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('courses:index')


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True

            user.save()
            login(request, user)
            return redirect('courses:index')
    return render(request, 'accounts/register.html', {'form': form})



