from datetime import date , time , datetime
today = date.today( )
now = datetime.now( )
print("Today's date is " , today)
print("\n Current Date and time is", now)
print("\nDate components", today.year, today.month, today.day)

import calendar

yy= 2001
mm= 9

print(calendar.month(yy, mm))
