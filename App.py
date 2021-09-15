import json
import multiprocessing.util
from difflib import get_close_matches
from difflib import SequenceMatcher

data= json.load(open("data.json"))

word= input("enter the word:")
matches= get_close_matches(word, data,2,0.8)


def word_meaning(w):
    w= w.lower()
    if word in data :
            return data[word]
    elif len(matches)>0:
        response= input("Did you mean {} ? Enter Y if yes or N if no.".format(matches[0]))
        if response .upper()== "Y":
            return data[matches[0]]
        elif response.upper() == "N" and len(matches)>1:
            response1= input("Then did you mean {} ? Enter Y if yes or N if no." .format(matches[1]) )
            if response1.upper() == "Y":

                return data[matches[1]]
            else:
                return "please double check the word as the word does'nt exist."
    else :
        return "Word doesn't exist. Please double check it."


output= word_meaning(word)
if  isinstance(output, (list)):
    sno= 1
    for i in output:
        print(sno,".", i)
        sno=sno+1
elif isinstance(output, type(None)):
    print("could not understand the word please re-enter")
else:
    print(word_meaning(word))
