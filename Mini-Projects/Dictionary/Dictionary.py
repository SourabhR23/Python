import json
from difflib import get_close_matches

# Load .json file to Code
data = json.load(open('data.json'))

# Define translate function
def translate(word):

    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print('did you mean >> %s '%get_close_matches(word, data.keys())[0])
        decide = input('Click y for Yes or n for No: ')
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return("You have enter wrong word please type correct word and try again!")
        else:
            return("You have enter wrong input, please click y or n ")
    else:
        print("You have enter wrong word please type correct word ")

# Input from User
word = input("\nEnter the Word you want to search from dictionary: ")
result = translate(word)

# If word have more than one meaning
if type(result) == list:
    for item in result:
        print(">> " + item)
else:
    print(result)