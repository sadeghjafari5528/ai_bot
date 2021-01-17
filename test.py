from __future__ import unicode_literals
import json
from hazm import *
#from learning import text_proccessor , argMax

def text_proccessor(text):
    normalizer = Normalizer()
    stemmer = Stemmer()
    lemmatizer = Lemmatizer()
    s = word_tokenize(normalizer.normalize(text))
    for i in range(len(s)):
        s[i] = lemmatizer.lemmatize(s[i])

    return s

def argMax(l):
    result = None
    x = "inf"
    for i in range(len(l)):
        if x == "inf":
            x = l[i]
            result = i
        elif l[i] > x:
            x = l[i]
            result = i
    return result

def testing():
    file = open("test_set.txt" , 'r')
    j = open('weights.txt' , 'r')
    weights = json.load(j)
    j.close()
    no_test = 0
    no_currect = 0
    while True:
        # Get next line from file 
        line = file.readline() 
        # if line is empty 
        # end of file is reached 
        if not line: 
            break

        text = line.split("/")
        real_label = int(text[1])
        text = text[0]
        
        s = text_proccessor(text)
        activation_list = [0,0,0,0,0]
        for i in s:
            if not i in weights.keys():
                weights[i] = [0,0,0,0,0]

            for a in range(5):
                activation_list[a] += weights[i][a]

        # calculate result
        estimate_label = argMax(activation_list)
        print(estimate_label)
        no_test += 1
        if estimate_label == real_label:
            no_currect += 1
        else: print(s)
    print("result : " , int(no_currect/no_test * 100))
    file.close()

testing()