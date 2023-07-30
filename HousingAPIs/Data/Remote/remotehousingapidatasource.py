import overpy
import requests

class RemoteHousingAPIDataSource:

    api = overpy.Overpass()
    """
    :param
    lat represents the lat of the center of the circle we are searching
    long represents the long of the center of the circle we are searching
    
    The return values should be a list of the houses in a 50 meter radius
    """
    def getHouseAddresses50Meters(self, lat, long):
        jsonResponse = requests.get(f"https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/{long},{lat}.json?radius=50&limit=50&dedupe&layers=housenum_label&access_token=pk.eyJ1IjoiZGFuaWVsemhhbmcxMjkiLCJhIjoiY2xrbGo0dW51MGI2eTNmcWVoYWRnZHlmeSJ9.BINJdFPV-t-SXnzr7AjuxA")
        return jsonResponse


