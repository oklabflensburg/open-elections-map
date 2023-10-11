#!../venv/bin/python

import os
import csv
import click
import psycopg2

from pathlib import Path
from dotenv import load_dotenv


path = f'{Path.cwd().parent}/.env'
load_dotenv(path)  

                                                                                
conn = psycopg2.connect(                                                  
    database = os.getenv('DB_NAME'),
    password = os.getenv('DB_PASS'),
    user = os.getenv('DB_USER'),
    host = os.getenv('DB_HOST'),
    port = os.getenv('DB_PORT')
)


@click.command()
@click.argument('file')
def read_dataset(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        
        for row in reader:
            write_row(row)
            print(row)


def convert_datatype(val):
    if not isinstance(val, int):
        return None

    return val


def write_row(row):
    cur = conn.cursor()

    insert_query = """
        INSERT INTO votes (gemeinde, wahlkreisnummer, erfassungsgebietsnummer, 
        erfassungsgebietsart, ausgezaehlt_abweichend_gebiet, 
        ausgezaehlt_abweichend_ags, ausbleibend, wahlberechtigte_gesamt,
        wahlberechtigte_ohne_wahlschein, wahlberechtigte_mit_wahlschein,
        wahlberechtigte_nicht_im_wvz, waehlende_gesamt,
        waehlende_ohne_wahlschein, waehlende_mit_wahlschein, 
        urnenwaehlende_mit_wahlschein_in_urnenwahllokal,
        briefwaehlende_mit_wahlschein_in_urnenwahllokal,
        stimmen_ungueltige, stimmen_gueltige, d1, d2, d3, d4, d5,
        d6, d7, d8, d9, d10, d11,  d12, d13, d14, d15, d17,
        d18, d19, d20, d21, d22, d23) VALUES (%s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    insert_query_values = (
       row[0],
       row[1],
       row[2],
       row[2],
       row[3],
       row[4],
       row[5],
       convert_datatype(row[6]),
       convert_datatype(row[7]),
       convert_datatype(row[8]),
       convert_datatype(row[9]),
       convert_datatype(row[10]),
       convert_datatype(row[11]),
       convert_datatype(row[12]),
       convert_datatype(row[13]),
       convert_datatype(row[14]),
       convert_datatype(row[15]),
       convert_datatype(row[16]),
       convert_datatype(row[17]),
       convert_datatype(row[18]),
       convert_datatype(row[19]),
       convert_datatype(row[20]),
       convert_datatype(row[21]),
       convert_datatype(row[22]),
       convert_datatype(row[23]),
       convert_datatype(row[24]),
       convert_datatype(row[25]),
       convert_datatype(row[26]),
       convert_datatype(row[27]),
       convert_datatype(row[28]),
       convert_datatype(row[29]),
       convert_datatype(row[30]),
       convert_datatype(row[31]),
       convert_datatype(row[32]),
       convert_datatype(row[33]),
       convert_datatype(row[34]),
       convert_datatype(row[35]),
       convert_datatype(row[26]),
       convert_datatype(row[37]),
       convert_datatype(row[38]))

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(insert_query, insert_query_values)
                num_of_rows_affected = cur.rowcount
                new_row_id = cur.fetchone()
                print(new_row_id)
                conn.commit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    read_dataset()
