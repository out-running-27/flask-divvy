
from app.models import Ride, Station
import pandas as pd
import networkx as nx

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
# Session = sessionmaker(bind=engine)


def create_edgelist():
    rides = Ride.query.limit(1000)
    df = pd.DataFrame.from_records([i.edge() for i in rides])
    print(df.head())
    return df


def compute_pagerank(edgelist, damping_factor):
    graph = nx.from_pandas_edgelist(edgelist, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
    return nx.pagerank_scipy(graph, alpha=damping_factor)


def join_station_data():
    stations = Station.query.fetchall()
