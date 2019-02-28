# importing json for loading the dictionary
import json
# difflib so you don't have to have exact spelling of word you're searching for 
from difflib import get_close_matches

dictionaryData = json.load(open("data.json"))  # insert whatever dictionary data you want here


def dictionaryDefinition(word):
    # making all of the words lowercase to avoid capitalization errors
    word = word.lower()
    
	
    # if user spells word correctly, and it's not a proper noun, 
	# and it's in the database, it'll return the definition
    if word in dictionaryData:
        return dictionaryData[word]

    # this checks to see if a person asked for a proper noun (i.e. Texas)
    elif word.title() in dictionaryData:
        return dictionaryData[word.title()]

    #this checks to see if a person asked for an anycronym such as NATO
    elif word.upper() in dictionaryData:
        return dictionaryData[word.upper()]
		
    # checking to see if a word they typed isn't in the dictionary, but maybe they misspelled it?
    elif len(get_close_matches(word, dictionaryData.keys())) > 0:

        questionAboutWordClarity = input("Did you mean %s? Enter Y if yes or N if no. " % get_close_matches(word, dictionaryData.keys())[0])
        questionAboutWordClarity = questionAboutWordClarity.lower()

        # if user responds with yes, then it'll return the definition
        if questionAboutWordClarity == "y" or "yes" or "yah" or "yup" or "of course":
            return dictionaryData[get_close_matches(word, dictionaryData.keys())[0]]
        
        # if the user responds no, then it'll end the loop and they can try again
        elif questionAboutWordClarity == "n" or "no" or "nope" or "nah" or "eh":
            return "Sorry about that, please try again" 
        
        else:
            return "Sorry about that, please try again"

    else:
        return "The word isn't in my dictionary, please double check"

# running the program loop, 
# so they can keep asking definitions until their face melts off if they want 

while True:

	userRequestedWord = input("Enter a word you'd like the definition for, puhleeezz: (enter 86 to stop the program) ")
	
	if userRequestedWord == "86":
		print("The dictionary store called; they're runnin' out of you")
		break
		
	dictionaryDefinitionOutput = dictionaryDefinition(userRequestedWord)

	# this is for formatting, to make sure if the word has multiple definition it'll print on seperate lines
	if type(dictionaryDefinitionOutput) == list:
		for item in dictionaryDefinitionOutput:
			print(item)
	else:
		print(dictionaryDefinitionOutput)
