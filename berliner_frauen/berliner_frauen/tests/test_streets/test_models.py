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
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    assert street.street_slug == "roesae-luexembuerg-straesse"


@pytest.mark.django_db
def test__district_number_of_added_streets():

    district = DistrictFactory.create(name="Mitte")

    StreetFactory.create_batch(
        3,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=False,
        image_available=False,
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    assert district.number_of_added_streets == 3


@pytest.mark.django_db
def test__district_number_of_completed_streets():

    district = DistrictFactory.create(name="Mitte")

    StreetFactory.create_batch(
        2,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=True,
        image_available=False,
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    StreetFactory.create_batch(
        2,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=False,
        image_available=False,
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    assert district.number_of_completed_streets == 2


@pytest.mark.django_db
def test__district_number_of_photos_taken():

    district = DistrictFactory.create(name="Mitte")

    StreetFactory.create_batch(
        10,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=True,
        image_available=True,
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    StreetFactory.create_batch(
        1,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=True,
        image_available=False,
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    assert district.number_of_photos_taken == 10
