import datetime
import requests
import string
from bs4 import BeautifulSoup


BASE_URL = "https://berlin.kauperts.de/"
STREET_INDEX_URL = BASE_URL + "Strassenverzeichnis/"


for letter in string.ascii_uppercase:
    response = requests.get(STREET_INDEX_URL + letter)
    soup = BeautifulSoup(response.content, "html.parser")
    street_table = soup.find("table", class_="default streets")
    street_links = street_table.find_all("a")

    for link in street_links:
        response = requests.get(BASE_URL + link["href"])
        soup = BeautifulSoup(response.content, "html.parser")
        detail_table = soup.find("table", id="Detailinformationen")

        street = {}
        street["name"] = link.string
        street["district"] = []

        streets_by_district = detail_table.find_all("tr", class_="district")

        streets = []

        for tr in streets_by_district:
            if not tr.a:
                continue
            street["district"].append(tr.a.string)
        streets.append(street)

        streets_named_after_people = []
        mitte_streets_named_after_people = []

        for street in streets:
            if "-" not in street["name"]:
                continue
            streets_named_after_people.append(street)

            for street in streets_named_after_people:
                if "Mitte" not in street["district"]:
                    continue
                mitte_streets_named_after_people.append(street)

        for street in mitte_streets_named_after_people:
            street = (str(street["name"] + "\n"))
            with open("test.txt", "a") as file:
                file.write(street)
