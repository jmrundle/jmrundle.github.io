from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    address: str
    lat: float
    lng: float

    def to_dict(self):
        return {
            "address": self.address,
            "lat": self.lat,
            "lng": self.lng
        }


@dataclass
class Course:
    rank: int
    name: str
    city: str
    state: str
    img_url: str
    architect: str
    year_built: int
    description: str
    detailed_location: Optional[Location] = None

    def to_dict(self):
        return {
            "rank": self.rank,
            "course_name": self.name,
            "city": self.city,
            "state": self.state,
            "img_url": self.img_url,
            "architect": self.architect,
            "year_built": self.year_built,
            "description": self.description,
            "detailed_location": {} if self.detailed_location is None else self.detailed_location.to_dict()
        }

