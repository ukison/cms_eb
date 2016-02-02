from django.views.generic import ListView
from django.views.generic import DetailView
from story.models import Story

# Create your views here.


class StoryList(ListView):
    model = Story


class StoryDetail(DetailView):
    model = Story
    pk_url_kwarg = 'id'
