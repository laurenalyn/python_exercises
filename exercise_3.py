# Prompt the user for the missing words to a Madlib sentence using the input function. You will make up your own Madlib sentence, but here's an example:
# 
# ____(name)____'s favorite subject in school is ____(subject)____.
# With the above given sentence, this is what a user session might look like:
# 
# $ python madlib.py
# Please fill in the blanks below:
# ____(name)____'s favorite subject in school is ____(subject)____.
# What is name? Marty
# What is subject? math
# Marty's favorite subject in school is math.

name = input("What is your name? ") 
# Lauren
subject = input("What is your favorite subject in school? ")
# science
print(name +"'s favorite subject in school is " + subject)
# lauren's favorite subject in school is science