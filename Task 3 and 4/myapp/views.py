from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
# username: sangeeta
# admin password: pisb@123


def home(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pnum = request.POST['number']
        gender = request.POST['gender']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('home')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "username taken")
                return redirect('home')
            else:
                myUser = User.objects.create_user(
                    username=username, email=email, first_name=fname, last_name=lname, password=pass1)
                userProfile = Profile(user=myUser, phone=pnum, gender=gender)
                userProfile.save()
                myUser.save()
                return redirect('login')
                # return render(request, "myappp/login.html")
        else:
            messages.info(request, "Password not matching")
            return redirect('home')
    else:
        context = {}
        return render(request, 'myapp/signup.html', context)


def userLogin(request):
    if request.method == "POST":
        username = request.POST["login_username"]
        password = request.POST["login_password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return render(request, "myapp/userhome.html")
        else:
            return render(request, "myapp/login.html", {"message": "Invalid Credentials"})

    return render(request, "myapp/login.html")
    # return redirect('login')


def userHome(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return(request, 'myapp/userhome.html')


def userLogout(request):
    logout(request)
    return render(request, "myapp/login.html", {"message": "Logged out."})


def search(request):
    if request.method == 'POST':
        email = request.POST["email"]
        if email == '':
            messages.error(request, "email id is invalid!")
            return redirect('search')
        user = User.objects.filter(email=email)
        if len(user) == 0:
            messages.info(request, "No user found")
            return redirect('search')
        context = {'user': user}
        return render(request, 'myapp/search_user_info.html', context)
    return render(request, 'myapp/search.html')
