from datetime import datetime
from pytz import timezone
import pytz


datetime.now()

est = timezone('America/Indiana/Indianapolis')
utc = pytz.utc

# EST DATE INFORMATION
year = 2024
month = 2
day = 5
hour = 14
minute = 15

est_date = est.localize(datetime(year=year,month=month,day=day,hour=hour,minute=minute))

print(f"EST Date: {est_date.isoformat()}")

print(f"UTC Date: {est_date.astimezone(utc).isoformat()}")