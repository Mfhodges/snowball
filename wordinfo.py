import sqlite3
import requests


""""
NOTE:
If you are making too many requests, they will be automatically limited. In that case, you will get back an error. Each individual query in a request counts towards the limit. The rate limiting is performed according to the "leaky bucket" algorithm.
The current rate limit is 350 requests per hour.

""""


#http://rhymebrain.com/talk?function=getRhymes&word=hello
def getRhyme(word):
     url = 'http://rhymebrain.com/talk'
     params = { 'function': 'getRhymes', 'word': word }
     response = requests.get(url, params).json()

     # Prints the word that rhymes the most with Python.
     return(response[0]['word'])


#http://rhymebrain.com/talk?function=getWordInfo&word=hello

def getSyllables(word):
     url = 'http://rhymebrain.com/talk'
     params = { 'function': 'getWordInfo', 'word': word }
     response = requests.get(url, params).json()


     return(response['syllables'])

#http://rhymebrain.com/talk?function=getPortmanteaus&word=blog
def getPortmanteaus(words):
     url = 'http://rhymebrain.com/talk'
     params = { 'function': 'getPortmanteaus', 'word': words }
     response = requests.get(url, params).json()


     return(response)





"""
[
    {
        "source": "blog,augmentation",
        "combined": "blogmentation,blaugmentation"
    },
    {
        "source": "blog,august",
        "combined": "blogust,blaugust"
    },
    {
        "source": "blog,logarithmic",
        "combined": "blogarithmic"
    }
]
"""
