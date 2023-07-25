import overpy

class RemoteHousingAPIDataSource:

    api = overpy.Overpass()
    """
    :param
    lat represents the lat of the center of the circle we are searching
    long represents the long of the center of the circle we are searching
    radius represents the radius of the circle we are searching
    
    The return values should be a list of 
    """
    def getCoordinatesForHomesInGivenRadius(self, lat, long, radius):
        overpass_query = f"""
                [out:json];
                (
                    node["building"="residential"](around:{radius},{lat},{long});
                    way["building"="residential"](around:{radius},{lat},{long});
                    relation["building"="residential"](around:{radius},{lat},{long});
                );
                out;
            """
        jsonResult = self.api.query(overpass_query)

