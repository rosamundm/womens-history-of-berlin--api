import json
import pytest
from rest_framework.test import force_authenticate
from tests.factories.streets import DistrictFactory, StreetFactory, TagFactory
from streets.views import DistrictViewSet, StreetViewSet, TagViewSet


@pytest.mark.django_db
def test__get_district_list(api_request, api_url, api_user):

    DistrictFactory.create_batch(3)

    view = DistrictViewSet.as_view(actions={"get": "list"})

    request = api_request.get(f"{api_url}districts/")
    
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

    request = api_request.get(f"{api_url}districts/")
    
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

    streets = StreetFactory.create_batch(3)

    view = StreetViewSet.as_view(actions={"get": "list"})

    request = api_request.get(f"{api_url}streets/")

    force_authenticate(request, user=api_user)
    response = view(request)
    response = response.render()
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200
    for i in range(0, 3):
        for street in streets:
            assert lambda n: "Rösä-Lüxembürg-Sträße %d" % n \
                == data[i]["name"]
            assert lambda n: "roesae-luexembuerg-straesse %d" % n == \
                data[i]["street_slug"]
            assert "https://www.openstreetmap.org/way/109819106" == \
                data[i]["map_link"]
            assert "Rosa Luxemburg" == data[i]["eponym_name"]
            assert "05.03.1871" == data[i]["eponym_date_of_birth"]
            assert "15.01.1919" == data[i]["eponym_date_of_death"]
            assert "Zamość, Poland" == data[i]["eponym_place_of_birth"]
            assert "Berlin, Germany" == data[i]["eponym_place_of_death"]
            assert "<p>Ipsum suspendisse ultrices gravida</p>" == \
                data[i]["eponym_description"]
            assert "luxemburg_berlin.jpeg" == data[i]["image"]
            # assert ["politics"] == data[i]["tags"]


@pytest.mark.django_db
def test__get_street_instance(api_request, api_url, api_user):

    street = StreetFactory.create()

    view = StreetViewSet.as_view(actions={"get": "retrieve"})

    request = api_request.get(f"{api_url}streets/")
    
    force_authenticate(request, user=api_user)
    response = view(request, street_slug=street.street_slug)
    response = response.render()
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200
    assert lambda n: "Rösä-Lüxembürg-Sträße %d" % n == data["name"]
    assert lambda n: "roesae-luexembuerg-straesse %d" % n == \
        data["street_slug"]
    assert "https://www.openstreetmap.org/way/109819106" == data["map_link"]
    assert "Rosa Luxemburg" == data["eponym_name"]
    assert "05.03.1871" == data["eponym_date_of_birth"]
    assert "15.01.1919" == data["eponym_date_of_death"]
    assert "Zamość, Poland" == data["eponym_place_of_birth"]
    assert "Berlin, Germany" == data["eponym_place_of_death"]
    assert "<p>Ipsum suspendisse ultrices gravida</p>" == \
        data["eponym_description"]
    assert "luxemburg_berlin.jpeg" == data["image"]
    # assert ["politics"] == data["tags"]


@pytest.mark.django_db
def test__district_is_read_only__post(api_request, api_url, api_user):
    
    district = DistrictFactory.create()

    view = DistrictViewSet.as_view(actions={"post": "create"})

    request = api_request.post(
        f"{api_url}districts/",
        content_type="application/json",
        data=json.dumps({"name": district.name})
    )
    
    force_authenticate(request, user=api_user)
    response = view(request)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "POST operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__district_is_read_only__put(api_request, api_url, api_user):
    
    district = DistrictFactory.create()

    view = DistrictViewSet.as_view(actions={"put": "update"})

    request = api_request.put(
        f"{api_url}districts/",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Mitte",
                "image_path": "picture.jpeg"
            }
        )
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, district_slug=district.district_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "PUT operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__district_is_read_only__patch(api_request, api_url, api_user):
    
    district = DistrictFactory.create()

    view = DistrictViewSet.as_view(actions={"patch": "partial_update"})

    request = api_request.patch(
        f"{api_url}districts/",
        content_type="application/json",
        data=json.dumps({"image_path": "picture.jpeg"})
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, district_slug=district.district_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "PATCH operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__district_is_read_only__delete(api_request, api_url, api_user):
    
    district = DistrictFactory.create()

    view = DistrictViewSet.as_view(actions={"delete": "destroy"})

    request = api_request.delete(
        f"{api_url}districts/",
        content_type="application/json"
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, district_slug=district.district_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "DELETE operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__street_is_read_only__post(api_request, api_url, api_user):

    street = StreetFactory.create()

    view = StreetViewSet.as_view(actions={"post": "create"})

    request = api_request.post(
        f"{api_url}districts/",
        content_type="application/json",
        data=json.dumps(
            {
                "name": street.name,
                "district": street.district_id,
                "map_link": street.map_link,
                "eponym_name": street.eponym_name,
                "eponym_date_of_birth": str(street.eponym_date_of_birth),
                "eponym_date_of_death": str(street.eponym_date_of_death),
                "eponym_place_of_birth": street.eponym_place_of_birth,
                "eponym_place_of_death": street.eponym_place_of_death,
                "image": street.image,
                "image_available": street.image_available,
                "eponym_core_data_added": street.eponym_core_data_added,
                "entry_complete": street.entry_complete,
                "tags": street.tags
            }
        )
    )
    
    force_authenticate(request, user=api_user)
    response = view(request)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "POST operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__street_is_read_only__put(api_request, api_url, api_user):

    street = StreetFactory.create()

    view = StreetViewSet.as_view(actions={"put": "update"})

    request = api_request.put(
        f"{api_url}streets/",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Neuer-Name-Straße",
                "image_path": "picture.jpeg"
            }
        )
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, street_slug=street.street_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "PUT operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__street_is_read_only__patch(api_request, api_url, api_user):

    street = StreetFactory.create()

    view = StreetViewSet.as_view(actions={"patch": "partial_update"})

    request = api_request.patch(
        f"{api_url}streets/",
        content_type="application/json",
        data=json.dumps({"name": "Neuer-Name-Straße"})
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, street_slug=street.street_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "PATCH operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__street_is_read_only__delete(api_request, api_url, api_user):

    street = StreetFactory.create()

    view = StreetViewSet.as_view(actions={"delete": "destroy"})

    request = api_request.delete(
        f"{api_url}streets/",
        content_type="application/json"
    )
    
    force_authenticate(request, user=api_user)
    response = view(request, street_slug=street.street_slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 403
    assert "DELETE operation not possible via API" == data["message"]


@pytest.mark.django_db
def test__get_tag_list(api_request, api_url, api_user):

    TagFactory.create_batch(2)

    view = TagViewSet.as_view(actions={"get": "list"})

    request = api_request.get(f"{api_url}tags/")

    force_authenticate(request, user=api_user)
    response = view(request)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200

    assert "my tag 0" == data[0]["name"]
    assert "my-tag-0" == data[0]["slug"]
    assert "my tag 1" == data[1]["name"]
    assert "my-tag-1" == data[1]["slug"]


@pytest.mark.django_db
def test__get_tag_instance(api_request, api_url, api_user):

    tag = TagFactory.create(name="a tag")

    view = TagViewSet.as_view(actions={"get": "retrieve"})

    request = api_request.get(f"{api_url}tags/")

    force_authenticate(request, user=api_user)
    response = view(request, slug=tag.slug)
    data = json.dumps(response.data)
    data = json.loads(data)

    assert response.status_code == 200
    assert "a tag" == data["name"]
    assert "a-tag" == data["slug"]
