import uuid
from django.db import models
from tinymce.models import HTMLField


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    published = models.DateField(blank=False, null=False, auto_now=True)
    body = HTMLField(null=True, blank=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    ready_to_publish = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = str(uuid.uuid4())
        super(BlogPost, self).save(*args, **kwargs)
