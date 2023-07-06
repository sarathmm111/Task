from django.shortcuts import render
# Create your views here.
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['password1']

        if password == conf_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('user:register')

            else:
                user = User.objects.create_user(
                    username=user_name, password=password
                )
                user.save()
                messages.info(request, 'Welcome')
        else:
            messages.info(request, 'Password not matched')
            return redirect('user:register')

        return redirect('user:login')

    return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('user:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
