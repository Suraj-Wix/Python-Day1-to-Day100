# l =[3,5,6]
# print(l)
# print(type(l))

marks =[3,5,6,"Harry", True,6,7,2,32,245,23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# # print(marks[5])

# print(marks[-3])# 6
# print(marks[len(marks)-3])# True
# print(marks[5-3])# True
# print(marks[2])# Harry

# if 7 in marks:
#     print("Yes")
# else:
#     print("No")
    
# if "arry" in "Harry":
#     print("yes")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#     print("yes")

# print(marks)
# print(marks[0:len(marks)])# prints the entire list
# print(marks[1:8])# [5, 6, 'Harry']
# print(marks[1:8:2])

# animals=["cat", "dog", "fish", "elephant", "tiger", "lion", "zebra","donkey","cow"]
# print(animals)[::2]# ['cat', 'fish', 'tiger', 'zebra'] using positive indexes
# print(animals[-8:-1:2])# ['dog', 'elephant', 'lion', 'donkey'] using negative indexes

# animals=["cat", "dog", "bat","mouse","pig","horse","donkey","goat","cow"]

# print(animals[1:8:3])# ['dog', 'mouse', 'donkey']

# List Comprehensions

lst=[i*i for i in range(4)]
print(lst)
lst=[i*i for i in range(10)if i%2==0]
print(lst)


# Examples 1:Accepts items with the small letter "o"int the new list
names=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0=[item for item in names if "o" in item]
print(namesWith_0)

# Example: Accepts items which have more then 4 letters

names=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0=[item for item in names if (len(item)>4)]
print(namesWith_0)