from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect


class Login(LoginView):
    template_name = 'users/login.html'
    
def logout_view(request):
    logout(request)  # 登出用户，清除用户的session
    return HttpResponseRedirect(redirect_to=reverse('learning_logs:index'))

