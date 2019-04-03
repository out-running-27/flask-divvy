
from app.models import Ride, Station
import pandas as pd
import networkx as nx
from app import db


def create_edgelist():
    rides = Ride.query.limit(100000)
    edges = pd.DataFrame.from_records([i.edge() for i in rides])
    return edges


def compute_pagerank(edgelist, damping_factor=0.85):
    graph = nx.from_pandas_edgelist(edgelist, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
    return nx.pagerank_scipy(graph, alpha=damping_factor)


def join_station_data(G):
    stations = pd.read_sql(db.session.query(Station).statement, con=db.session.bind)
    rides = pd.DataFrame(list(G.items()), columns=["id", "ranking"])
    return stations.merge(rides, how="inner")
