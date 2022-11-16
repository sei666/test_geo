from .city import CityApi, CitiesApi, FindTheNearestApi

def initialize_routes(api):
# ##--------------------------------------------- city -------------------------------------------------------------
    pathCity = "/api/v1/"
    api.add_resource(CityApi, pathCity + '/city', methods=['POST'], endpoint='city_without_arg')
    api.add_resource(CityApi, pathCity + '/city/<cityId>', methods=['GET', 'DELETE'], endpoint='city_with_arg')
    api.add_resource(CitiesApi, pathCity + '/cities', methods=['GET'])
    api.add_resource(FindTheNearestApi, pathCity + '/findTheNearest', methods=['GET'])
# ##-----------------------------------------------------------------------------------------------------------------