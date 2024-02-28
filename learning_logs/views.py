from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse

from .models import Topic
from .forms import TopicForm


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
        return HttpResponseServerError(content=errors)
    else:
        context = {"topic": topic, "entries": entries}
        return render(request, "learning_logs/topic.html", context)
    
def add_topic(request):
    if request.method != "POST":
        form = TopicForm()  # 未提交数据，创建新表单
    else:
        form = TopicForm(request.POST)  # 用提交的数据初始化Form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topics"))
    context = {"form": form}
    return render(request, "learning_logs/add_topic.html", context=context)