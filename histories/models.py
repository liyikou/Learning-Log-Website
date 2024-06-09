from django.db import models

from users.models import User
from learning_logs.models import Entry

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='histories', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)