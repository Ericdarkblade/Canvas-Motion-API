from ics import Calendar
import ics
import re
import requests
import arrow
import datetime

canvas_ics_url = "https://iu.instructure.com/feeds/calendars/user_lCk4udBsZzaFdyFnnhrE7dOiXPec3mCDIbPAo1Rv.ics"


class ParseException(Exception):
    pass


class Canvas_Event:
    def __init__(
        self,
        name: str,
        begin: arrow.Arrow,
        end: arrow.Arrow,
        duration: datetime.timedelta,
        description: str,
        uid: str,
    ) -> None:
        self.name = name
        self.begin = begin
        self.end = end
        self.duration = duration
        self.description = description
        self.uid = uid

        self.class_code = parse_class(self.name)
        self.assignment_title = parse_assignment(self.name)

    @classmethod
    def from_event(cls, event: ics.event.Event) -> "Canvas_Event":
        self = cls(
            name=event.name,
            begin=event.begin,
            end=event.end,
            duration=event.duration,
            description=event.description,
            uid=event.uid,
        )
        return self

    def __str__(self):
        return f"\
        name: {self.name}\n\
        begin: {self.begin}\n\
        end: {self.end}\n\
        duration: {self.duration}\n\
        description: {self.description}\n\
        class_code: {self.class_code}\n\
        assignment_title: {self.assignment_title}\n\
        "


def parse_canvas_calendar(
    url=canvas_ics_url,
) -> [Canvas_Event]:
    """Iterates through a Canvas ical url feed (ending in .ics)

    Args:
        url (str, optional): Eric Walkers ICAL URL. Defaults to Global Canvas ICS URL

    Raises:
        ParseException: Is thrown when an invalid URL is entered.

    Returns:
        [Canvas_Event]: Essentialy a dictionary that does computed inputs on an ics event.
    """

    def is_class(name: str) -> bool:
        """This function is a sin, and unoptimal

        Args:
            name (str): ical event description | ics.name

        Returns:
            Boolean: True/False whether the string is representative of a class.
        """
        try:
            parse_class(name)
            return True
        except ParseException:
            return False

    canvas_calendar = Calendar(requests.get(url).text)
    raw_events = canvas_calendar.events

    clean_events = []

    # try:
    for event in raw_events:
        if is_class(event.name):
            clean_event = Canvas_Event.from_event(event)
            clean_events.append(clean_event)
        else:
            pass
    return clean_events
    # except Exception:
    # raise ParseException("Invalid ICS URL Entered Parsed")


def parse_class(name: str) -> str:
    """Parses Canvas ICS event name|description for class title AT END OF STRING
     Example:
     'Review your Presentation #3 | Career Options [SP24-BL-INFO-I301-8506]'
         Returns:
    'INFO-I301'

     Args:
         name (str): event name

     Raises:
         NoParseException: Thrown if name does not contain output for pattern.

     Returns:
         str: Class Code within Input String
    """

    # Example Class Name
    # [SP24-BL-INFO-I301-8506]
    # Pattern Grabs 'INFO-I301'
    pattern = r"\[\w+-\w+-(\w+-\w+)-\d+\]$"

    class_code_match = re.search(pattern, name)
    if class_code_match:
        class_code = class_code_match.group(1)
        return class_code
    else:
        raise ParseException(f"No Class Code Found for string: '{name}'")


def parse_assignment(name: str) -> str:
    """Parses an ICS event name|description for assignment title


    Args:
        name (str): ics.event.name | ical Description

    Raises:
        ParseException: Raised if there is a regex error, if this gets raised we're in deep shit.

    Returns:
        str: Assignment Title
    """
    pattern = r"(.*)\s\[.*\]$"

    assignment_match = re.search(pattern, name)
    if assignment_match:
        assignment = assignment_match.group(1)
        return assignment
    else:
        raise ParseException(f"No Assignment Title found for string: '{name}'")


# Regex Test

if __name__ == "__main__":
    calendar = parse_canvas_calendar()

    print(len(calendar))
