from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, template_name='learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request=request, template_name="learning_logs/topics.html", context=context)

def topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
    except Topic.DoesNotExist:
        return HttpResponseServerError(content="Topic not found.")
    except Exception as e:
        return HttpResponseServerError(content="Server occurred error.")
    else:
        context = {"topic": topic, "entries": entries}
        return render(request=request, template_name="learning_logs/topic.html", context=context)
    
def add_topic(request):
    if request.method != "POST":
        form = TopicForm()  # 未提交数据，创建新表单
    else:
        form = TopicForm(data=request.POST)  # 用提交的数据初始化Form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse("learning_logs:topics"))
    # GET / POST but form is not valid
    context = {"form": form}
    return render(request=request, template_name="learning_logs/add_topic.html", context=context)

def add_entry(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return HttpResponseServerError("Topic not found.")
    else:
        if request.method != "POST":
            form = EntryForm()
        else:
            form = EntryForm(data=request.POST)
            if form.is_valid():
                new_entry = form.save(commit=False)  # 暂时不保存数据库
                new_entry.topic = topic  # 设置外键字段，关联Topic
                new_entry.save()
                return HttpResponseRedirect(redirect_to=reverse(viewname="learning_logs:topic", args=[topic_id]))  # args存放重定向的url需要的所有实参
        context = {'topic': topic, 'form': form}
        return render(request, 'learning_logs/add_entry.html', context)