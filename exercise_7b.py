# Tip Calculator
# Prompt the user for two things:
# the total bill amount & quality of service
end_message = "Your total comes to: "
great = "We are so glad you enjoyed your service!"
alright = "What areas could be improved?"
nope = "We are so sorry you didnt enjoy your service."

total_bill = float(raw_input("What is the total bill amount?: "))
print("Your bill total is $" + str(total_bill))

svc_level = raw_input("Was the service received good, fair, or bad? ").lower()
print("Your service level selected was " + svc_level)

# Calculate the tip amount 

if svc_level == 'good':
    tip_total = float(total_bill * .2)
    review_message = great 
elif svc_level == 'fair':
    tip_total = float(total_bill * .15)
    review_message = alright
elif svc_level == 'bad':
    tip_total = float(total_bill * .1)
    review_message = nope
elif svc_level != 'good' or svc_level != 'fair' or svc_level != 'bad':
    print("Please review your input")
print("Based on your input your tip should be $" + str(tip_total))

# the total amount (bill amount + tip amount). 
total_amount = tip_total + total_bill
total_amount = '${:.2f}'.format(total_amount)
print(review_message)
print(end_message, total_amount)

# Remember that you need to convert the input from the user input to floats instead of ints. 
#   Use the float function instead of the int function.
# To format a float number as a dollar value, use Python's formatting syntax: '%.2f' % amount
