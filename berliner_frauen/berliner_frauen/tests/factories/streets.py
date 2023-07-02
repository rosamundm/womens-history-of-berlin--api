import factory
from streets.models import District, Street


class DistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = District


class StreetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Street
