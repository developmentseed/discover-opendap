import json

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'discover_opendap'))
from discover_opendap import discover

sources_filepath = os.path.join(os.path.dirname(__file__), '..', 'tests', 'input.json')

with open(sources_filepath) as f:
    source_urls = json.load(f)

source_variables = {
    'https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/fcast/tavg3_2d_aer_Nx': [
        'totexttau',
        'sssmass25',
        'dusmass25',
        'bcsmass',
        'ocsmass',
        'so2smass',
        'so4smass'
    ],
    'https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/fcast/tavg1_2d_slv_Nx': [
        'v10m',
        'u10m',
        'ps',
        't850',
        't10m',
        'qv10m'
    ],
    'https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/fcast/tavg1_2d_flx_Nx': [
        'pblh'
    ]
}

sources = {}

for source in source_urls:
    sources[source] = {
        'urls': source_urls[source],
        'variables': source_variables[source]
    }

geojson_filepath = os.path.join(os.path.dirname(__file__), 'boundary.json')

with open(geojson_filepath) as f:
    geojson = json.load(f)

discover(sources, geojson['geometry'])
