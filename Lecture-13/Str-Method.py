# Strings are immutable

# For uppercase any string
a = "Apple"
print(a.upper()) # output : APPLE

# For lowercase any string
print(a.lower()) # output : apple

# rstrip() is used only for trailing(jsdh!!!) not for leadind(!!!djhvf)
b = "!!Mango !!!!!"
print(b.rstrip("!")) # output : !!Mango

# replace()
d = "World"
print(d.replace("World","Duniya")) # output : Duniya

# split() is convert string into list
x = "ab cd"
print(x.split(" ")) #output : ['ab', 'cd']

# capitalize()
y = "abcd"
print(y.capitalize()) # output : Abcd

# center() is .center(n) make length(nth)
z = "abcdefgh,absdnjhfv"
print(z.center(50)) # output :                abcdefgh,absdnjhfv

# count() is a count any world in string
print(z.count("a")) # output : 2

# endswith() is returen only true or false
z1 = "abcd!!!"
print(z1.endswith("!!!")) # output : true

# find() is used for find any word index of string
str = "Hey i am savan solanki" 
print(str.find("am")) # output : 6

# isalnum() is rutern only true when string in only A-Z, a-z, 0-9 otherwise return false
str1 = "Heyiamsavansolanki" 
print(str1.isalnum()) # output : True

# islower() is return true for all word is lowercase otherwise return false
print(str1.islower()) # output : False

# isprintable() is return true when all value is printable otherwise false 
str = "Hey i am savan solanki\n" 
print(str.isprintable()) # output : False (bcz \n is not printable) 

# isspace() used when value is white space

# istitle() return true when first letter of  all each word string is capitale otherwise false

# swapcase() is used for convert to lowercase and uppercase  and uppercase and lowercase

# title() is used for all first letter convert in uppercase
