import datetime as d
import pytz as pz

tday = d.datetime.today()

print(tday.year)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta = d.timedelta(days=7) 

print(tday + tdelta) #Will add 7 Days in today

bday = d.datetime(2022,8,28)

tillbday = bday - tday

print(tillbday)

d_today = d.datetime.today()
d_now = d.datetime.now()
d_utc = d.datetime.utcnow()

print(d_today)
print(d_now)
print(d_utc)

dnew = d.datetime(2020,7,25,12,50,45,tzinfo=pz.utc) #2020-07-25 12:50:45+00:00  +00:00 - this is utc standad

print(dnew) 


for tz in pz.all_timezones:
    print(tz)
    
    
