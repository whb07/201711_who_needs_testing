from time import sleep


def get_water_level_africa():
    sleep(15)
    return '15 cm'


def get_future_rainfall():
    rain_level = get_water_level_africa().split(' ')[0]
    return rain_level
