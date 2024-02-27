from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register Models
admin.site.register(Topic)
admin.site.register(Entry)