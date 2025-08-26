import random
import datetime
import calendar
import time
# while True:
# x = datetime.datetime.now()
# print (x)
ran = random.random()
# today = datetime.date.today()
# yy = today.year
# mm = today.month
# now = datetime.datetime.now()
# print(calendar.month(yy,mm))
# print("todays date is ", today)
# print("the current time is ", now)
def randate(startdate, endate):
    print("printing a random date between ", startdate, " and ",endate, ": " )
    datefor = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startdate, datefor))
    endtime = time.mktime(time.strptime(endate, datefor))
    randomtime = starttime + ran * (endtime - starttime)
    randomdate = time.strftime(datefor, time.localtime(randomtime))
    return randomdate
print ("random date =", randate("1/1/2016", "8/26/2025"))