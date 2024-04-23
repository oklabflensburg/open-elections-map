#!./venv/bin/python

import csv
import click
import json
import re

from geojson import FeatureCollection, Feature, Point
from pathlib import Path


def read_input(src):
    features = []

    with open(src, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            properties = {}
            geometries = {}

            properties['constituency_id'] = row['constituency_id']
            properties['label'] = row['label']
            properties['address'] = row['address']
            properties['postal_code'] = row['postal_code']
            properties['city'] = row['city']

            properties['slug'] = get_slug(row['label'], row['city'], row['address'])
            geometries['coordinates'] = [row['latitude'], row['longitude']]

            f = {
                'geometry': geometries,
                'properties': properties
            }

            features.append(f)

    return features


def remove_chars(string):
    slug = string

    tpl = (('©', ''), ('"', ''), ('\\', ''), ('&', 'und'), ('(', ''), (')', ''))

    for item1, item2 in tpl:
        slug = slug.replace(item1, item2)

    return slug


def replace_umlauts(string):
    slug = string

    tpl = (('ü', 'ue'), ('Ü', 'Ue'), ('ä', 'ae'), ('Ä', 'Ae'), ('ö', 'oe'), ('Ö', 'Oe'), ('ß', 'ss'))

    for item1, item2 in tpl:
	    slug = slug.replace(item1, item2)

    return slug


def get_slug(label, city, address):
    title = re.sub('[\d\s!@#\$%\^&\*\(\)\[\]{};:,\./<>\?\|`~\-=_\+]', ' ', label)
    addr = re.sub('[\s!@#\$%\^&\*\(\)\[\]{};:,\./<>\?\|`~\-=_\+]', ' ', address)

    street = re.sub('\d.*', '', address)
    streets = list(set(street.split()))

    for item in streets:
        title = title.replace(item.strip(), '')

    slug = f'{title} {addr} {city}'.lower().strip()
    slug = remove_chars(slug)
    slug = re.sub(r'\s+', ' ', replace_umlauts(slug)).replace(' ', '-')

    return slug


def generate_geojson(features):
    fc = []

    crs = {
        'type': 'name',
        'properties': {
            'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'
        }
    }

    for feature in features:
        coordinates = feature['geometry']['coordinates']

        geometry = Point((float(coordinates[1]), float(coordinates[0])))
        properties = feature['properties']

        fc.append(Feature(geometry=geometry, properties=properties))

    c = FeatureCollection(fc, crs=crs)

    return c


@click.command()
@click.argument('src')
def main(src):
    filename = Path(src).stem
    parent = str(Path(src).parent)
    dest = Path(f'{parent}/{filename}.geojson')

    features = read_input(src)
    collection = generate_geojson(features)

    with open(dest, 'w', encoding='utf8') as f:
        json.dump(collection, f, ensure_ascii=False)


if __name__ == '__main__':
    main()
