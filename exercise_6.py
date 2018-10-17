# Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius, and 
# convert the value to degrees in Fahrenheit and display it to the user. 

#prompt user for a number in deg Celsius
temp_in_celsius = int(raw_input("Temperature in C? "))
#convert the value to degrees Fahrenheit
temp_in_fahrenheit = (temp_in_celsius * 1.8) + 32
print(temp_in_fahrenheit)


# Example session:
# $ python exercise_6.py
# Temperature in C? 28
# 82.4 F
# $ python exercise_6.py
# Temperature in C? -5
# 23 F
# Hint: the formula to convert degrees C to degrees F is: F = C x 1.8 + 32.