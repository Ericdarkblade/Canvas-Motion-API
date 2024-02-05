import ics
from ics import Calendar
import requests
import re

url = 'https://iu.instructure.com/feeds/calendars/user_lCk4udBsZzaFdyFnnhrE7dOiXPec3mCDIbPAo1Rv.ics'

canvas_calendar = Calendar(requests.get(url).text)



events = canvas_calendar.events


if __name__ == '__main__':
    for event in events:
        name = event.name
        print(name)