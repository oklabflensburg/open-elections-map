#!./venv/bin/python

import csv
import json
import click


def read_csv_dataset(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = []

        for row in reader:
            rows.append(row)

        return rows


def read_geojson_dataset(file):
    with open(file, 'r') as f:
        data = json.load(f)

        return data


def generate_properties(data, csv, key):
    for feature in data['features']:
        c = [x for x in csv for r in x if r == '{:0>2}'.format(feature['properties'][key])]

        print(c)
        feature['properties'].update({'candidates': c})

    return data


def write_geojson_dataset(file, data):
    with open(f'{file.split(".")[0]}.updated.geojson', 'w') as file:
        json.dump(data, file, ensure_ascii=False)


@click.command()
@click.argument('csv_file')
@click.argument('geojson_file')
@click.argument('match_key')
def main(csv_file, geojson_file, match_key):
    geojson_data = read_geojson_dataset(geojson_file)
    csv_data = read_csv_dataset(csv_file)
    data = generate_properties(geojson_data, csv_data, match_key)
    write_geojson_dataset(geojson_file, data)


if __name__ == '__main__':
    main()
