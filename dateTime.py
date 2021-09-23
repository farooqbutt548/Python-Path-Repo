                            # -------------   Date & Time 

'''import datetime as dt

date1 = dt.date.today()      # today date complete
print(date1)

print('years are ',date1.year)       # individual year
print('months are ',date1.month)      # individual month
print('days are ', date1.day)         # individual day


date2= dt.time(8, 36,33, 122212)
print('time is : ', date2)

print('houres are  : ', date2.hour)
print('minutes are : ', date2.minute)
print('seconds are : ', date2.second)
print('microseconds are : ', date2.microsecond)
                # --date & time combine
datetime_obj = dt.datetime(2021, 8,31, 23,59,59,999999)
print(datetime_obj)

print('the only date is : ',datetime_obj.date())
print('the only time is : ',datetime_obj.time())
print('the only years is : ',datetime_obj.year)
print('the only hours is : ',datetime_obj.hour)
        # -- current date time & datetime differences
current_dt = dt.datetime.now()        # today() or now()
print('current date & time is : ', current_dt)

birth_date = dt.datetime(1995, 4, 20, 8,37,12)      # selective datetime
print('your birth date is : ',birth_date)

my_age = current_dt-birth_date                  # date time difference
print('my actual age is : ', my_age)

print(type(current_dt))     # datetime type
print(type(birth_date))
print(type(my_age))         # difference two dates is timedelta obj

                            # Month of the year
import calendar as cal
mon = cal.month(1947, 8, 3)
print(mon)'''


#                               --------also can be used
'''import datetime
import calendar      

dt = datetime.datetime.now()            # current time and date
print (dt)

# print('years are: ',dt.year)            # individual time and date
# print('months are: ',dt.month)
# print('days are: ',dt.day)
# print('hour are: ',dt.hour)
# print('minutes are: ',dt.minute)
# print('seconds are: ',dt.second)
# print('microseconds are: ',dt.microsecond)

# all_cal = calendar.calendar(2021)          # all months of the year
# print(all_cal)

# cal = calendar.month(2022,4)            # specific month calendar
# print(cal)

# print('an other way to print month: ', datetime.datetime.now().month, 'mean September')
#           format of time and date

print(dt.strftime('the date is: %a, %dth %b, %Y'))  # %a,%A = day, %d=date, %b=month, %y,%Y=year'''
'''import time
t = time.localtime()
print(t)            # all type of time and date

print('years : ',t.tm_year)         # individual time or date
print('months : ',t.tm_mon)
print('days : ',t.tm_mday)
print(' hours :',t.tm_hour)
print(' minutes :',t.tm_min)
print(' seconds :',t.tm_sec)'''