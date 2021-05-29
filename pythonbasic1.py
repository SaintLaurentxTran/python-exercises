# Bython Basic 1


# 1. Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
# print('Twinkle, twinkle, little star, \n  How I wonder what you are! \n      Up above the world so high, \n      Like a diamond in the sky. \nTwinkle, twinkle, little star, \n  How I wonder what you are')


# 2. Write a Python program to get the Python version you are using. 
# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)


#3. Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# import calendar
# x = int(input("Input the year: "))
# y = int(input("Input the month: "))
# print(calendar.month(x, y))

# 34. Write a Python program to sum of two given (input) integers. However, if the sum is between 15 to 20 it will return 20. 
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))


# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


# 91. Write a Python program to swap two variables. Function name "swap2Vars"
ex: x = 5, y = 4
out: x = 4, y = 5
x = 6
y = 4
x, y = y, x
print(x)
print(y)
# 138. Write a Python program to convert true to 1 and false to 0. 
x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)


# 99. Write a Python program to clear the screen or terminal. 
import os
import time
os.system("ls")
time.sleep(2)
os.system('clear')