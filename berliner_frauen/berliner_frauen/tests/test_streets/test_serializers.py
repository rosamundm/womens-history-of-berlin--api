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
        assert lambda n: "Chärlöttenbürg-Wilmersdörf %d" % n \
              == data[i]["name"]
        assert lambda n: "chaerloettenbuerg-wilmerssdoerf %d" % n == \
            data[i]["district_slug"]
        assert "Schloss_Clbg.jpeg" == data[i]["image_path"]


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
    assert lambda n: "Chärlöttenbürg-Wilmersdörf %d" % n == data["name"]
    assert lambda n: "chaerloettenbuerg-wilmerssdoerf %d" % n == \
        data["district_slug"]
    assert "Schloss_Clbg.jpeg" == data["image_path"]
    

@pytest.mark.django_db
def test__get_street_list(api_request, api_url, api_user):

    StreetFactory.create_batch(3)

    view = StreetViewSet.as_view(actions={"get": "list"})

    request = api_request.get(
        f"{api_url}streets/",
        content_type="application/json"
    )
    
    force_authenticate(request, user=api_user)
    response = view(request)
    response = response.render()
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200
    for i in range(0, 3):
        assert lambda n: "Rösä-Lüxembürg-Sträße %d" % n \
              == data[i]["name"]
        assert lambda n: "roesae-luexembuerg-straesse %d" % n == \
            data[i]["street_slug"]
        assert "05.03.1871" == data[i]["eponym_date_of_birth"]
        assert "15.01.1919" == data[i]["eponym_date_of_death"]


@pytest.mark.django_db
def test__get_street_instance(api_request, api_url, api_user):

    street = StreetFactory.create()

    view = StreetViewSet.as_view(actions={"get": "retrieve"})

    request = api_request.get(
        f"{api_url}streets/",
        content_type="application/json"
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, street_slug=street.street_slug)
    response = response.render()
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200
    assert lambda n: "Rösä-Lüxembürg-Sträße %d" % n == data["name"]
    assert lambda n: "roesae-luexembuerg-straesse %d" % n == data["street_slug"]
    assert "05.03.1871" == data["eponym_date_of_birth"]
    assert "15.01.1919" == data["eponym_date_of_death"]