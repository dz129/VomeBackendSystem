import requests
import json
import sys
from model.latlongresponse import LatLongResponse
import googlemaps


class RemoteHousingAPIDataSource:
    """
    :param
    lat represents the lat of the center of the circle we are searching
    long represents the long of the center of the circle we are searching
    
    The return values should be a list of the houses in a 50 meter radius
    probably want to map these values into a class
    """
    googleMapsClient = googlemaps.Client(key="AIzaSyBFnsA9F8RSumIDh6gbTUQGUxeP05CaHmI")

    def getHouseAddresses50Meters(self, lat, long):
        jsonResponse = requests.get(
            f"https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/{long},{lat}.json?radius=50&limit=50&dedupe&layers=housenum_label&access_token=pk.eyJ1IjoiZGFuaWVsemhhbmcxMjkiLCJhIjoiY2xrbGo0dW51MGI2eTNmcWVoYWRnZHlmeSJ9.BINJdFPV-t-SXnzr7AjuxA").json()
        houses = jsonResponse["features"]
        # i want this HousesList to have a list fo house objects with lat and long, we can add the addresses later when we do the reverse geocoding
        HousesList = []
        for home in houses:
            geometry = home["geometry"]
            coordinates = geometry["coordinates"]
            houseClass = LatLongResponse(coordinates[1], coordinates[0])
            HousesList.append(houseClass)
        return HousesList

    def getReverseGeoCodeAddress(self, lat, long):
        #alternatively use this, googles api seems way too expensive
        #https://api.mapbox.com/geocoding/v5/{endpoint}/{longitude},{latitude}.json
        addressResult = self.googleMapsClient.reverse_geocode((lat, long))
        return addressResult


