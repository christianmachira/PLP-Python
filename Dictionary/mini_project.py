# creating a program that will allow a user to input a word and then the program will return the definition of the word.
# The program will also return a message if the word is not found in the dictionary.
# the program will also consider input using different cases, upper loer or mixed

# importing the json module
import json
import difflib

# load json file
with open('/Users/christianmachira/Developer/Python PLP/Dictionary/data.json', 'r') as file:
    data = json.load(file)

# create a class
class dictionary:
        
        # create a method that takes a word as an argument
        def __init__(self, word):
            self.word = word

        # create a method that will return the definition of the word
        def get_definition(self):
            # check if the word is in the dictionary
            if self.word in data:
                return data[self.word]
            # check if the word is in the dictionary in lower case
            elif self.word.lower() in data:
                return data[self.word.lower()]
            # check if the word is in the dictionary in upper case
            elif self.word.upper() in data:
                return data[self.word.upper()]
            # check if the word is in the dictionary in title case
            elif self.word.title() in data:
                return data[self.word.title()]
            # adding word predicition intelligence to the program using the difflib module
            elif len(difflib.get_close_matches(self.word, data.keys())) > 0:
                yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % difflib.get_close_matches(self.word, data.keys())[0])
                if yn == "Y":
                    return data[difflib.get_close_matches(self.word, data.keys())[0]]
                elif yn == "N":
                    return "The word does not exist in the dictionary. Please double check"
                else:
                    return "We did not understand your entry"    
            else:
                return "The word does not exist in the dictionary"



# ask user for input
input_word= input("Enter a word: ")

# create an instance of the class
Dictionary = dictionary(input_word)

# look up the definition of the word
meaning = Dictionary.get_definition()

# print the definition
print(meaning)