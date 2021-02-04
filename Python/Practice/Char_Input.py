## Program to ask user name and age, then tell them what year they will turn 100.

import datetime
name = input("Please tell me your name: ")
age = int(input("Hi "+ name + ", please tell me your age on this year's birthday: "))
cyear = int(datetime.datetime.now().year)
futAge = str(int(cyear - age) + 100)

print(name + ", you will be 100 in the year", futAge +"!")