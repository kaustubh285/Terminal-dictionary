import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def dictionari(word):
    if word in data:
        print("Meaning:")
        return data[word]
    else:
        word1 = get_close_matches(word,data.keys())[0]
        print("Did you mean "+word1+"?")
        confirmation =input("Press Y for yes, N for no:")
        confirmation = confirmation.lower()
        if confirmation =="y":
            print("Meaning:")
            return data[word1]
        else:
            print("Word Not Found!!!")
            print("Top similar words are:")
            return get_close_matches(word,data.keys())

word = input("Enter the word:")
word = word.lower()
meanings = dictionari(word)
i=1
for values in meanings:
    print(str(i)+")"+values)
    i=i+1
