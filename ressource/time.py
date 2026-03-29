from time import *
from datetime import timedelta
import datetime
from zoneinfo import ZoneInfo

def time_to_timestamp(date_str):
    dt = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())

def get_time():
    now = datetime.datetime.now(ZoneInfo("Europe/Paris"))
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%Hh%M")
    return "On est actuellement le " + date + " et il est " + time

print(get_time())