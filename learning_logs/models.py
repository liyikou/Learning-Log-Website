from django.db import models

from users.models import User


# Topic
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联User表，设置级联删除
    
    def __str__(self) -> str:
        return self.text
    
# Entry
class Entry(models.Model):
    ACCESS_PERMISSION_CHOICES = [
        ('public', 'Public'),
        ('authenticated', 'Authenticated'),
        ('vip', 'VIP'),
    ]
    topic = models.ForeignKey(Topic, related_name='entries', on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    access_permission = models.CharField(max_length=32, choices=ACCESS_PERMISSION_CHOICES, default='public')
    
    # additional information
    class Meta:
        verbose_name_plural = 'entries'  # 复数形式，否则会展示为 'Entrys'
    
    def __str__(self) -> str:
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text