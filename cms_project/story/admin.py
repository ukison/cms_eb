from django.contrib import admin
from story.models import Story

# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')

admin.site.register(Story, StoryAdmin)
