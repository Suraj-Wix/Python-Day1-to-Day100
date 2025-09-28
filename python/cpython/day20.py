# Operations on Tuples in Python|python Tutorial-Day#25

# Tuples are ordered collection of data  itmes. 
# They store multiple itmes in  a single variable .
# Tuple items are separated by commas and enclosed within round brackets().
# Tuples are unchangeable meaning we can not alterthem after creation.

# for example 1:


tup=(1,2,76,342,32,"green",True)
# tup[:3]
#tup[0]=90// this will give an error as tuples are unchangeable
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[0])
#print(tup[34])

if 3421 in tup:
    print("Yes 342 is present in this tuple")
tup2=tup[1:4]
print(tup2)
    
    
    
# Example 1:

# country=("Spain","Italy","India","England","Germany")
# if "Germany" in country:
#     print("Germay is preset.")
# else:
#     print("Germany is absent.")
        
        
# 4 Range of Index:

# You can print a range of tuple items by specifying where do you want to start,
# where do you want to end if you want to skip elements in betweens the range.

# Syntax:

# Tuple[start:end:jumpIndex]
# Note: jump Index is optional. We will see this in given 
# example.

# Example: Printing elements within a particular range:

# animals=("cat","dog","bat","mouse","pig","horse","donkey","goat","cow")
# print(animals[3:7])# it will print from index 3 to index 6
# print(animals[-7:-2])# using negative indexes

# tup me sab list ki tarah hi hota different but hai ki 
# ki aap tuples ko change nhi kr sakte hai

# tuples are immutable
# String are immutable
# lists are mutable