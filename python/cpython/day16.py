# a=9
# b=8
# # gmean=(a*b)/(a+b)
# # print(gmean)
# c=8
# d=7
# gmean=(c*d)/(c+d)
# print(gmean)

def calculateGmean(a, b):
    mean=(a*b)/(a+b)
    print(mean)
    
def isGreater(a,b): 
   if(a>b):
    print("first number is greater")
   else:
     print("second number is greater or equal")  

def isLesser(a,b):
    pass # yeh function kuch nahi karega    

a=9
b=8
calculateGmean(a, b)
c=8
d=7
calculateGmean(c, d)
isGreater(a,b)