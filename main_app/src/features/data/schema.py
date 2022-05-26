from enum import Enum
from typing import Union

from pydantic import BaseModel


#
class CountriesEnum(str, Enum):
    POLAND = 'PL'


class KeysEnum(str, Enum):
    AMENITY = "amenity"
    AEROWAY = "aeroway"
    BARRIER = "barrier"
    BOUNDARY = "boundary"
    WATERWAY = "waterway"
    TOURISM = "tourism"
    BUILDING = "building"


class AmenityEnum(str, Enum):
    ZIP_LINE = "zip_line"
    RESTAURANT = "restaurant"
    BAR = "bar"
    AERODROME = "aerodrome"
    CAFE = "cafe"
    BIERGARTEN = "biergarten"
    FOOD_COURT = "food_court"
    ICE_CREAM = "ice_cream"
    PUB = "pub"
    BICYCLE_PARKING = "bicycle_parking"
    BICYCLE_RENTAL = "bicycle_rental"
    BOAT_RENTAL = "boat_rental"
    BUS_STATION = "bus_station"
    CAR_RENTAL = "car_rental"
    CHARGING_STATION = "charging_station"
    FUEL = "fuel"
    PARKING = "parking"
    TAXI = "taxi"
    ATM = "atm"
    BANK = "bank"
    BUREAU_DE_CHANGE = "bureau_de_change"
    HOSPITAL = "hospital"
    PHARMACY = "pharmacy"
    ARTS_CENTRE = "arts_centre"
    BROTHEL = "brothel"
    CASINO = "casino"
    FOUNTAIN = "fountain"
    GAMBLING = "gambling"
    NIGHTCLUB = "nightclub"
    PLANETARIUM = "planetarium"
    THEATRE = "theatre"
    POST_BOX = "post_box"
    POST_OFFICE = "post_office"
    TOWNHALL = "townhall"
    BBQ = "bbq"
    BENCH = "bench"
    DRINKING_WATER = "drinking_water"
    SHELTER = "shelter"
    TOILETS = "toilets"
    WASTE_BASKET = "waste_basket"
    DIVE_CENTRE = "dive_centre"
    GRAVE_YARD = "grave_yard"
    MARKETPLACE = "marketplace"
    MONASTERY = "monastery"
    PHOTO_BOOTH = "photo_booth"
    PLACE_OF_WORSHIP = "place_of_worship"
    VENDING_MACHINE = "vending_machine"
    CITY_WALL = "city_wall"
    NATIONAL_PARK = "national_park"
    WATERFALL = "waterfall"
    ZOO = "zoo"
    KIOSK = "kiosk"
    WILDERNESS_HUT = "wilderness_hut"
    VIEWPOINT = "viewpoint"
    THEME_PARK = "theme_park"
    CATHEDRAL = "cathedral"
    PICNIC_SITE = "picnic_site"
    CHAPEL = "chapel"
    MUSEUM = "museum"
    CHURCH = "church"
    MOTEL = "motel"
    HOTEL = "hotel"
    INFORMATION = "information"
    HOSTEL = "hostel"
    GUEST_HOUSE = "guest_house"
    GALLERY = "gallery"
    CHALET = "chalet"
    CARAVAN_SITE = "caravan_site"
    CAMP_SITE = "camp_site"
    CAMP_PITCH = "camp_pitch"
    ATTRACTION = "attraction"
    ARTWORK = "artwork"
    AQUARIUM = "aquarium"
    APARTMENT = "apartment"
    ALPINE_HUT = "alpine_hut"
    SUPERMARKET = "supermarket"

class OSMQuery(BaseModel):
    country: str
    admin_level: int
    key: KeysEnum
    value: Union[AmenityEnum]
