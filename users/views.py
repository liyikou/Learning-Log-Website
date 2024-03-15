from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect

from users.forms import UserCreateForm


class Login(LoginView):
    template_name = 'users/login.html'

   
def logout_view(request):
    logout(request)  # 登出用户，清除用户的session
    return HttpResponseRedirect(redirect_to=reverse('learning_logs:index'))


def register_view(request):
    if request.method != 'POST':
        form = UserCreateForm()
    else:
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)