import requests
from zipfile import ZipFile
import io
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "../data/")

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


# noinspection SqlWithoutWhere
def get_ride_data(file_list, trunc=False):
    session = Session()
    divvy_trip_url = 'https://s3.amazonaws.com/divvy-data/tripdata/'
    columns = ['trip_id', 'start_time', 'end_time', 'bikeid', 'tripduration',
               'from_station_id', 'to_station_id', 'gender', 'birthyear']

    if trunc:
        session.execute('DELETE FROM ride')
        session.commit()

    for file in file_list:
        r = requests.get(divvy_trip_url + file + '.zip')
        z = ZipFile(io.BytesIO(r.content))
        df = pd.read_csv(z.open(file + '.csv'), index_col="trip_id",
                         usecols=columns)
        df.columns = ['start_time', 'end_time', 'bike_id', 'trip_duration',
                      'from_station_id', 'to_station_id', 'gender', 'birth_year']
        df.to_sql('ride', con=engine, if_exists='append')
        print('Inserted {} into ride'.format(file))
        session.commit()
        session.close()


def get_station_data():
    session = Session()
    api = "https://feeds.divvybikes.com/stations/stations.json"
    columns = ["id", "stationName", "latitude", "longitude"]

    r = requests.get(api).json()
    df = pd.DataFrame(r["stationBeanList"], columns=columns)

    df.set_index("id", inplace=True)
    df.rename({"stationName": "station_name"}, axis='columns', inplace=True)

    print(df.head())

    # write to db to use in graph
    df.to_sql('station', con=engine, if_exists='replace')
    session.commit()
    session.close()


def main():
    # 2018_Q1 uses different column names, not compatible with earlier years
    print("getting ride data")
    file_list = ['Divvy_Trips_2018_Q2', 'Divvy_Trips_2018_Q3', 'Divvy_Trips_2018_Q4']
    get_ride_data(file_list=file_list, trunc=True)
    print("getting station data")
    get_station_data()


if __name__ == '__main__':
    main()
