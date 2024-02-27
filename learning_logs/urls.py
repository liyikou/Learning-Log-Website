from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(route='topics/', view=views.topics, name='topics'),
]

app_name='learning_logs'