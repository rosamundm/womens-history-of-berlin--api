import pytest
from tests.factories.streets import DistrictFactory, StreetFactory


def test__admin_view(admin_client):
    response = admin_client.get("/admin/")
    assert response.status_code == 200


def test__district_admin_list_view(admin_client):
    response = admin_client.get("/admin/streets/district/")
    assert response.status_code == 200


def test__district_admin_object_view(admin_client):

    district = DistrictFactory.create(name="Mitte")

    response = admin_client.get(f"/admin/streets/district/{district.id}/change/")

    assert response.status_code == 200


def test__street_admin_list_view(admin_client):
    response = admin_client.get("/admin/streets/street/")
    assert response.status_code == 200


def test__street_admin_object_view(admin_client):

    district = DistrictFactory.create(name="Mitte")

    street = StreetFactory.create(
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

    response = admin_client.get(f"/admin/streets/street/{street.id}/change/")

    assert response.status_code == 200


def test__district_admin_entries_completed(admin_client):

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

    response = admin_client.get("/admin/streets/district/")

    assert '<td class="field-entries_completed">0.0%</td>' in str(response.content)


def test__district_entries_with_photos_taken(admin_client):

    district = DistrictFactory.create(name="Mitte")

    StreetFactory.create_batch(
        3,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=False,
        image_available=True,
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

    response = admin_client.get("/admin/streets/district/")

    assert '<td class="field-entries_with_photos_taken">60.0%</td>' in str(
        response.content
    )


def test__district_complete_from_available_photos(admin_client):

    district = DistrictFactory.create(name="Mitte")

    StreetFactory.create_batch(
        3,
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
        5,
        district=district,
        name="Rösä-Lüxembürg-Sträße",
        eponym_name="Rosa Luxemburg",
        eponym_core_data_added=False,
        entry_complete=False,
        image_available=True,
        tags=[
            "politics",
        ],
        map_link="https://www.openstreetmap.org/way/109819106",
    )

    response = admin_client.get("/admin/streets/district/")

    assert '<td class="field-complete_from_available_photos">37.5%</td>' in str(
        response.content
    )
