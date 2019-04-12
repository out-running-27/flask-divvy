
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app.models import Ride, Station

import pandas as pd
from app import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


from build_graph import create_edgelist, compute_pagerank, join_station_data


def write_full_data_set():
    query = "SELECT trip_id, start_time, end_time, bike_id, trip_duration, from_station_id, " \
            "s.station_name as from_station_name, to_station_id, s2.station_name as to_station_name, " \
            "s.latitude as from_station_lat, s.longitude as from_station_long " \
            "FROM Ride r " \
            "JOIN Station s ON r.from_station_id = s.id " \
            "JOIN Station s2 ON r.to_station_id = s2.id"

    df = pd.read_sql(query, con=db.session.bind)

    df.to_csv("./data/full_data_set.csv", index=False)


def write_csv(filename, days_of_week=None, lollapolooza=False):
    edges = create_edgelist(days_of_week=days_of_week, lollapolooza=lollapolooza)
    graph = compute_pagerank(edges, damping_factor=0.85)
    df = join_station_data(graph)
    df.to_csv("./data/{}.csv".format(filename), index=False)


if __name__ == '__main__':
    if not os.path.exists("./data/full_data_set.csv"):
        print('INFO: creating file full_data_set.csv')
        write_full_data_set()

    if not os.path.exists("./data/pagerank_all_dates.csv"):
        print('INFO: running pagerank on full dataset')
        write_csv("pagerank_all_dates")

    if not os.path.exists("./data/pagerank_weekend.csv"):
        print('INFO: running pagerank for weekend')
        write_csv("pagerank_weekend", days_of_week=('0', '6'))

    if not os.path.exists("./data/pagerank_weekday.csv"):
        print('INFO: running pagerank for weekday')
        write_csv("pagerank_weekday", days_of_week=('1', '2', '3', '4', '5'))

    if not os.path.exists("./data/pagerank_lolla.csv"):
        print('INFO: running pagerank for lolla')
        write_csv("pagerank_lolla", lollapolooza=True)
