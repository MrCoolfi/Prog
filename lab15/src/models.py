from dataclasses import dataclass

@dataclass
class Country:
    id: int
    name: str

@dataclass
class BuildingType:
    id: int
    type_name: str

@dataclass
class Building:
    id: int
    name: str
    city: str
    country_id: int
    height: float
    year: int
    type_id: int