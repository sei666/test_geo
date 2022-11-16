import json
from flask import Response, request, jsonify
from geopy.geocoders import Nominatim

from models.city import City
from flask_restful import Resource
import os

geolocator = Nominatim(user_agent="Tester")


##---------------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------- City Api ------------------------------------------------------------


class CityApi(Resource):
    def get(self, cityId):
        city = City.objects.get(id = cityId)
        cityJson = json.loads(city.to_json())
        return jsonify(cityJson)

    def post(self):
        body = request.get_json()
        cityName = body.get('cityName')
        location = geolocator.geocode(cityName,language="en")
        city = City(city = str(location.address), pointLocation = (location.latitude, location.longitude))
        city.save()
        cityJson = json.loads(city.to_json())
        return jsonify(cityJson)

    def delete(self, cityId):
        city = City.objects.get(id = cityId)
        city.delete()
        return {"deleted": cityId}, 200


##---------------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------- Cities Api ------------------------------------------------------------

class CitiesApi(Resource):
    def get(self):
        cities = City.objects()
        citiesJson = json.loads(cities.to_json())
        return jsonify(citiesJson)
##---------------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------- Find The Nearest Api ------------------------------------------------------------

class FindTheNearestApi(Resource):
    def get(self):
        args = request.args
        latitude = args['latitude']
        longitude = args["longitude"]
        cities = City.objects(pointLocation__near=[float(latitude), float(longitude)])
        citiesJson = json.loads(cities.to_json())[:2]
        return jsonify(citiesJson)
