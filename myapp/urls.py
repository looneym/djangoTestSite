from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^signup/$', views.signupView, name='signupView'),
    url(r'^signupHandler/$', views.signupHandlerView, name='signupHandlerView'),
    url(r'^welcome/$', views.signupLandingView, name='signupLandingView'),

    url(r'^login/', views.loginView, name='loginView'),
    url(r'^auth/$', views.authHandlerView, name='authHandlerView'),

    url(r'^logout/$', views.logoutView, name='logoutView'),
    url(r'^loggedout/$', views.loggedoutView, name='loggedoutView'),

    url(r'^loggedin/$', views.loggedinView, name='loggedinView'),
    url(r'^invalid/$', views.invalidView, name='invalidView'),

    url(r'^secure/$', views.securedView, name='securedView'),

]



