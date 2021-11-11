from django.db import models
from django.db.models.fields import related


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Street(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="streets"
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    core_data_added = models.BooleanField()
    entry_complete = models.BooleanField()
    name = models.CharField(max_length=60)
    street = models.OneToOneField(
        Street, on_delete=models.CASCADE, primary_key=True, related_name="eponym"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=50, null=True, blank=True)
    place_of_death = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "People"
