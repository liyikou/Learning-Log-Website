import datetime
from enum import auto
from django.db import models

# Topic
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
    
# Entry
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # additional information
    class Meta:
        verbose_name_plural = 'entries'  # 复数形式，否则会展示为 'Entrys'
    
    def __str__(self) -> str:
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text