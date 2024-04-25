import numpy as np

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm, LoginForm, SelectAlgorithm

from .scripts.algorithms import DE, CGA
from .scripts.functions import my_fun

# Home page
def index(request):
    return render(request, "optimization/index.html")

# signup page
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "optimization/signup.html", {"form": form})

# login page
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("user_home")
    else:
        form = LoginForm()
    return render(request, "optimization/login.html", {"form": form})

# logout page
def user_logout(request):
    logout(request)
    return redirect("login")

# Execution of Classic Generic Algorithm
def view_cga(request):
    num_iter = 1000
    n_p = 10
    bounds = (-65536.0, 65536.0)
    cga = CGA(n_p, bounds, my_fun)
    cga.run(num_iter, verbose=True)

    context = {
        'num_iter': num_iter,
        'n_p': n_p,
        'bounds': bounds,
        'cga': cga,
    }

    return render(request, "optimization/cga.html", context = context)

# Execution of Differential Equation
def view_de(request):
    num_iter = 1000
    np_ = 10
    cr = 0.9
    f = 0.8
    bounds=(
        -np.ones(10)*0.1,
        np.ones(10)*0.1
    )
    de = DE(my_fun, bounds, np_, cr, f)
    de.run(num_iter, verbose=True)

    context = {
        'num_iter': num_iter,
        'n_p': np_,
        'bounds': bounds,
        'cr': cr,
        'f': f,
        'cga': de,
    }

    return render(request, "optimization/de.html", context = context)