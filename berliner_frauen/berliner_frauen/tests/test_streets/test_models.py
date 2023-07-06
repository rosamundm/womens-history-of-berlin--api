import pytest
from tests.factories.streets import DistrictFactory, StreetFactory


@pytest.mark.django_db
def test__district_slug_generated():

    district = DistrictFactory.create(name="Chärlöttenbürg-Wilmerßdörf")

    assert district.district_slug == "chaerloettenbuerg-wilmerssdoerf"


@pytest.mark.django_db
def test__street_slug_generated():
    
    street = StreetFactory.create(
        district=DistrictFactory.create(name="Mitte"),
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=False,
        image_available=False,
        tags=["politics", ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    assert street.street_slug == "roesae-luexembuerg-straesse"
