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
separator = "-" * 40


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

#Text options and choice
texts_count = len(TEXTS)
print(f"We have {texts_count} texts to be analyzed.")
print(separator)
input_index = input(f"Enter a number between 1 and {texts_count} to select text: ")

#input index control
if not input_index.isnumeric():
    print(separator)
    print("Input only numeric values! Program now exits...")
    exit()
elif int(input_index) not in range(1,texts_count+1):
    print(separator)
    print(f"Please insert only number between 1 and {texts_count}! Program now exits...")
    exit()
else:
    text_choice = TEXTS[int(input_index)-1]

#text analyzator
separated_words = [word.strip(".,!?\n") for word in text_choice.split(" ") if not word == '']
analyzed_text = {"words" : separated_words,
                 "words_count" : len(separated_words),
                 "titlecase" : len([word for word in separated_words if word.istitle()]),
                 "uppercase" : len([word for word in separated_words if word.isupper() and word.isalpha()]),
                 "lowercase" : len([word for word in separated_words if word.islower()]),
                 "numeric_count" : len([word for word in separated_words if word.isnumeric()]),
                 "numeric_sum" :  sum([int(word) for word in separated_words if word.isnumeric()]),
                 "words_lenght" : {}
                 }

#printing out the analysis
print(separator)
print(f"""There are {analyzed_text["words_count"]} words in the selected text.
There are {analyzed_text["titlecase"]} titlecase words.
There are {analyzed_text["uppercase"]} uppercase words.
There are {analyzed_text["lowercase"]} lowercase words.
There are {analyzed_text["numeric_count"]} numeric strings.
The sum of all the numbers {analyzed_text["numeric_sum"]}""")

#gathering data for graph
for word in separated_words:
    if len(word) in analyzed_text["words_lenght"].keys():
        analyzed_text["words_lenght"][len(word)].append(word)
    else:
        analyzed_text["words_lenght"].setdefault(len(word), [word])

#printing out header of graph
print(separator)
print("""LEN|     OCCURENCES     |NR.""")
print(separator)

#printing out data of graph loop
i = 1
pokus = 1
while i <= max(analyzed_text["words_lenght"]): #loop while 'i' is less than longest word
    for key in analyzed_text["words_lenght"].keys():
        if key == i:
            value_count = len(analyzed_text["words_lenght"][key])
            print(f'{" "*(3-len(str(key)))}{key}|{"*"*value_count}{" "*(20 - value_count)}|{len(analyzed_text["words_lenght"][key])}')
            pokus = 1
            i += 1
        else:
            if pokus <= max(analyzed_text["words_lenght"]): #in case of non-existing key, repeat till all keys from analyzed_text are looped
                pokus += 1
                continue
            else:
                pokus = 1
                i += 1
                continue


exit()