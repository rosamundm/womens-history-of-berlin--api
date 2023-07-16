import datetime
import factory
from streets.models import District, Street


class DistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = District

    name = factory.Sequence(lambda n: "Chärlöttenbürg-Wilmersdörf %d" % n)
    image_path = "Schloss_Clbg.jpeg"


class StreetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Street

    name = factory.Sequence(lambda n: "Rösä-Lüxembürg-Sträße %d" % n)
    district = factory.SubFactory(DistrictFactory)
    map_link = "https://www.openstreetmap.org/way/109819106"
    eponym_name = "Rosa Luxemburg"
    eponym_date_of_birth = datetime.date(1871, 3, 5)
    eponym_date_of_death = datetime.date(1919, 1, 15)
    eponym_place_of_birth = "Zamość, Poland"
    eponym_place_of_death = "Berlin, Germany"
    eponym_description = "<p>Ipsum suspendisse ultrices gravida</p>"
    image = "luxemburg_berlin.jpeg"
    image_available = True
    eponym_core_data_added = True
    entry_complete = True
    tags = ["politics", ],
