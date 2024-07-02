										# Python  Day - 1
										# Date/Day - 1 July 2024  / Monday

"""
Today on Day - 1,  We learn about the comments, escape sequences , print statements, variables, constants, 
take input from the user and typecasting.
"""

# This is a single line comment.
"""
This is a multiline comment and
it is ignored by the python interpreter.
"""

print("Hello, I am Abhishek Tomar and I am prepare for wrost.")
print("Hello, I am Abhishek Tomar", "I am prepare for wrost.")  # Here we use , to connect two sentences.

print("I am a good boy\n")    # \n is a new line character which print the next statement in the new line.
print("I live in\t India")    # \t is insert tab escape sequence which create a large gap between two character.

# Take input from the user.
print("Enter the value of n: ")
n = input() # here the input stores in n as a string not as a integer.
print("the value of n is ",n)

# Now we learn about the typecasting as by creating a calculator and we take the input from the user.
print("Enter the number: ")
num1 = input()
print("Enter the number-2");
num2 = input()

print("The addition of these two numbers is: \n", int(num1) + int(num2))  # here we typecaste the string into integer by using int.
print("The subtraction of these two numbers is: \n", int(num1) - int(num2)) # here we typecaste the string into integer by using int.
print("The multiplication of these two numbers is: \n", int(num1) * int(num2))  # here we typecaste the string into integer by using int.
print("The division of these two numbers is: \n", int(num1) / int(num2))   # here we typecaste the string into integer by using int.

a = 45
b = 5.52
c = "my code"
d = "55"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("The sum of a + d is : ", a + b)
# print("The sum of a + d is : ", a + d)   # you get error in this line due to having different data types you want to add.

# so, to solve this error you want to type cast them into the same data type such as : int-int or str-str.
print("The sum of a + d is : ", int(a) + int(d))