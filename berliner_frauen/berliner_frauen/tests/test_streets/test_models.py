import pytest
from tests.factories.streets import DistrictFactory


@pytest.mark.django_db
def test__district_slug_generated():

    district = DistrictFactory.create(name="Chärlöttenbürg-Wilmerßdörf")

    assert district.district_slug == "chaerloettenbuerg-wilmerssdoerf"
