#!./venv/bin/python

import csv
import json



def read_csv_dataset():
    with open('data/20230324.parsed.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = []

        for row in reader:
            rows.append(row)

        return rows


def read_geojson_dataset():
    with open('data/kommunalwahlkreise_2018.geojson', 'r') as f:
        data = json.load(f)

        return data


def generate_properties(geojson, csv):
    for feature in geojson['features']:
        c = [x for x in csv for i, r in enumerate(x) if x[-1] == feature['properties']['NAME']]
        # print(c)
        feature['properties'].update({'candiates': c})
        print(feature['properties'])


def write_dataset(data):
    with open('kommunalwahlkreise_2018.updated.geojson', 'w') as f:
        json.dump(data, f)


def main():
    geojson = read_geojson_dataset()
    csv = read_csv_dataset()
    generate_properties(geojson, csv)


if __name__ == '__main__':
    main()
