


from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import wordinfo
import random



f = open('milkandhoney.txt', 'r')
lines = f.readlines()
lines = filter(lambda x: x !='\n',lines ) # removes '\n'
f.close()

sf1 = open("sf1.txt","w+")
sf2 = open("sf2.txt","w+")
sf3 = open("sf3.txt","w+")
sf4 = open("sf4.txt","w+")
sf5 = open("sf5.txt","w+")
sf6 = open("sf6.txt","w+")
sf7 = open("sf7.txt","w+")
sf1.close()
sf2.close()
sf3.close()
sf4.close()
sf5.close()
sf6.close()
sf7.close()


"""
#ideally these should be sets but im having issues since they are immutable
s1 = set()
s2 = set()
s3 = set()
s4 = set()
s5 = set()
s6 = set()
s7 = set()
"""
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []

syllable_dict = {}
syllablesets = [s1, s2, s3, s4, s5, s6, s7]
syllabefiles = [(s1,sf1),(s2,sf2),(s3,sf3),(s4,sf4),(s5,sf5),(s6,sf6),(s7,sf7)]
markov_dict = {}

def syllablewrite():
    for setsyllable, filesyllable in syllabefiles:
        for item in setsyllable:
            filesyllable.write("%s\n" %item)



def build_dict(words):
    """
    Build a dictionary from the words.
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    for i, word in enumerate(words):
        try:
            first, second, third = words[0][i], words[0][i+1], words[0][i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in markov_dict:
            markov_dict[key] = []
        markov_dict[key].append(third)
    return markov_dict



# get
def main():

    # i is the no. and line is the variable/text/line
    for i, line in enumerate(lines):
        tokens = word_tokenize(line.strip()) # stripping the \n bit and tokenizes
        print "line:",i, tokens, "\n\n"

        smaller_list = []

        if t in tokens:

        else:
            smaller_list.append(t)

        # there a limit to the number of queries so we should only do it when we have to
        #wordsort = [ (w, wordinfo.getSyllables(w)) for w in smaller_list]
        wordsort = [ (w, random.randint(1,7)) for w in smaller_list] # for debugging purposes
        #print "\t", wordsort,"\n" # the line with assigned syllables
        print build_dict(wordsort)
        for syl, sylset in enumerate(syllablesets):
            #print "\t current",syl+1 , ": \t" , sylset # syllable n sets current contents
            syltuples = filter(lambda x: x[1] == syl+1, wordsort)
            newset = [w[0] for w in syltuples]
            prevset = sylset

            #print "\t","newset",newset,"\n"
            sylset += newset
            #print "\t new",syl+1, ":\t", sylset ,"\n"

    syllablewrite()


if __name__ == "__main__":
    main()
