import re
from pydap.client import open_url
from shapely.geometry import Point, Polygon, shape, box

def ingest(sources, geojson_polygon):
    polygon = shape(geojson_polygon)
    results = []
    for source_key in sources:
        source = sources[source_key]
        variables = source['variables']
        for url in source['urls']:
            date = extract_date_from_url(url)
            dataset = open_url(url)
            lats = dataset['lat'][:]
            lons = dataset['lon'][:]
            for i, lat in enumerate(lats):
                for j, lon in enumerate(lons):
                    point = Point(lon, lat)
                    in_boundary = polygon.contains(point)
                    if in_boundary == True:
                        for variable in variables:
                            var = dataset[variable]
                            value = var[0,i,j].data[0].item(0, 0, 0)
                            results.append({
                                "key": variable,
                                "value": value,
                                "date": date,
                                "coordinates": [float(lon), float(lat)]
                            })
    return results

def extract_date_from_url(url):
    pattern = re.compile(r'(\d{8})_(\d{2})\Z')
    match = pattern.search(url)
    return str(match.group(0))
