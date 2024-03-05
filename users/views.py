from django.shortcuts import render
from django.contrib.auth.views import LoginView


class Login(LoginView):
    template_name = 'users/login.html'

