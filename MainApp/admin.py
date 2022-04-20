from django.contrib import admin

# Register your models here.
from .models import Topic, Entry #add it here


admin.site.register(Topic)
admin.site.register(Entry)

