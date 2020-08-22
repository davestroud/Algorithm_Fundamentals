#-----------------------------------------------------------------------
# leapyear.py
#-----------------------------------------------------------------------

'''
The following pseudocode determines whether a year is a leap year or a common
year in the Gregorian calendar (and in the proleptic Gregorian calendar
before 1582). The year variable being tested is the integer representing
the number of the year in the Gregorian calendar.

if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
'''

import sys

# Accept an int year as a command-line argument. Write True to
# standard output if the year is a leap year. Otherwise write False

year = int(sys.argv[1])

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and (year % 100 != 0)
isLeapYear = isLeapYear or (year % 400 == 0)

print(isLeapYear)

#-----------------------------------------------------------------------

# python leapyear.py 2016
# True

# python leapyear.py 1900
# False

# python leapyear.py 2000
# True
