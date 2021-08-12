from django.shortcuts import render, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import User, Product, ProductType
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    return render(request, 'hill_bakes/index.html')


def cookies(request):
    cookie = Product.objects.filter(type_id='1')
    context = {
        'cookie': cookie
    }

    return render(request, 'hill_bakes/cookies.html', context)


def cakes(request):
    cake = ProductType.objects.filter(id='5')
    context = {
        'cake': cake
    }
    return render(request, 'hill_bakes/cakes.html', context)


def cake_balls(request):
    cake_ball = Product.objects.filter(type_id='6')
    context = {
        'cake_ball': cake_ball
    }
    return render(request, 'hill_bakes/cake_balls.html', context)


def about(request):
    return render(request, 'hill_bakes/about.html')


def signup(request):
    print('METHOD', request.method)
    if request.method == 'GET':
        return render(request, 'hill_bakes/signup.html')
    elif request.method == 'POST':
        # get data from form
        form = request.POST
        username = form['username']
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']

        # create user. username, email, password order matters
        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('hill_bakes:home_page'))


def login_user(request):
    # user visits page
    if request.method == 'GET':
        return render(request, 'hill_bakes/login.html')
    # user submits form
    elif request.method == 'POST':
        # get form data
        form = request.POST
        username = form['username']
        password = form['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('hill_bakes:home_page'))


def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('hill_bakes:home_page'))
