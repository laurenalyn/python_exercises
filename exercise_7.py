# Tip Calculator
# Prompt the user for two things:

# The total bill amount
total_bill = float(raw_input("Total bill amount: "))
print(total_bill)
# The level of service, which can be one of the following: good, fair, or bad
service_lvl = raw_input("What was the service level? (good, fair, or bad)").lower()
print(service_lvl)
# Calculate the tip amount 
if service_lvl == "good":
    tip_total = float(total_bill * .2)
elif service_lvl == "fair":
    tip_total = float(total_bill * .15)
elif service_lvl == "bad":
    tip_total = float(total_bill * .1)
print("Tip Amount: %d " % (tip_total))
# the total amount (bill amount + tip amount). 
total_amount = total_bill + tip_total
# print(total_amount)
print("Total Amount Due: %d" % (total_amount))

# The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%
# Example session:

# $ python tip_calc.py
# Total bill amount? 100
# Level of service? good
# Tip amount: $20.00
# Total amount: $120.00
# $ python tip_calc.py
# Total bill amount? 48
# Level of service? bad
# Tip amount: $4.80
# Total amount: $52.80
# Hints:

# Remember that you need to convert the input from the user input to floats instead of ints. 
#   Use the float function instead of the int function.
# To format a float number as a dollar value, use Python's formatting syntax: '%.2f' % amount