from __future__ import unicode_literals
import json
from hazm import *
import sqlite3

class Learner:
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

    def deleteStopWords(self , text , stopwords):
        t1 = []
        for w in text:
            if not w[0] in stopwords:
                t1.append(w)
        return t1

    def makeZeroList(self , n):
        l = []
        for i in range(n):
            l.append(0)
        return l

    def learning(self):
        print("learning")
        conn = sqlite3.connect("ai_db.db")
        cur = conn.cursor()
        j = open('weights.txt' , 'r')
        result = open('result.txt' , 'w')
        weights = json.load(j)
        j.close()
        l = cur.execute("select text , label from sample")
        #stopwords = list(open('resources/stopwords.txt' , 'r' , encoding="utf8").read().splitlines())
        lx = self.makeZeroList(16)
        for sample in list(l):
            real_label = int(sample[1])
            text = sample[0]
            
            s = self.text_proccessor(text)
            activation_list = self.makeZeroList(16)
            for i in s:
                if not i in weights.keys():
                    weights[i] = self.makeZeroList(16)

                for a in range(16):
                    activation_list[a] += weights[i][a]

            # update weights
            estimate_label = self.argMax(activation_list)
            #print(estimate_label , real_label)
            if estimate_label != real_label:
                lx[real_label] += 1
                for i in s:
                    for a in range(16):
                        if a == real_label:
                            weights[i][a] += 1
                        else:
                            weights[i][a] -= 1
        j = open("weights.txt" , "w")
        json.dump(weights,j)
        result.writelines(str(weights) + "\n")
        j.close()
        result.close()
        cur.close()
        conn.close()
        print(lx , sum(lx))
if __name__ == "__main__":
    l = Learner()
    l.learning()

