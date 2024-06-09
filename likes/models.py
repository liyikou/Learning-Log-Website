from django.db import models

from users.models import User
from learning_logs.models import Entry


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='likes', on_delete=models.CASCADE)