#!/usr/bin/env python3

import os
import sys
from scripts.models import Course, Location
import requests


GOOGLE_GEOCODE_API = "https://maps.googleapis.com/maps/api/geocode/json"
GOOGLE_GEOCODE_API_KEY = os.environ['GOOGLE_GEOCODE_API_KEY']


def geocode(course: Course) -> Location:
    params = {
        "address": f"{course.name}, {course.city}, {course.state}",
        "key": GOOGLE_GEOCODE_API_KEY
    }

    resp = requests.get(GOOGLE_GEOCODE_API, params=params)
    data = resp.json()

    if data['status'] != 'OK':
        print(data['message'], file=sys.stderr)
        return None

    addr = data['results'][0]['formatted_address']

    loc = data['results'][0]['geometry']['location']
    lat, lng = loc['lat'], loc['lng']

    return Location(addr, lat, lng)


if __name__ == "__main__":
    test_course = Course(99, "Black", "Espanola", "NM", "https://URL.jpg", "Baxter Spann", 2003, "Test Description")
    location = geocode(test_course)
    print(location.to_dict())

