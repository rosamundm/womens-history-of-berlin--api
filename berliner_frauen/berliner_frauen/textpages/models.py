from django.db import models
from tinymce.models import HTMLField


class TextPage(models.Model):
    title = models.CharField(max_length=50)
    body = HTMLField(null=True, blank=True)
    slug = models.CharField(max_length=50)
