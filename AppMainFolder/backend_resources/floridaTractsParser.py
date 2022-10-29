import geopandas as gp
import geojson
import json
import requests

# Creates a json file with the annual income data for each census tract in Orange County
def create_income_json_file():
    api_key = '94f15b818568d82a42e2c1120de6af89ccd4d6b8'
    api_url = 'https://api.census.gov/data/2020/acs/acs5/subject?get=NAME,S1902_C03_001E&for=tract:*&in=county:095&in=state:12&key=' + api_key
    income_json_data = requests.get(api_url).json()
    with open("assets\\annual_income_orange_county_tracts.json", "w") as file:
        json.dump(income_json_data, file)
        print("Annual income json file created!")

# Creates a geojson file from the TIGER/Line Shapefile downloaded from the US Census Bureau
# https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2020.html#list-tab-BV7EUGCSTGIS1AB989
def create_flTracts_geojson_file():
    florida_tracts_zip_file = "2020_florida_tract.zip"

    print("Creating a geojson file based on the Florida tracts TIGER/Line Shapefile...")
    florida_tracts_coordinates = gp.read_file(florida_tracts_zip_file)
    florida_tracts_coordinates = florida_tracts_coordinates.to_crs(4326)
    florida_tracts_coordinates.to_file("assets\\florida_tracts.geojson", driver="GeoJSON")

# filter the florida_tracts.geojson file to only include the tracts that are in Orange County
def filter_flTracts_geojson_file():
    orange_county_code = "095"

    print("Filtering the geojson file to only include the tracts that are in Orange County...")
    with open("assets\\florida_tracts.geojson") as file:
        data = geojson.load(file)
        new_data_features = []
        for feature in data.features:
            if feature.properties["COUNTYFP"] == orange_county_code:
                new_data_features.append(feature)
        data.features = new_data_features
        with open("assets\\orlando_tracts.geojson", "w") as file:
            geojson.dump(data, file)

# create_flTracts_geojson_file()
# filter_flTracts_geojson_file()
create_income_json_file()