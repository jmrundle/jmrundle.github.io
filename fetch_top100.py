#!/usr/bin/env python3

import sys
import os.path
import json
import requests
from typing import List
from bs4 import BeautifulSoup
from models import Course
from geocode import geocode


LIST_URL = "https://golf.com/travel/courses/best-public-golf-courses-top-100-you-can-play-2020-21/"
DEFAULT_FILE = "data.json"


def parse_resp(html) -> List[Course]:
    soup = BeautifulSoup(html, 'html.parser')
    course_divs = soup.select("div.top100-featured-item__inner")
    return [ parse_course(c) for c in course_divs ]


def parse_course(course_div) -> Course:
    details = course_div.select_one("div.top100-featured-item__ranking-block")
    title = details.select_one("h3.top100-featured-item__title").get_text().split()
    location = details.select_one("div.top100-featured-item__location > span:nth-of-type(2)").get_text().split(', ')
    specs = details.select("div.top100-featured-item__specs div.top100-featured-item__spec-text")

    rank = int(title[0][:-1])  # strip "."
    name = title[1]
    city = location[0]
    state = location[1] if len(location) > 1 else "" 
    img_url = course_div.select_one(".top100-featured-item__image-wrapper > img")['src']
    architect = specs[0].get_text()
    year_built = int(specs[1].get_text()) if specs[1].get_text() else 0

    descr = ""
    for p in course_div.select("div.top100-featured-item__infos > p"):
        descr += p.get_text().strip()

    return Course(rank, name, city, state, img_url, architect, year_built, descr)


def geocode_courses(courses):
    for c in courses:
        c.detailed_location = geocode(c)


def save_courses(courses, out_stream):
    data = [ c.to_dict() for c in courses ]
    print(json.dumps(data, indent=2), file=out_stream)


def main():
    out_file   = DEFAULT_FILE
    do_geocode = False

    for arg in sys.argv[1:]:
        if arg == '-g':
            do_geocode = True
        else:
            out_file = arg

    if os.path.exists(out_file):
        print("Output file already exists", file=sys.stderr)
        sys.exit(1)

    resp = requests.get(LIST_URL)
    courses = parse_resp(resp.text)

    if do_geocode:
        geocode_courses(courses)

    with open(out_file, 'w+') as out_stream:
        save_courses(courses, out_stream) 


if __name__ == '__main__':
    main()

