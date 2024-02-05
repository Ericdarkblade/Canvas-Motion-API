import ics
from ics import Calendar
import requests
import re

url = "https://iu.instructure.com/feeds/calendars/user_lCk4udBsZzaFdyFnnhrE7dOiXPec3mCDIbPAo1Rv.ics"

# c = Calendar(requests.get(url).text)
c = None
with open("Scratch Crap/ICS Parsing/Canvas.ics", "r") as read_file:
    c = Calendar(read_file.read())


e = c.events
with open("Scratch Crap/ICS Parsing/Parsed Loop Information.txt", "w") as write_file:
    for event in e:
        write_file.write(f"Name:\n{event.name}" + "\n")
        write_file.write(f"Name Type:\n{type(event.name)}" + "\n")
        write_file.write(f"Begin:\n{event.begin}" + "\n")
        write_file.write(f"Begin Type:\n{type(event.begin)}" + "\n")
        write_file.write(f"End:\n{event.end}" + "\n")
        write_file.write(f"End Type:\n{type(event.end)}" + "\n")
        write_file.write(f"Duration:\n{event.duration}" + "\n")
        write_file.write(f"Duration Type:\n{type(event.duration)}" + "\n")
        write_file.write(f"Description:\n{event.description}" + "\n")
        write_file.write(f"Description Type:\n{type(event.description)}" + "\n")
