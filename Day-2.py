											# Day-2
											# Date/Day - 2 July 2024/ Tuesday

"""
Today, on day - 2 we learn about the - "String slicing and other functions, list, dictionary and its function,
										and Sets in python".
			 List(Mutable), Dictionary and Tuple(Immutable) are the data structures in python.
"""

# String Slicing : A technique to extract a specific portion (substring) of a string. You can do this by specifying
#                  the start and end indices within square brackets [] separated by a colon :  .

# Note : The slicing of string indices will be starts from 0.
mystr = "I am Abhishek Tomar and On Day - 2 we learn String Slicing, list, dictionary and sets in python."

print(len(mystr))   # To print length of the string we use len() function.      Output: 95
print(mystr[0:20])  # To print string form a particular place use its range called as string slicing from 0 to 20.
print(mystr[0:100]) # if we take slicing number more than its original length they print till original length comes.

print(mystr[0:20:2]) # if we want to print our string with one space gap we use 2 after alot its range .
print(mystr[0:20:3]) # if we want to print our string with two spaces gap we use 3 after alot its range .
print(mystr[0:20:4]) # if we want to print our string with three spaces gap we use 4 after alot its range .

# But you want to think that if we skip or forget started and ending indices then what wil we happened. Let's try:
print(mystr[::])    # They print the entire length of  string as it is.
print(mystr[0::])   # They print the entire length of  string as it is.
print(mystr[::1])   # They print the entire length of  string as it is.

# Reverse The String.
print(mystr[::-1])  # This is the best way to reverse a string.
# output ==>>   .nohtyp ni stes dna yranoitcid ,tsil ,gnicilS gnirtS nrael ew 2 - yaD nO dna ramoT kehsihbA ma I


# Negative Slicing :
print(mystr[-66:-60])   # your starting slicing integer number is less than ending slicing if it
#                         doesn't your output may not be print on the output window some time.


# Some mostly used Functions used in string slicing :

print(mystr.isalnum()) # The isalnum() function in Python used to check if a string consists entirely of alphanumeric characters.
print(mystr.isalpha()) # The isalpha() method in Python is used to check if all the characters in a given string are alphabetic letters (a-z, A-Z). It returns True if all characters are alphabets, otherwise False.
print(mystr.endswith("python"))
print(mystr.count('o'))
print(mystr.isupper()) #  Returns True if all the characters are in upper case, otherwise False.
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("python", "java"))
print(mystr.swapcase()) # swapcase() =	Swaps cases, lower case becomes upper case and vice versa.


# List in Python : List is Mutable.
list1 = [34, 54, 67, 21, 45]
print(list1)

# Slicing in List :
print(list1[::-1])  # Reverse the given list.
print(list1[0:4])  # 4 is excluded and 0 is included.

list1.sort()    # sort the list.
print(list1)

# Some Functions in list :

print(list1.append(99))
print(list1.remove(34))
print(len(list1))
print(list1.reverse())
print(list1.insert(5,4))
print(list1.count(4))


# Tuple in python : It is Immutable .

Tuple = (1, 2, 3, 4, 5)
print(Tuple)

Single_Tuple_element = (9,)
print(Single_Tuple_element)

# Create a program to swap the two programs.

# Method - 1 :

a = 9
b = 8

# This is the easiest way to swap of two numbers.
a,b = b,a
print("The value of a is ", a, "and the value of b is ", b)

# Method - 2 :

c = 45
d = 9
temp = c
c = d
d = temp

print("value of c after swap is ", c, "value of d after swap is ",d)

# Dictionary in Python
dic = { }
# print(type(dic))

dic2 = {"Rohit":"Burger",
        "Virat":"Sandwich",
        "Axar":"Pizza",
        "Kuldeep":"Biryani"}

dic2["Rishab"] = "Kachori"      # To add the new items in the dictionary.
print(dic2)
print(dic2["Axar"])     # Access the elements from the dictionary.

dic3 = dic2.copy()
del dic2["Rishab"]
print(dic2)

print(dic2.get("Virat"))  # Get the key value of the dictionary.

print(dic2.keys())
print(dic2.values())
print(dic2.items())

dic2.update({"Beni":"Halwa Puri"})
print(dic2)



