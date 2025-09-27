# function Arguments and return statement

# def average(a,b):
#  print("The average is ",(a+b)/2)

# average(4 ,6)    


# def average(a=9,b=1):
#  print("The average is ",(a+b)/2)

# # average(4 ,6) 
# average(b=9) 


# def name(fname, mname="Jhon",lname="Whatson"):
#     print("Hello", fname, mname, lname)
    
# name("Amy", "Agarwal", "jain")



# def average(a=9,b=1):
#  print("The average is ",(a+b)/2)

# # average(4 ,6) 
# average(b=9) 

# # average(b=9,a=21)
# average(a=21)

# def average(a, b, c=1):
#     print("The average is", (a + b + c) / 2)

# # Call the function here
# average(5, 6)

# def name(fname, mname, lname):
#     print("Hello", fname, mname, lname)
# # Call the function here
# name("Peter","Quill","Parker")

# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("Average is: ", sum/len(numbers))

# average(5,6,7,1)


# def name(**name):
#     print(type(name))
#     print("Hello", name["fname"], name["mname"],name["lname"])
# name(mname="Buchana", lname="Barnes",fname="James")



def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ", sum/len(numbers))
    # return 7
    return sum/len(numbers)

c=average(5,6,7,1)
print(c)
