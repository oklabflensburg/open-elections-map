#!./venv/bin/python

import csv
import json



def read_csv_dataset():
    with open('data/luebeck/20230324.parsed.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = []

        for row in reader:
            rows.append(row)

        return rows


def read_geojson_dataset():
    with open('data/luebeck/kommunalwahlkreise_2018.geojson', 'r') as f:
        data = json.load(f)

        return data


def generate_properties(data, csv):
    for feature in data['features']:
        c = [x for x in csv for r in x if r == feature['properties']['NAME']]
        print(c)
        feature['properties'].update({'candidates': c})
        # print(feature['properties'])

    return write_geojson_dataset(data)


def write_geojson_dataset(data):
    with open('data/luebeck/kommunalwahlkreise_2018.updated.geojson', 'w') as file:
        json.dump(data, file, ensure_ascii=False)


def main():
    geojson = read_geojson_dataset()
    csv = read_csv_dataset()
    generate_properties(geojson, csv)


if __name__ == '__main__':
    main()
