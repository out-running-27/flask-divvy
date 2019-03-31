
from app.models import Ride
import pandas as pd

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
# Session = sessionmaker(bind=engine)


def create_edgelist():
    rides = Ride.query.limit(100)
    df = pd.DataFrame.from_records([i.edge() for i in rides])
    print(df.head())
    return df
