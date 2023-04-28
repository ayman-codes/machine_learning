import contractions
import matplotlib.pyplot as plt
import string
import re
from cleantext import clean
import random



class Preprocessing_token():
    def __init__(self, token):
        self.token =token
        
    # returns the expanded version of contractions
    def remove_contractions(self, token):
        token = contractions.fix(token.lower())
        return token
    
    #convert all words to lower case
    def remove_uppercase(self, token):
        token = token.lower()
        return token
    
    #Remove Punctuation
    def remove_punctuation(self, token):
        token =  re.sub('[%s]' % re.escape(string.punctuation), '' , token)
        return token
    
    #Remove Numbers
    def remove_numbers(self, token):
        token = re.sub(r'\d+', '', token)
        return token
    
    #Remove whitespace
    def remove_whitespace(self, token):
        token = " ".join(token.split()) #split text then join with space between words
        return token
    
    #remove Emojis 
    def remove_emojis(self, token):
        regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',token)
    