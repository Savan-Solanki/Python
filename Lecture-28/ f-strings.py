letter = "Hey my name is {} and i am from {}"
name = "Savan"
country = "India"

print(letter.format(name,country))

# letter = "Hey my name is {1} and i am from {0}"
# name = "Savan"
# country = "India"
# print(letter.format(country,name))

# f-srting
print(f"Hey my name is {name} and i am from {country}")


price = 2364.046
txt = f"{price: .2f}"
print(txt)

# txt = "{price:.2f}"
# print(txt.format(price = 7686.29973))
