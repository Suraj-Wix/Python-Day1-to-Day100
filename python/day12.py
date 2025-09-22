# strings slicing and operations on strings in python
name="suaj,addi"
# print(name[0:5]) yaha pr kitna number of element hai voh print kra sakte hai suarj=5 
print(len(name)) #yaha pr length pring kra dega jais 9


# fruit="Mango"
# len1=len(fruit)
# print("Mango is a",len1,
#       "letter  word.")


fruit="Mango"
mangoLen=len(fruit)
print(mangoLen)
# print(fruit[0:4])#including 0 but not 4
# print(fruit[1:4])#including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])


#Quick Quiz:
nm="suraj"
print(nm[-4:-2])