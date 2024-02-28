from django.shortcuts import render, HttpResponse
from .models import Topic


def index(request):
    return render(request, template_name='learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request=request, template_name="learning_logs/topics.html", context=context)

def topic(request, topic_id):
    errors = None
    try:
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
    except Topic.DoesNotExist:
        topic = None
    except Exception as e:
        topic = None
        errors = 'There is something error.'
        return HttpResponse({"status": 500, "error": errors})
    else:
        context = {"topic": topic, "entries": entries}
        return render(request, "learning_logs/topic.html", context)