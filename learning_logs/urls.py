from django.urls import path, re_path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='topics/', view=views.topics, name='topics'),
    re_path(route=r'^topic/(?P<topic_id>\d+)/$', view=views.topic, name='topic'),
    path(route='add_topic/', view=views.add_topic, name='add_topic'),
    re_path(route=r'^add_entry/(?P<topic_id>\d+)/$', view=views.add_entry, name='add_entry'),
    re_path(route=r'^edit_entry/(?P<entry_id>\d+)/$', view=views.edit_entry, name="edit_entry"),
]

app_name='learning_logs'