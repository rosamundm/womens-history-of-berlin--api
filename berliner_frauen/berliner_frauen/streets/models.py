from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from .helpers import slugify_umlauts


class District(models.Model):
    name = models.CharField(max_length=50)
    image_path = models.CharField(max_length=50, blank=True, null=True)
    district_slug = models.CharField(max_length=50, blank=True, null=True)

    @property
    def number_of_added_streets(self):
        return self.streets.count()

    @property
    def number_of_completed_streets(self):
        return self.streets.filter(entry_complete=True).count()

    @property
    def number_of_photos_taken(self):
        return self.streets.filter(image_available=True).count()

    def save(self, *args, **kwargs):
        self.district_slug = slugify_umlauts(self.name)
        super(District, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Street(models.Model):
    eponym_core_data_added = models.BooleanField()
    entry_complete = models.BooleanField()
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="streets"
    )
    map_link = models.URLField()
    name = models.CharField(max_length=50)
    street_slug = models.CharField(max_length=50, blank=True, null=True)
    eponym_name = models.CharField(max_length=60)
    eponym_date_of_birth = models.DateField(null=True, blank=True)
    eponym_date_of_death = models.DateField(null=True, blank=True)
    eponym_place_of_birth = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    eponym_place_of_death = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    eponym_description = HTMLField(null=True, blank=True)
    image = models.URLField(max_length=200, null=True, blank=True)
    image_available = models.BooleanField()
    tags = TaggableManager()
    last_edited = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.street_slug = slugify_umlauts(self.name)
        super(Street, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
