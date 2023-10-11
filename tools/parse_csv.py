#!./venv/bin/python

import csv
import click


def write_dataset(location, row):
    with open(f'{location.split(".")[0]}.parsed.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        spamwriter.writerow(row)


@click.command()
@click.argument('file')
def read_dataset(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        counter = 1

        for row in spamreader:
            if len(row) == 0:
                counter = counter + 1
            else:
                row.append(str(f'{counter:02}'))
                print(row)
                write_dataset(file, row)


if __name__ == '__main__':
    read_dataset()
