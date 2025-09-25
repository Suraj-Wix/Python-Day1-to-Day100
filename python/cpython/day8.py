name = "Harry"
friend="Rohan"
anotherFriend='Lovish'

# apple="He said, \"I want to eat an apple"
apple='''He said,
Hi Harry
hey I am good.
"I want to eat an apple'''


print("Hello, " +name)
# print(apple)
print(name[0])
print(name[1])
print(name[3])
print(name[4])
# print(name[5])#IndexError: string index out of range
print("Lets use a for loop\n")
for character in apple:
    print(character)