
from get_data import get_ride_data, get_station_data


def main():
    # 2018_Q1 uses different column names, not compatible with earlier years
    print("getting ride data")
    file_list = ['Divvy_Trips_2018_Q2', 'Divvy_Trips_2018_Q3', 'Divvy_Trips_2018_Q4']
    get_ride_data(file_list=file_list, trunc=True)
    print("getting station data")
    get_station_data()


if __name__ == '__main__':
    main()
