import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def meaning(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word]

    else:
        word1 = get_close_matches(word, data.keys())[0]
        print("Did you mean "+word1+"?")
        confirmation = input("Press y for Yes and n for No:")
        confirmation = confirmation.lower()
        if confirmation == "y":
            return data[word1]
        else:
            print("Sorry. Did not find the word -"+word)
            print("Top 3 similar results are:")
            print(get_close_matches(word, data.keys()))

word = input("Enter the word:")
word=word.lower()
output = meaning(word)
i =1
if type(output) == "str":
    print(output)
else:
    for items in output:
        print(str(i)+")"+items)
        i=i+1
