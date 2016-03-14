from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return HttpResponse("<h2>HEY!</h2>")

def loginView(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('myapp/login.html', c)

def authHandlerView(request):
    username  = request.POST.get('username', '')
    password  = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/myapp/loggedin')
    else:
        return HttpResponseRedirect('/myapp/invalid')

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/myapp/loggedout')

def loggedoutView(request):
    return HttpResponse("<h2>Logged Out Succesfully</h2>")

@login_required
def securedView(request):
    return HttpResponse("<h2>Secured urL</h2>")

def loggedinView(request):
    return HttpResponse("<h2>Logged in</h2>")

def invalidView(request):
    return HttpResponse("<h2>Invalid Credentials</h2>")

def signupView(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('myapp/signup.html', c)

def signupHandlerView(request):
    username  = request.POST.get('username', '')
    email  = request.POST.get('emali', '')
    password  = request.POST.get('password', '')
    user = User.objects.create_user(username, email , password)
    return HttpResponseRedirect('/myapp/welcome')

def signupLandingView(request):
    return HttpResponse("<h2>New user created</h2><h2><a href='/myapp/secure/'>secure page</a></h2>")



