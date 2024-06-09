from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, template_name='learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_created')
    context = {"topics": topics}
    return render(request=request, template_name="learning_logs/topics.html", context=context)

@login_required
def topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        if topic.owner != request.user:
            return HttpResponseForbidden()
        entries = topic.entries.order_by('-date_created')
    except Topic.DoesNotExist:
        return HttpResponseServerError(content="Topic not found.")
    except Exception as e:
        ''
        return HttpResponseServerError(content="Server occurred error.")
    else:
        context = {"topic": topic, "entries": entries}
        return render(request=request, template_name="learning_logs/topic.html", context=context)
    
@login_required
def add_topic(request):
    if request.method != "POST":
        form = TopicForm()  # 未提交数据，创建新表单
    else:
        form = TopicForm(data=request.POST)  # 用提交的数据初始化Form
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(redirect_to=reverse("learning_logs:topics"))
    # GET / (POST but form is not valid)
    context = {"form": form}
    return render(request=request, template_name="learning_logs/add_topic.html", context=context)

@login_required
def add_entry(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        # 防止用户在其他用户的主题下创建文章
        if topic.owner != request.user:
            return HttpResponseForbidden()
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

@login_required
def edit_entry(request, entry_id):
    try:
        entry = Entry.objects.get(id=entry_id)
        topic = entry.topic
        if topic.owner != request.user:
            return HttpResponseForbidden()
    except Entry.DoesNotExist:
        return HttpResponseServerError("Entry not found.")
    else:
        if request.method != 'POST':
            # GET请求页面：创建form实例，带值的form
            form = EntryForm(instance=entry)  
        else:
            # 根据表单提交的数据创建form进行表单数据校验
            form = EntryForm(data=request.POST, instance=entry)  # 必须加上instance否则topic字段没有填充，因为form的Meta类定义了fields限制为 'text'，否则页面加载form会多一个下拉菜单选Topic。
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
        context = {'topic': topic, 'entry': entry, 'form': form}
        return render(request, 'learning_logs/edit_entry.html', context)