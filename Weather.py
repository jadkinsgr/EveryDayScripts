import weather_forecast as wf
from datetime import datetime, date

location = input('Where do you live? ')
#location = 'Grand Rapids'
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
today2 = str(today) #API requires a string not a date so convert the date to a string here then call it

wf.forecast(place=location, time=current_time,
            date=today2, forecast="daily")
