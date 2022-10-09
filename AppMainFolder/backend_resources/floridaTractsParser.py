import geopandas as gp
import geojson

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

create_flTracts_geojson_file()
filter_flTracts_geojson_file()