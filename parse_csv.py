#!./venv/bin/python


import csv



def write_dataset(data):
    with open('edata/20230324.new.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)


def read_dataset():
    with open('data/20230324.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        counter = 1

        for row in spamreader:
            if len(row) == 0:
                counter = counter + 1
            else:
                row.append(str(f'{counter:02}'))
                print(row)



def main():
    data = read_dataset()
    # write_dataset(data)


if __name__ == '__main__':
    main()
