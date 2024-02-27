from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, template_name='learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request=request, template_name="learning_logs/topics.html", context=context)