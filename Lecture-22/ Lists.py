# l = 33
# print(l)
# print(type(l))

marks = [33, 44, 55, 66, 77, 88, 99, 00]
# print(type(marks)) # <class 'list'>
# print(marks[0]) # 33
# print(marks[1]) # 44
# print(marks[2]) # 55

# print(marks[-3])
# print(marks[len(marks)-3])

# if 44 in marks:
#     print("Yes")
# else:
#     print("No")    

# print(marks)
# print(marks[1:-1])
# print(marks[1:3])

# jumpIndex
# print(marks[1:8])
# print(marks[1:8:2])

# List Comprehension
# lst = [i*i for i in range(5)]
# lst = [i for i in range(5)]
# print(lst)

lst = [i for i in range(5) if i%2 == 0]
print(lst)
