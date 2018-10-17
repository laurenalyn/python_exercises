# Work or Sleep In?
# Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. Example session:

day = int(raw_input("Please enter a number from 0 - 6 "))

# Fill in your code here
# The user will enter a number between 0 to 6 inclusive. Given this number, 
# print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, 
# and so on. Here's an example user session (this assumes you've named the 
# file exercise_5.py):
if day == 0:
    print("Sleep in")
elif day == 1:
    print("Go to work")
elif day == 2:
    print("Go to work")
elif day == 3:
    print("Go to work")
elif day == 4:
    print("Go to work")
elif day == 5:
    print("Go to work")
elif day == 6:
    print("Sleep in")
# $ python work_or_sleep_in.py
# Day (0-6)? 5
# Go to work
# $ python work_or_sleep_in.py
# Day (0-6)? 6
# Sleep in