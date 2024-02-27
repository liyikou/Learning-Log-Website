import datetime
from enum import auto
from django.db import models

# Topic
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text