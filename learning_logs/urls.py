from django.urls import path, re_path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='topics/', view=views.topics, name='topics'),
    re_path(route=r'^topic/(?P<topic_id>\d+)/$', view=views.topic, name='topic'),
    path(route='add_topic/', view=views.add_topic, name='add_topic'),
]

app_name='learning_logs'