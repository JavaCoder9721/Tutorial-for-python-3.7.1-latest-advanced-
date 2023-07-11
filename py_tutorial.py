# I/O #
"""
I/O means input & output.
output is used to print a result or text.
input is used to take or ask something to the user.
Lets learn!
"""

# Output #

print("hello") # As you can see that i wrote "hello" in quotes in parantheses. This will print "hello".
print(1 + 2) # But this time, i didn't wrote anything in quotes, means i want to print the result of 1 and 2. as i used "(1 + 2)". it is not important to only use 2 numbers, you can use different operators and more number or formulas
print("The sum of 1 and 3 is ",1 + 3) # Just like the two this will print "The sum of 1 and 3 is 4" but this time i used the text without quotes and with quotes, means i want to print a message with the result.

# Input #

"""
input is used to take input like in a calculator for numbers or in a search engine for query
for input, we first need to learn about variables, but theres a way to use input without vars.
"""
print(input("Enter a string: ")) # As you can see that i used the input function with message"Enter a string: " for asking, in the brackets, this will first prompt the user and then it will print it.
# We can also convert an input to a double(floating point number) or a integer(whole number)
# Heres how:
print(int(float(input("Enter a float: ")))) # As you can see that i used int() function for converting the input into a whole number, its not important to only use input in an int function, you can use a string that have number or a float, i also used to the float() function to first convert the input to a floating point number then convert it into int, Example: if i entered "1.8" as the input, it will output "1"
## Variable (subpart) ##
"""
vars are used to store data, like for now we are just printing the input, and we didn't able to get the data of the input again. in this vars will help us.
python has 5 datatypes. But in python, you dont need to give the type of the var

"""
a = 100 # This is a way to declare variable, now this will declare a variable a with a value "100", becuase i didn't wrote the value in quotes, i will be able to add it with another numbers
# like
print(a + 4) # because i declared a var a then it will not raise a error, it will print "104" the value of a is 100 and im adding 4 to it, so it will print 104
# Heres are all datatypes
string = "hello" # String(str)
integer = 193 # Integer
double = 1.4 # floating point number
list = [1,"hello"] # list
dict = {"apple": "a healty food"} # Dictionaries
"""
As you know float & integer are used to store numbers
strings are used to store words/paragraphs/phrases
list are used to store many things at once
for printing list we just use the normal variable method but for taking a specific thing we use this print(list[<location>])
example-
list = [1,9]
print(list[1])
print(list[0])
This will print "9 \n 1" and for taking a bunch of specific things we use another different method
example-
list = [5,7,4,6]
print(list[0:2])
this will only print "5,7,4"
because we told the program to only print 3 things in the list
dictionary are used to store a key with its value
dict = {"apple": "healthy"}
unlike lists we dont use the location method instead we add the key to print the value of the key like
print(dict["apple"]) This will print "healthy" to the console.
we can also add input to variables.
"""

# Loops #

"""
if you want to print "hello" 4 or 5 times, you will use print statement 4 or 5 times but if i ask you to print it 100 times, then you dont need to use 100 times, loops will help you

"""
for i in range(10):
    print(i)
# This will print the counting to 1-10 because we loop i ten times, and note that the i were using, is now a variable
# There are some more simple ones, like while loop
# heres a while loop example
i = 0
while i > 5:
    print("hello")
    i = i + 1
# in while loops we have to declare the var first because we cant use a var without declaring it. while loops are not specifically used to loop, but they are used in infinite loops
# like-
"""
while True:
    print("hello")
This will print hello infinite times
if we want to end the loop we can use break statement, break statement works in all loops-
while True:
    print(1 + 1)
    break
for i in range(3):
    print(i)
    break
we can also use loops inside loops, they are called nested loops
"""





"""
Note: This is a advanced tutorial but not the best, if you want to learn all of the python, i refer to learn it by mistakes or read the python book.
if you don't need both options then you can read this and learn
i used all of my experience in this, so please start it or if i missed something then please message me in the issues section.
"""