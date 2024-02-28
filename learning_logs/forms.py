from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # 让Django不要为字段 text 生成标签
