import json
import pytest
from rest_framework.test import force_authenticate
from tests.factories.streets import DistrictFactory, StreetFactory
from streets.views import DistrictViewSet, StreetViewSet


@pytest.mark.django_db
def test__get_district_list(api_request, api_url, api_user):

    DistrictFactory.create_batch(3)

    view = DistrictViewSet.as_view(actions={"get": "list"})

    request = api_request.get(
        f"{api_url}districts/",
        content_type="application/json"
    )
    
    force_authenticate(request, user=api_user)
    response = view(request)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200

    for i in range(0, 3):
        assert "Chärlöttenbürg-Wilmersdörf" == data[i]["name"]
        assert "Schloss_Clbg.jpeg" == data[i]["image_path"]
        assert lambda n: "chaerloettenbuerg-wilmerssdoerf %d" % n == \
            data[i]["district_slug"]


@pytest.mark.django_db
def test__get_district_instance(api_request, api_url, api_user):

    district = DistrictFactory.create()

    view = DistrictViewSet.as_view(actions={"get": "retrieve"})

    request = api_request.get(
        f"{api_url}districts/",
        content_type="application/json"
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, district_slug=district.district_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200
    assert "Chärlöttenbürg-Wilmersdörf" == data["name"]
    assert "Schloss_Clbg.jpeg" == data["image_path"]
    assert lambda n: "chaerloettenbuerg-wilmerssdoerf %d" % n == \
        data["district_slug"]

