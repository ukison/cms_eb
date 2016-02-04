from django.views.generic import ListView
from django.views.generic import DetailView
from django.db import models
from django.shortcuts import render_to_response
from story.models import Story


# Create your views here.


class StoryList(ListView):
    model = Story


class StoryDetail(DetailView):
    model = Story
    pk_url_kwarg = 'id'


def search(request):
	if 'search' in request.GET:
		q = request.GET['search']
		queryset = Story.objects.filter(models.Q(name__contains=q) | models.Q(markdown_content__contains=q))
		return render_to_response('story/story_list.html', context={'object_list': queryset})