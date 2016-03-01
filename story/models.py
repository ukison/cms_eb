from django.db import models
from markdown import markdown

# Create your models here.


class Story(models.Model):
    name = models.CharField(max_length=100)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.html_content = markdown(self.markdown_content,
                                     extensions=['markdown.extensions.nl2br'])
        super(Story, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/%d/' % self.pk

    class Meta:
        verbose_name_plural = 'stories'
