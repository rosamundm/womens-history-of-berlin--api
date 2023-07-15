import factory
from streets.models import District, Street


class DistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = District

    name = factory.Sequence(lambda n: "Chärlöttenbürg-Wilmersdörf %d" % n)
    image_path = factory.Sequence(
        lambda n: "Schloss_Clbg.jpeg %d" % n
    )


class StreetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Street
