from __future__ import unicode_literals
import json
from hazm import *

class learner:
    def text_proccessor(self,text):
        normalizer = Normalizer()
        stemmer = Stemmer()
        lemmatizer = Lemmatizer()
        s = word_tokenize(normalizer.normalize(text))
        for i in range(len(s)):
            s[i] = lemmatizer.lemmatize(s[i])

        return s

    def argMax(self,l):
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


    def learning(self):
        file = open("training_set1.txt" , 'r')
        j = open('weights.txt' , 'r')
        result = open('result.txt' , 'w')
        weights = json.load(j)
        j.close()
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
            
            s = self.text_proccessor(text)
            activation_list = [0,0,0,0,0]
            for i in s:
                if not i in weights.keys():
                    weights[i] = [0,0,0,0,0]

                for a in range(5):
                    activation_list[a] += weights[i][a]

            # update weights
            estimate_label = self.argMax(activation_list)
            print(estimate_label)
            if estimate_label != real_label:
                for i in s:
                    for a in range(5):
                        if a == real_label:
                            weights[i][a] += 1
                        else:
                            weights[i][a] -= 1
        j = open("weights.txt" , "w")
        json.dump(weights,j)
        result.writelines(str(weights) + "\n")
        j.close()
        file.close()
        result.close()
if __name__ == "__main__":
    l = learner()
    l.learning()

