
from app.models import Ride, Station
import pandas as pd
import networkx as nx
from app import db
from sqlalchemy import or_, and_
import datetime


def create_edgelist(days_of_week=None, lollapolooza=False):
    """
    Filters Ride data by a variety of different fields,
    :param days_of_week: tuple of strings of the days of week; 0: Sunday, 1: Monday and so on
    :param lollapolooza: filter records to only lollapolooza days 8/1 - 8/4
    :return: list of rides to be input into pagerank function
    """

    selector = Ride.query

    if days_of_week:
        selector = selector.filter(or_("strftime('%w', ride.start_time) in {}".format(days_of_week)))

    if lollapolooza:
        # selector = selector.filter("ride.start_time between '2018-08-02' and '2018-08-05'")
        selector = selector.filter(Ride.start_time.between('2018-08-02', '2018-08-05'))

    print(selector)

    rides = selector.all()
    edges = pd.DataFrame.from_records([i.edge() for i in rides])
    print("INFO: the number of edges from query are {}".format(len(edges)))
    return edges


def compute_pagerank(edgelist, damping_factor=0.85):
    graph = nx.from_pandas_edgelist(edgelist, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
    return nx.pagerank_scipy(graph, alpha=damping_factor)


def join_station_data(G):
    stations = pd.read_sql(db.session.query(Station).statement, con=db.session.bind)
    rides = pd.DataFrame(list(G.items()), columns=["id", "ranking"])
    return stations.merge(rides, how="inner")

