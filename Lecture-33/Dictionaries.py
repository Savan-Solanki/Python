dic = {
    # "key": "value"'
    "name": "Savan",
    "age": "21"
}

print(dic["name"])

# print(dic["name2"]) => error
print(dic.get("name2"))

for key in dic.keys():
    print(dic[key])