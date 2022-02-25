import datetime
import calendar
from turtle import st

from numpy import PINF

bal = 5000
intrate = 13* 0.01
monpay = 500

today = datetime.date.today()

days_currentmonth = calendar.monthrange(today.year,today.month)[1]

days_EndofMonth = days_currentmonth - today.day

# print(today)
# print(days_currentmonth)
# print(days_EndofMonth)

startdate = today + datetime.timedelta(days=days_EndofMonth + 1)
enddate = startdate
#print(startdate)


while bal > 0:
    int_charge = (intrate / 12) * bal
    bal += int_charge
    bal -= monpay
    
    bal = round(bal,2)
    if bal < 0:
        bal = 0
        
    #bal = 0 if bal < 0 else round(bal,2)
    
    print(enddate,bal)
    
    days_currentmonth = calendar.monthrange(enddate.year,enddate.month)[1]
    #days_EndofMonth = days_currentmonth - today.day
    enddate = enddate + datetime.timedelta(days=days_currentmonth)