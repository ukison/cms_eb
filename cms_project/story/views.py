from django.views.generic import ListView
from story.models import Story

# Create your views here.


class StoryList(ListView):
    model = Story
