import json
import sys, os
from random import randint
from pydap.client import open_url
from shapely.geometry import Point, Polygon, shape, box

url = 'https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/fcast/tavg1_2d_flx_Nx/tavg1_2d_flx_Nx.20180601_06'

dataset = open_url(url)

boundary_filepath = os.path.join(os.path.dirname(__file__), 'boundary.json')

with open(boundary_filepath) as f:
    boundary = json.load(f)

polygon = shape(boundary['geometry'])

lats = dataset['lat'][:]
lons = dataset['lon'][:]

geojson = {
    'type': 'FeatureCollection',
    'features': []
}

for i, lat in enumerate(lats):
    for j, lon in enumerate(lons):
        point = Point(lon, lat)
        in_boundary = polygon.contains(point)
        if in_boundary == True:
            feature = {
                'type': 'Feature',
                'properties': {
                    'concentration': randint(1, 500)
                },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [point.x, point.y]
                }
            }
            geojson['features'].append(feature)

print json.dumps(geojson)
