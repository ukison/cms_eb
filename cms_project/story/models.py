from django.db import models
from markdown import markdown

# Create your models here.


class Story(models.Model):
    name = models.CharField(max_length=100)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)

    def save(self, *args, **kwargs):
        self.html_content = markdown(self.markdown_content)
        super(Story, self).save(*args, **kwargs)
