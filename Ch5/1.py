'''
Exercise 5.1. The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
UNIX systems, the epoch is 1 January 1970.
>>> import time
>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds, plus the number of days since the epoch.
'''
import time

curr_time = time.time() #time in seconds since epoch

seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60
seconds_in_minute = 60 

days_since_epoch = int(curr_time / seconds_in_day)
remainder = curr_time % seconds_in_day

hours = int(remainder / seconds_in_hour)
remainder = remainder % seconds_in_hour

minutes = int(remainder / seconds_in_minute)
remainder = remainder % seconds_in_minute

seconds = int(remainder)

print(f"It is {hours}:{minutes}:{seconds} UTC, and {days_since_epoch} days since the UNIX epoch." )