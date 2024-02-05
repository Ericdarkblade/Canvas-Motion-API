from ics import Calendar
import ics
import requests
import arrow
import datetime
from exceptions import ParseException


class canvas_event:
    def __init__(
        self,
        name: str,
        begin: arrow.Arrow,
        end: arrow.Arrow,
        duration: datetime.timedelta,
        description: str,
    ) -> None:
        self.name = name
        self.begin = begin
        self.end = end
        self.duration = duration
        self.description = description

    @classmethod
    def from_event(cls, event: ics.calendar.Event) -> None:
        cls.name = event.name
        cls.begin = event.begin
        cls.end = event.end
        cls.duration = event.duration
        cls.description = event.description


def parse_canvas_calendar(
    url="https://iu.instructure.com/feeds/calendars/user_lCk4udBsZzaFdyFnnhrE7dOiXPec3mCDIbPAo1Rv.ics",
):
    try:
        canvas_calendar = Calendar(requests.get(url).text)
        raw_events = canvas_calendar.events

        clean_events: [canvas_event] = []

        for event in raw_events:
            clean_event = canvas_event.from_event(event)
            clean_events.append(clean_event)

        return clean_events
    except Exception:
        raise ParseException("Invalid ICS URL Entered Parsed")
