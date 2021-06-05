'''
author = Jiri Gebauer
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#general variables
separator = "_" * 40


#users database
users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

#user login input
print(separator)
print("TEXT ANALYZATOR V1.0")
print(separator)
username = input("Please enter your username: ")
password = input("Please enter your password: ")
print(separator)

#login program
if username in users.keys():
    if password == users[username]:
        print(f"Welcome to the app {username}! You have successfully logged in.")
        print(separator)

    else:
        print("Wrong password!")
        print(separator)
        exit()

else:
    print("""This username does not exist! Please try again. 
#TIP: Login information is case-sensitive!""")
    print(separator)
    exit()

#Text options
text_count = len(TEXTS)
print(f"We have {text_count} texts to be analyzed.")
print(separator)
text_choice = input(f"Enter a number between 1 and {text_count} to select: ")
print(separator)

print(text_choice)






