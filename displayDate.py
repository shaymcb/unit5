#Shaylee McBride
#26Apr2018
#displayDate.py - tells you the date

from datetime import *

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February','March','April','May','June','July','August','September','October','November','December']

today = date.today()
weekday = days[today.weekday()]
month = months[today.month-1]

print('Today is',weekday+',',month,today.day,today.year)