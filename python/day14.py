# if else conditional statements in python

# a=int(input("Enter your age"))
# print("Your age is:",a)
#conditional operators
# >,<,>=,<=,==
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("You can drive")
#     print("yes")
# else:
#     print("You cannot drive")
#     print("No")
#     print("Yay!")
    
# applePrice = 190
# budget =200
# if(applePrice <= budget):
#         print("Alexa, add 1 kg Apples to the cart.")
#         else :
#             print("Alexa, do not add Apples to the cart.") ish me error find kr na hai

# applePrice=10
# budget=200
# if(budget-applePrice>50):
#     print("Alexa, and 1 kg Apples to the cart.")
# elif(budget-applePrice>70):
#     print("Its okey you can buy")
# else:
#     print("Alexa,do not add Apples to the cart.")

# num=int(input("Enter the value of num:"))
# if(num<0):
#     print("Number is negative.")
# elif(num==0):
#     print("Number is Zero.")
# else:
#     print("Number is positive.")
    
#     print("I am happy now")


# Nested if statements


num=18
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
    