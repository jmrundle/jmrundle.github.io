#!/usr/bin/env python3

import os
import sys
from models import Course, Location
from typing import List
import requests


def geocode_courses(courses: List[Course]):
    with requests.Session() as s:
        for c in courses:
            c.detailed_location = geocode_course(c, s)


def geocode_course(course: Course, session=None) -> Location:
    GOOGLE_GEOCODE_API = "https://maps.googleapis.com/maps/api/geocode/json"
    GOOGLE_GEOCODE_API_KEY = os.environ['GOOGLE_GEOCODE_API_KEY']

    params = {
        "address": f"{course.name}, {course.city}, {course.state}",
        "key": GOOGLE_GEOCODE_API_KEY
    }

    if session is not None:
        resp = session.get(GOOGLE_GEOCODE_API, params=params)
    else:
        resp = requests.get(GOOGLE_GEOCODE_API, params=params)

    data = resp.json()

    if data['status'] != 'OK':
        raise ValueError(data['error_message'])

    addr = data['results'][0]['formatted_address']

    loc = data['results'][0]['geometry']['location']
    lat, lng = loc['lat'], loc['lng']

    return Location(addr, lat, lng)


if __name__ == "__main__":
    test_course = Course(99, "Black", "Espanola", "NM", "https://URL.jpg", "Baxter Spann", 2003, "Test Description")
    location = geocode_course(test_course)
    print(location.to_dict())

