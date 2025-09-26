# strings are immutable
a="Harry!!!!!!!!!!Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","Suraj"))
# print(a.split(""))

blogHeading="introduction to Js"
print(blogHeading.capitalize())

str1="welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

print(str1.endswith("!!!"))

str1="Welcome to the Console !!!"
print(str1.endswith("to",4,10))


str1="He's name is Dan. He is an honest man."
print(str1.find("is"))
# print(str1.index("ishh"))

str1 ="WelcomeToTheConsole"
print(str1.isalnum())
str1="Welcome"
print(str1.isalpha())

str1="hello world"
print(str1.islower())

str1="We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())

str1="     " #using Spacebar
print(str1.isspace())
str2="     " #using Tab
print(str2.isspace())

str1="World Health Organization"
print(str1.istitle())#True if each word starts with a capital letter)

str2 ="To kill a Mocking bird"
print(str2.istitle())

# The replace() method can be used to rplace a part of the original string with another string.

str1="Python is a Compiled Language"
print(str1.replace("Compiled", "Interpreted"))

# startswith():
# The endswith() method checks if the string starts with a given value. If yes the return True, else False.else

str1="Python is a Interpreted Language"
print(str1.startswith("Python"))

# swapcase():
str1="Python is a Interpreted Language"
print(str1.swapcase())

# title();
# The title() method capitalizes each letter of the word within the string.

str1="He's name is Dan. Dan is an honest man."
print(str1.title())