from django.shortcuts import render, HttpResponse, redirect
from .models import movies01
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .form import rating

def movie_detail(request):
    model = movies01.objects.all()
    # if request == 'POST':
    #     fm = rating(request.POST)
    #     if fm.is_valid():
    #         movie = fm.cleaned_data['Title']
    #         rate = fm.cleaned_data['Rate']
    #         print(movie, rate)
    return render(request, 'table.html', {'model': model})
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, f"Your account successfully created {fname}")
        return redirect('signin')
    return render(request, 'signup.html')
def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            # fname=user.first_name
            return redirect('movie')
            # return render(request, 'index.html', {'fname': fname})
        else:
            messages.error(request, "please use your right credentials")
            return redirect('home')
    return render(request, 'signin.html')
def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully !')
    return redirect('home')
    # return render(request, 'signout.html')
def search(request):
    if request.method=='POST':
        search = request.POST['searched']
        Genre = movies01.objects.filter(Genre__contains=search)
        # print(Genre)
        return render(request, 'seach.html', {'search':search,'Genre':Genre})
