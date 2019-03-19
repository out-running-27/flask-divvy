import requests
from zipfile import ZipFile
import io
import os
import pandas as pd
from app import db
from sqlalchemy import create_engine
from config import Config

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "../data/")

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

def get_ride_data():
    divvy_file = 'https://s3.amazonaws.com/divvy-data/tripdata/Divvy_Trips_2018_Q2.zip'

    r = requests.get(divvy_file)
    z = ZipFile(io.BytesIO(r.content))
    df = pd.read_csv(z.open('Divvy_Trips_2018_Q2.csv'), index_col="trip_id",
                     usecols=['trip_id', 'start_time', 'end_time', 'bikeid', 'tripduration', 'from_station_id',
                              'to_station_id', 'gender', 'birthyear'])
    df.columns = ['start_time', 'end_time', 'bike_id', 'trip_duration',
                            'from_station_id', 'to_station_id', 'gender', 'birth_year']
    df.to_sql('Ride', con=engine, if_exists='append')



def get_station_data():
    api = "https://feeds.divvybikes.com/stations/stations.json"
    columns = ["id", "stationName", "latitude", "longitude"]

    r = requests.get(api).json()
    df = pd.DataFrame(r["stationBeanList"], columns=columns)
    df.set_index("id", inplace=True)

    # write to csv to use in graph
    df.to_csv(data_dir + "station_info.csv")


def main():
    if not os.path.exists("../data/Divvy_Trips_2018_Q2.csv"):
        print("getting ride data")
        get_ride_data()
    else:
        print("file already exists")

    # if not os.path.exists("../data/station_info.csv"):

    # else:
    #     print("file already exists")
    print("getting station data")
    get_station_data()


if __name__ == '__main__':
    main()
