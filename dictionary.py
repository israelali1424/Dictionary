# improt the Json libary
import json
from  difflib import get_close_matches

data = json.load(open("data.json"))
# print (data["high"])
# This is a function that will define a any word that you ask

def define(word):
    # this line makes it that the fuction will define words if they have uppercase letter in it
    word = word.lower()
    if word in data:
        return (data[word])
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead Enter Y or yes and N for no" % get_close_matches(word,data.keys())[0])
        if yn  == "Y" or yn =="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "I dont know what word you are looking for maybe check the spelling"
        else:
            return "We do not know what you are looking for"
    else:
        print ("This word does not  exist in the dictionary")


word = input("What you do you want to define")
print (define(word))

output = define(word)
if type(output) == list:
    for w in output:
        print(w)
else:
    print (output)
