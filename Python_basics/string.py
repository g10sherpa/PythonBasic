#Strings are Arrays
a = "Hello, World!"
print(a[1])

"""
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
Get the characters from position 2 to position 5 (not included):
"""
b = "Hello, World!"
print(b[1:3])

"""Negative Indexing
Use negative indexes to start the slice from the end of the string:
Get the characters from position 5 to position 1, starting the count from the end of the string:
"""
b = "Hello, World!"
print(b[-6:-2])

"""
String Length
To get the length of a string, use the len() function.
The len() function returns the length of a string:
"""
a = "Hello, World!"
print(len(a))


"""
The strip() method removes any whitespace from the beginning or the end:
"""
a = " Hello, World! "
print(a.strip())

"""
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
Use the format() method to insert numbers into strings:
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
